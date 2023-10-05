from django.urls import path, include
from django.http import request
from django.contrib import admin

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('barberHome.urls')),
  path('usuarios/', include('usuarios.urls')),
]