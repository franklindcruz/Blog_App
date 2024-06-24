from django.urls import path
from . import views

urlpatterns = [
    path('demohome', views.demohome, name='demohome'),
    path('create', views.demo, name='create'),

    path('', views.index, name='home'),
    path('post/', views.post, name='post'),
    path('post_description/<int:id>',views.post_description, name='post_description'),
    path('delete_post/<int:id>', views.delete_post, name='delete_post'),
    path('edit_post/<int:id>', views.edit_post, name='edit_post'),
    
    path('register/',views.register, name='register'),
]
