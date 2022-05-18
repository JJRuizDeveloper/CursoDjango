from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estaticos/', views.estaticos, name='estaticos')

]
