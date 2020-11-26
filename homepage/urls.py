from django.urls import path

from . import views
from .views import (
    ServiceView,
    Service_detail,
    BlogView,
    GalleryView,
    BlogDetailView,
    

)

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about, name='about'),
    path('service/',ServiceView.as_view(), name='service'),
    path('gallery/',GalleryView.as_view(), name='gallery'),
    path('blog/',BlogView.as_view(), name='blog'),
    path('blog/<slug:slug>/',BlogDetailView.as_view(), name='blogsingle'),
    path('contact/',views.Contact, name='contact'),
    path('service/<slug:slug>/',Service_detail.as_view(), name='service_detail'),
    
    
]