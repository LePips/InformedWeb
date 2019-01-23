from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers

from . import views

app_name = 'api'
urlpatterns = [
    # /api/candidates/
    path('candidates/', views.candidates_list),
    # /api/candidates/<id>
    path('candidates/<int:id>/', views.candidate_detail),
    # /api/candidates/<id>/elections
    path('candidates/<int:id>/elections/', views.candidate_elections),
    # /api/elections/
    path('elections/', views.elections_list),
    # /api/elections/<id>
    path('elections/<int:id>/', views.election_detail),
    # /api/elections/<id>/candidates/
    path('elections/<int:id>/candidates/', views.election_candidates)
]
