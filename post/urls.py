from django.urls import path    
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('post/',views.post, name='post'),
    path('post_description/<int:id>',views.post_description, name='post_description'),
    path('delete_post/<int:id>',views.delete_post, name='delete_post')
]   