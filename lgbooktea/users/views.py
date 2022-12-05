from django.shortcuts import render, HttpResponse

def index(request): # index needs request whether it's used or not
    test_data = {
        'message' : 'hello'
    }
    return render(request, 'index.html', test_data)
