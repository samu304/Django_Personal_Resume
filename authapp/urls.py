from django.urls import path
from authapp import views

urlpatterns = [
    path('signup/', views.signup, name='signup_page'),
    path('login/', views.handle_login, name='login_page'),
    path('logout/', views.handle_logout, name='logout_page'),
]