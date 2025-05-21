from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingPage, name="landingPage"),
    path('<str:day_name>/', views.dayView, name='day'),
]
