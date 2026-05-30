from django.urls import path
from app.views import *

app_name = 'app'

urlpatterns = [
    path('http-test', http_test),
    path('json-test', json_test),
    path('', home, name='home'),
    path('about', about),
    path('contact', contact),
]
