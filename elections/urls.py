from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'elections'
# Currently use the Django admin. Urls, views, and templates need refactoring
urlpatterns = [
    # # /elections/
    # path('', views.elections_list, name='elections_list'),
    # # /elections/<id>
    # path('<str:id>', views.view_election, name='view_election'),
    # # /elections/edit/<id>
    # path('edit/<str:id>', views.edit_election, name='edit_election'),
    # # /elections/set/<id>
    # path('set/<str:id>', views.set_election, name='set_election'),
    # # /elections/create
    # path('create/', views.create_election, name='create_election')
]
