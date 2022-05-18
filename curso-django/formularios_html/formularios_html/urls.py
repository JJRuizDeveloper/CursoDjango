from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get/form/', views.getform, name="form"),
    path('get/goal/', views.getgoal, name="goal"),
    path('post/form', views.postform, name="postform"),
    path('post/goal', views.postgoal, name="postgoal")
]
