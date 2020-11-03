from django.urls import path
from .views import DetailView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about, name='about'),
    path('service/',views.services, name='service'),
    path('gallery/',views.photos, name='gallery'),
    path('blog/',views.blogs, name='blog'),
    path('blogsingle/',views.blogsigle, name='blogsingle'),
    path('contact/',views.Contact, name='contact'),
    #path('form/',ContactView, name='form'),
    
    
]