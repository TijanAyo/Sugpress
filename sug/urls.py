from django.urls import path
from . import views
from .views import PostView, DetailPost, CreatePost, UpdatePost, DeletePost

urlpatterns = [
    path('', views.index, name= 'index'),
    # path('press/', views.press, name= 'press'),

    # Class based Url Routing
    path('press/', PostView.as_view(), name= 'press'), 
    path('post/<int:pk>/', DetailPost.as_view(), name= 'post_detail'),
    path('post/new/', CreatePost.as_view(), name= 'create_post'),
    path('post/<int:pk>/update/', UpdatePost.as_view(), name= 'update_post'),
    path('post/<int:pk>/delete/', DeletePost.as_view(), name= 'delete_post'),
    
    path('about/', views.about, name='about')
]

