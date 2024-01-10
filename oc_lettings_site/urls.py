from django.contrib import admin
from django.urls import path, include

from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('', include('lettings.urls')),
    path('', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
