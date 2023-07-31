from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('about/', views.about, name='about_page'),
    path('service/', views.service, name='service_page'),
    path('resume/', views.resume, name='resume_page'),
    path('contact/', views.contact, name='contact_page'),
    path('blog/', views.blog, name='blog_page'),
]
