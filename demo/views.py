from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'base.html', {})


def demo1(request):
    return render(request, 'demo/demo1.html', {})