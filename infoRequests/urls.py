from django.urls import path
from django.conf.urls import url

from . import views

app_name="requests"
urlpatterns = [
    # /requests/
    path('', views.requests_list, name='requests_list')
]
