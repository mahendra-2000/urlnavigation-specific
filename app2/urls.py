from django.urls import path
from app2.views import *
app_name='teddy'

urlpatterns=[
    path('hello/',hello,name='hello'),
]