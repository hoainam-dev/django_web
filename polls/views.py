from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
 
def index(request):
    response = HttpResponse()
    response.write("<h1>Home Page</h1>")
    response.write("<ul><li><a href='/home'>Home Page</a></li><li>Contact Page</li></ul>")
    return response

def html(request):
    response = HttpResponse()
    response.write("<h1>Contact Page</h1>")
    response.write("<ul><li><a href='/home'>Home Page</a></li><li>Contact Page</li></ul>")
    return response
