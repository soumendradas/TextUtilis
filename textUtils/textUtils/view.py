from django.http import HttpResponse
from django.shortcuts import render


def index(requests):
    return render(requests, 'index.html')


def about(requests):
    return render(requests, 'about.html')


def contact(requests):
    return render(requests, 'contact.html')


def analyze(request):
    dj_text: str = request.POST.get('text', "default")
    remove_punc = request.POST.get('remove_punc', 'off')
    capfirst = request.POST.get('capfirst', 'off')
    new_line_remove = request.POST.get('new_line_remove', 'off')
    space_remove = request.POST.get('space_remove', 'off')
    char_count = request.POST.get('char_count')

    analyze_text: str = dj_text
    perform_text: str = ""
    if remove_punc == "on":
        punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        temp_str: str = ""

        for char in analyze_text:
            if char not in punctuation:
                temp_str += char

        perform_text = perform_text + '|Remove punctuation|'
        analyze_text = temp_str

    if capfirst == 'on':
        analyze_text = analyze_text.upper()
        perform_text = perform_text + '|Capitalize character|'

    if new_line_remove == 'on':
        temp_str = ""
        for char in analyze_text:
            if char != "\n" and char != "\r":
                temp_str += char
        analyze_text = temp_str
        perform_text = perform_text + '|Remove new line|'

    if space_remove == 'on':
        temp_str = ""
        for i, char in enumerate(analyze_text):
            if not (analyze_text[i] == " " and analyze_text[i + 1] == " "):
                temp_str += char
        analyze_text = temp_str
        perform_text = perform_text+"|Remove extra spacer|"

    if char_count == 'on':
        t = len(dj_text)
        analyze_text = analyze_text + f"\nCharacter count : {t}"
        perform_text = perform_text + '|Character count|'

    if (remove_punc == 'on' or capfirst == 'on' or
            new_line_remove == 'on' or space_remove == 'on' or char_count == 'on'):
        params = {'perform': perform_text, 'analyze_text': analyze_text}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Some thing error.......................")
