from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('admin/', views.admin, name='admin'),
    path('adminpanel/', views.adminpanel, name='adminpanel'),
    path('music/<int:num>/', views.music, name='music')

]