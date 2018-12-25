from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'elections'
urlpatterns = [
    # /elections/
    path('', views.elections_list, name='elections_list'),
    # /elections/<id>
    path('<str:id>', views.edit_election, name='edit_election')
]
