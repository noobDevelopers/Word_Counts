from django.http import HttpResponse as response
from django.shortcuts import render
def homepage(request):
    return render(request,'home.html')
def count(request):
    fulltext = request.GET['TextBox']
    words = fulltext.split(' ')
    
    return render(request,'count.html',{'fulltext':fulltext,'count':len(words)})
def about(request):
    return render(request,'about.html')