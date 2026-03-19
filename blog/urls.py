from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome, name='blog_welcome'),
    path('eco/<str:texto>/', views.eco, name='blog_eco'),
    path('info/', views.info, name='blog_info'),
]
