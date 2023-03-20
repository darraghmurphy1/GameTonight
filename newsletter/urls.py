from django.urls import path
from . import views

urlpatterns = [
    path('newsletter/', views.add_subscriber, name='newsletters'),
]
