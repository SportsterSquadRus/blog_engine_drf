from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostsListView.as_view()),
    path('post/<int:pk>', views.PostDetialView.as_view()),
    path('post/create', views.PostCreateView.as_view())
]