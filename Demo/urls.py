"""Demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from django.conf.urls import url
# from .views import index
from AppDemo.views import  appTest
from django.urls import include, path
from django.contrib import admin
from dbDemo.views import dbtest
from dbDemo.views import deleteUpdata
from dbDemo.views import changeData
from webDemo.views import webdemo
from dbDemo.views import find


urlpatterns = [
    # url(r'^index/', views.index) ,
    path('admin/', admin.site.urls),
    path('appDemo/', include('AppDemo.urls')),
    path('dbtest/', dbtest),
    path('apptest/',appTest),
    path('webdemo/',webdemo),
    path('deleteUpdata/',deleteUpdata),
    path('changeData/',changeData),
    path('find/',find),
]
