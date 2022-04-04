from django.urls import path
from . import views

urlpatterns = [
    path('food/<int:id>/', views.food, name="food"),
    path('your_food/<str:name>/', views.your_food, name="your_food"),
    path('search_food/<int:id>/', views.search_food, name="search_food")
]
