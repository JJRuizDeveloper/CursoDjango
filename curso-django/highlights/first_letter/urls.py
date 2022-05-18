from django.urls import path
from . import views

urlpatterns = [
    path('<letter>', views.first, name='first'),
]