from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_favourite, name='favourite'),
    path('add_favourite/<int:post_id>/', views.add_favourite, name='favourite_add'),
    path('delete_favourite/<int:favourite_id>/', views.delete_favourite, name='delete_favourite'),
]
