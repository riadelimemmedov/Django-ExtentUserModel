"""movie_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homeView,name='homeView'),
    path('movies/',include('movies.urls',namespace='movies')),
    path('login/',loginView,name='loginView'),
    path('logout/',logoutView,name='logoutView'),
    path('users/',include('users.urls',namespace='users'))
]
admin.site.site_header = 'Movies Administration'#The text to put at the top of each admin page, as an <h1> (a string). By default, this is “Django administration”.
admin.site.index_title = 'Manage The Site' #The text to put at the top of each admin page, as an <h1> (a string). By default, this is “Django administration”.
