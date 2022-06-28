# i have created this file - Priyanshu
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about_us.html')

def analyze(request):
    #get the text
    orginal_djtext=request.POST.get('text','default')
    djtext=orginal_djtext

    #check box value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcounter=request.POST.get('charcounter','off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=''
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        params={'purpose':'Remove Punctuations','analyzed_text':analyzed}
        djtext=analyzed

    if fullcaps=='on':
        analyzed=''
        for char in djtext:
            analyzed+=char.upper()
        params={'purpose':'UpperCase','analyzed_text':analyzed}
        djtext = analyzed

    if newlineremover=='on':
        analyzed=''
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed+=char
        params={'purpose':'Remove NewLine','analyzed_text':analyzed}
        djtext = analyzed

    if extraspaceremover=='on':
        analyzed=''
        for index,char in enumerate(djtext):
            if not(djtext[index]==' ' and djtext[index+1]==' '):
                analyzed+=char
        params = {'purpose': 'Remove ExtraSpace', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcounter=='on':
        analyzed=len(djtext)
        params={'purpose':'Character Counter','analyzed_text':analyzed}


    if removepunc!='on' and fullcaps!='on' and newlineremover!='on' and extraspaceremover!='on' and charcounter!='on':
        return HttpResponse("Please select any option for analysis")

    elif(orginal_djtext==''):
        return HttpResponse("Please enter text in the textarea")
    else:
        return render(request, 'analyze.html', params)
