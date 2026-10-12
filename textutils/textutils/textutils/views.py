from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'index2.html')

def analyze(request):

    #getting the text
    djtext = request.POST.get('text','default')

    #checkboxes
    removepunc = request.POST.get('removepunc','off')
    capitalize = request.POST.get('capitalize','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover =  request.POST.get('extraspaceremover','off')
    countchar = request.POST.get('countchar','off')

    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    characters = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'''
    analyzedtext = ""

    #checking checkboxes

    #removing punctuations
    if removepunc =="on":
        for char in djtext: 
            if char not in punctuations or char ==" " or char =="\n":
                analyzedtext = analyzedtext + char
            
        # params = {'purpose':'To remove punctuations','analyzedtext':analyzedtext}
        djtext = analyzedtext

    #converting to uppercase
    analyzedtext = ""
    if capitalize =="on":
        for char in djtext:
            analyzedtext = analyzedtext + char.upper()
        
        # params ={'purpose':'Convert to uppercase','analyzedtext':analyzedtext}
        djtext = analyzedtext

    #newline remover
    analyzedtext = ""
    if newlineremover =="on":
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzedtext = analyzedtext + char
        
        # params ={'purpose':'New line remover','analyzedtext':analyzedtext}
        djtext = analyzedtext

    #extra space remover
    analyzedtext = ""
    if extraspaceremover =="on":
        for index, char in enumerate(djtext):
            if not(char == " " and djtext[index+1] == " " and index+1 < len(djtext)):
                analyzedtext = analyzedtext + char
        
        # params ={'purpose':'Remove extra space','analyzedtext':analyzedtext}
        djtext = analyzedtext
    params ={'purpose':'Text analysis','analyzedtext':djtext}

    #counting characters
    if countchar =="on":
        charcount =0
        for char in djtext:
            if char in characters:
                charcount += 1
        
        params ={'purpose':'Counting characters','analyzedtext': charcount}
        
    # else:
    #     return HttpResponse("error")
  
    return render(request, 'analyze.html',params)

