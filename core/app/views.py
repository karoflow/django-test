from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def http_test(request):
    return HttpResponse('<h1>this is a test</h1>')

def json_test(request):
    return JsonResponse({'name':'karo'})

def home(request):
    return render(request, 'app/home.html')

def about(request):
    return HttpResponse('<h1>About</h1>')
    
def contact(request):
    return HttpResponse('<h1>Contact</h1>')