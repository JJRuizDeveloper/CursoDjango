from django.urls import path
from . import views

urlpatterns = [
    path('queries/', views.queries, name="queries"),
    path('update/', views.update, name="update")
]