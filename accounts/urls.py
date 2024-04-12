from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.accounts_register_view, name='register_view'),
    path('profile/', views.accounts_profile_view, name='profile_view'),
    path('addpost/', views.accounts_addPost_view, name='addPost_view'),
    path('deletepost/<int:pk>', views.accounts_deletePost_view, name='deletePost_view'),
    path('updatepost/<int:pk>', views.accounts_updatePost_view, name='updatePost_view'),
]
