from django.shortcuts import render, redirect
from .models import Product, Nutriment
from django.contrib import messages
import numpy


def food(request, id):
    product = Product.objects.get(id=id)
    nutriment = Nutriment.objects.get(id=id)
    return render(request, "food.html", {'product': product, 'nutriment': nutriment})


def your_food(request, name):
    liste = []
    try:
        for data in Product.objects.filter(name__icontains=name):
            liste.append(data)
            product = liste[0:6]
    except UnboundLocalError:
        messages.warning(request,
                         "Produit non disponible dans la base de données"
                         )
        return redirect('index')
    return render(request,
                  "your_food.html",
                  {'data': product}
                  )


def search_food(request, id):
    liste = []
    product = Product.objects.get(id=id)
    for data in Product.objects.filter(categorie=product.categorie).order_by("ecoscore"):
        liste.append(data)
    substitute = numpy.random.choice(liste[0:25], 6, False)
    return render(request,
                  "search_food.html",
                  {'data': substitute,
                   'product': product}
                  )
