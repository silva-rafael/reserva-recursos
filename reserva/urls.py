from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('registro/', views.registro_view, name='registro'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('accounts/login/', views.login_view, name='login'),
]
