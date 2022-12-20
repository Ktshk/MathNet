from django.urls import path
from math_net_app import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about")
]
