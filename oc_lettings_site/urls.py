""" urls for the all project """
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings

from .views import home

handler404 = 'oc_lettings_site.views.error_404_view'    # pylint: disable=C0103
handler500 = 'oc_lettings_site.views.error_500_view'    # pylint: disable=C0103


urlpatterns = [
    path('', home, name='home'),
    path('', include('lettings.urls')),
    path('', include('profiles.urls')),
    path('admin/', admin.site.urls),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]
