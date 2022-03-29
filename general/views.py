from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def food(request):
    return render(request, 'food.html')


def product404(request):
    return render(request, 'product404.html')
