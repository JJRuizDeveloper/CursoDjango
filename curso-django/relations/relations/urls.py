from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('one/', include('onetoone.urls')),
    path('many/', include('manytoone.urls')),
    path('manytomany/', include('manytomany.urls'))
]
