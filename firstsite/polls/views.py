from django.shortcuts import render

def say_hello(request):
    return render(request, template_name='hello.html')

def say_hello_dop(request):
    return render(request, template_name='hello_dop.html')