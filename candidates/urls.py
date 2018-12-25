from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'candidates'
urlpatterns = [
    # /candidates/
    path('', views.candidates_list, name='candidates_list'),
    # /candidates/<id>
    path('<str:id>', views.edit_candidate, name='edit_candidate'),
    # /candidates/set/<id>
    path('set/<str:id>', views.set_candidate, name='set_candidate')
]
