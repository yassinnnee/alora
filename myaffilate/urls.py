
from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('pricing',views.pricing,name='pricing'),
    path('about',views.about,name='about'),
    path('blog_home', views.blog_home, name='blog_home'),
    path('blog_post', views.blog_post, name='blog_post'),
    path('faq',views.faq, name='faq')
    
]