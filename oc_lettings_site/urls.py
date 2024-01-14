from django.contrib import admin
from django.urls import path, include

from .views import home

handler404 = 'oc_lettings_site.views.error_404_view'
handler500 = 'oc_lettings_site.views.error_500_view'


urlpatterns = [
    path('', home, name='home'),
    path('', include('lettings.urls')),
    path('', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
