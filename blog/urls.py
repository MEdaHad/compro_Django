from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.PostGallery.as_view(), name='gallery_link'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
