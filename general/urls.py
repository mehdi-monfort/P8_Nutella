from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('food/<str:name>/', views.food, name="food"),
    path('product404/', views.product404, name="404"),
]
