from django.urls import path
from django.conf.urls import url

from . import views

app_name="requests"
urlpatterns = [
    # /requests/
    path('create', views.create_info_request, name='create_info_request')
]
