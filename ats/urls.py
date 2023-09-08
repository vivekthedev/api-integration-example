from django.urls import path
from . import views
urlpatterns = [
    path("", views.HomeView.as_view(), name='index'),
    path("candidates", views.all_cadidates, name='all_candidates'),
    path("candidates/new", views.new_cadidate, name='new_candidate'),
]