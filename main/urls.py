from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.PollsListView.as_view(), name='list'),
]