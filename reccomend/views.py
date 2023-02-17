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
