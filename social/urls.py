from . import views
from django.urls import path

urlpatterns = [

    # url for homepage
    path('', views.PostList.as_view(), name="home"),
    # url for a more detailed view of a post
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # url to like a post
    path('like/<slug:slug>/', views.PostDetail.as_view(), name='post_like'),
    # url to post form
    path('user_post', views.UserPostView.as_view(), name='user_post'),

]
