from django.shortcuts import render, HttpResponse

def index(request): # index needs request whether it's used or not
    return HttpResponse("Hello World")
