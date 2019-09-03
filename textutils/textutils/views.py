# I have created this file - Hardik Maru

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    text_value = request.GET.get('t1')
    removepunctuation = request.GET.get('removepunctuation', 'off')
    uppercase = request.GET.get('uppercase', 'off')
    print(uppercase)
    lowercase = request.GET.get('lowercase', 'off')
    countcharacters = request.GET.get('countcharacters', 'off')
    countwords = request.GET.get('countwords', 'off')
    removedigits = request.GET.get('removedigits', 'off')
    analyzed_text = ""
    purpose = ""
    if removepunctuation == "on":
        purpose = "Remove Punctuation"
        punctuations = '''
        ~!@#$%^&*()_+{}|:"<>?'/.\,;][
        '''
        analyzed_text =""
        for char in text_value:
            if char not in punctuations:
                analyzed_text += char


    elif removedigits == "on":
        purpose = "Remove Digits"
        digits = '''
        0123456789
        '''
        for char in text_value:
            if char not in digits:
                analyzed_text += char


    elif countcharacters == "on":
        purpose = "Count Characters"
        for char in text_value:
            if char != " ":
                analyzed_text += char
        analyzed_text = str(len(analyzed_text))
        analyzed_text += " Characters."

    elif uppercase == "on":
        purpose = "Convert To Uppercase"
        for char in text_value:
            analyzed_text += char.upper()


    elif lowercase == "on":
        purpose = "Convert To Lowercase"
        for char in text_value:
            analyzed_text += char.lower()


    elif countwords == "on":
        purpose = "Count Words"
        analyzed_text = str(len(text_value.split(" ")))
        analyzed_text += " Words."


    else:
        return HttpResponse("Error")

    print(purpose)
    params = {'purpose': purpose, 'analyzed_text': analyzed_text}
    return render(request, 'analyze.html', params)