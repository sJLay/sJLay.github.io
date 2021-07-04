from django.urls import path
from AppDemo.views import appTest

urlpatterns = [
    path('appTest',appTest)
]