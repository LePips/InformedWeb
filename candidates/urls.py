from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# Keep for reference
# router = routers.DefaultRouter()
# router.register(r'newCandidates', views.NewCandidateViewSet)

app_name = 'candidates'
# Currently use the Django admin. Urls, views, and templates need refactoring
urlpatterns = [
    # # /candidates/
    # path('', views.candidates_list, name='candidates_list'),
    # # /candidates/<id>
    # # path('<str:id>', views.view_candidate, name='view_candidate'),
    # # /candidates/edit/<id>
    # path('edit/<str:id>', views.edit_candidate, name='edit_candidate'),
    # # /candidates/set/<id>
    # path('set/<str:id>', views.set_candidate, name='set_candidate'),
    # # /candidates/create
    # path('create/', views.create_candidate, name='create_candidate')
]
