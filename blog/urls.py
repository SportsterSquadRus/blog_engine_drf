from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostsListView.as_view()),
    path('post/<int:pk>/', views.PostDetialView.as_view()),
    path('post/create/', views.PostCreateView.as_view()),
    path('post/update/<int:pk>', views.PostUpdateView.as_view()),
    path('post/delete/<int:pk>', views.PostDeleteView.as_view()),
    path('comment/create/', views.CommentCreateView.as_view()),
]