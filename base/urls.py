from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('posts/', views.posts, name="posts"),
    path('post/<slug:slug>', views.post, name="post"),
    path('profile/', views.profile, name="profile"),

    #CRUD PATHS

    path('createpost/', views.createPost, name="create_post"),
    path('updatepost/<slug:slug>', views.updatePost, name="update_post"),
    path('deletepost/<slug:slug>', views.deletePost, name="delete_post"),

    path('sendEmail/', views.sendEmail, name="send_email"),
]