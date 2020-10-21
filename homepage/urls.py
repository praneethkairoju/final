from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about, name='about'),
    path('service/',views.service, name='service'),
    path('gallery/',views.gallery, name='gallery'),
    path('blog/',views.blog, name='blog'),
    path('blog-single/',views.blog, name='blog-single'),
    path('contact/',views.contact, name='contact'),
    
]