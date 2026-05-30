from django.urls import path

from app.views import *

urlpatterns = [
    path('http-test', http_test),
    path('json-test', json_test),
    path('', home),
    path('about', about),
    path('contact', contact),
]
