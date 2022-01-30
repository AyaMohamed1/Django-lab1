from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#request -> response


def welcome(request):
    return HttpResponse('Welcome ^ ^')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

