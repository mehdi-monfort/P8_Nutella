from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Product


def your_food(request, name):
    liste = []
    try:
        for data in Product.objects.filter(name__icontains=name):
            liste.append(data)
            product = liste[0:6]
        return render(request, "your_food.html", {'data': product})
    except UnboundLocalError:
        return redirect("/product404")


def food(request, name):
    liste = {}
    for data in Product.objects.values_list("ecoscore").order_by("ecoscore"):
        liste.append(data)
        product = liste[0:6]
    return render(request, "food.html", {'data': product})

