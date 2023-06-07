"""
URL configuration for personalblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from blog.views import list_posts, detail_post, create_post
from django.contrib.auth import views as auth_views
from django.shortcuts import render, get_object_or_404, redirect
from django.views.defaults import page_not_found


urlpatterns = [
    path('', list_posts, name='home'),
    path('posts/', list_posts, name='list_posts'),
    path('posts/<int:id>/', detail_post, name='detail_post'),
    path('posts/create/', create_post, name='create_post'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='list_posts'), name='logout'),
]

handler404 = 'blog.views.page_not_found'