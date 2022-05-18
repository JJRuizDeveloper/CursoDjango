from django.urls import path
from . import views

urlpatterns = [
    path('', views.optional, name='optional'),
    path('<str:name>', views.optional, name='optional'),
]