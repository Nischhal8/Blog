from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('',PostView.as_view(), name='blog-home'),
    path('about/',views.about, name='blog-about'),
    path('post/<int:pk>/',PostDetailview.as_view(), name='post-detail' ),
    path('post/<int:pk>/update/',UpdatePostview.as_view(), name='post-update' ),
    path('post/<int:pk>/delete/',PostDeleteview.as_view(), name='post-delete' ),
    path('post/new/', CreatePostview.as_view(), name='create-post'),
]