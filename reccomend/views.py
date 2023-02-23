from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'home.html')

def Python(request):
    return render(request, 'python.html')

def JavaScript(request):
    return render(request, 'javascript.html')

def Django(request):
    return render(request, 'django.html')

def React(request):
    return render(request, 'react.html')

def Vue(request):
    return render(request, 'vue.html')

def Bootstrap(request):
    return render(request, 'bootstrap.html')

def Angular(request):
    return render(request, 'angular.html')

def DjangoRest(request):
    return render(request, 'django.html')

def TensorFlow(request):
    return render(request, 'tensorflow.html')
