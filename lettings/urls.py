from django.urls import path
from .views import index, letting

urlpatterns = [
    path('lettings/', index, name='lettings_index'),
    path('lettings/<int:letting_id>/', letting, name='letting')
]
