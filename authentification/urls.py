from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout'),
    path('signup/', views.signup, name='signup'),
]
