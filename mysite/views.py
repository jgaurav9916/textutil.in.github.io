#i have created this file - gaurav

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    #return HttpResponse("home")

def analyzer(request):
    #get the text
    djtext = request.GET.get('text','default')
    removepun = request.GET.get('removepunc','default')
    fullcaps = request.GET.get('fullcaps','off')
    spaceremover = request.GET.get('spaceremover','off')
    newlineremover = request.GET.get('newlineremover','off')
    countchar = request.GET.get('countchar','off')
    print(removepun)
    print(djtext)
    if removepun == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char 
                #analyze the text
        params={'purpose':'Remove Punctutations','analyzed_text':analyzed }
        return render(request,'analyze.html',params)

    elif(fullcaps == "on"):
        analyzed=""
        for char in djtext:
            analyzed= analyzed + char.upper()
        params={'purpose':'Upper Text','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif spaceremover == "on":
        analyzed = djtext.strip()

        params = {'purpose': 'Remove space', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char is not '\n':
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover ', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    elif countchar =="on":
        analyzed = 0
        for char in djtext:
            analyzed = analyzed + 1
        params = {'purpose': 'Count Characters', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("ERROR")

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
#def capfirst(request):
 #   return HttpResponse('''capitalize first<a href="http://127.0.0.1:8000/">HOME</a>''')

#def newlineremove(request):
 #   return HttpResponse('''new line remover<a href="http://127.0.0.1:8000/">HOME</a>''')

#def spaceremove(request):
    #return HttpResponse("space remover")

#def countchar(request):
    #return HttpResponse('''count character<a href="http://127.0.0.1:8000/">HOME</a>''')