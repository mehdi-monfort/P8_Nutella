from django.urls import path
from . import views

urlpatterns = [
    path('your_food/<str:name>/', views.your_food, name="your_food"),
]
