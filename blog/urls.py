from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home_view, name='home_view'),
    path('bloglist/', views.blog_list_view, name='blog_list'),
    path('blogdetail/<int:pk>', views.blog_detail_view, name='blog_detail'),
    path('commentcreate/<int:pk>', views.blog_comment_create_view, name='commentCreate_view'),
    path('updateComment/<int:pk>', views.blog_updateComment_view, name='updateComment_view'),
    path('deleteComment/<int:pk>/<int:pk_post>', views.blog_deleteComment_view, name='deleteComment_view'),
]
