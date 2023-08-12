from . import views
from django.urls import path

urlpatterns = [
   path('',views.home, name='home'),
   path('home/',views.home, name='home'),
   
   path(r'^category/(?P<field>[a-z]+)$', views.category, name='category'),
   
   path('about-dev/',views.about_dev,name='about_dev'),
   path('delete/<str:key>', views.delete,name='delete'),
   path('like/<str:post_id>',views.like,name='like'),
   path('dislike/<str:post_id>',views.dislike,name='dislike'),
]
