from django.urls import path
from lojaApp import views



urlpatterns = [
    path('',views.index,name='index'),
]
