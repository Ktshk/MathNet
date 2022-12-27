from django.urls import path
from math_net_app import views

urlpatterns = [
    path('', views.login, name="login"),
    path('about/', views.about, name="about")
]
