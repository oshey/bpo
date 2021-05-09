from django.urls import path

from accounts.views import TestView
from jobs.views import JobListView, JobCreateView, JobUpdateView, JobDeleteView

app_name = 'jobs'

urlpatterns = [
    path('test/', TestView.detail, name='test'),
    path('', JobListView.as_view(), name='list'),
    path('create/', JobCreateView.as_view(), name='create'),
    # path('update/', JobUpdateView.as_view(), name='update'),
    # path('delete/', JobDeleteView.as_view(), name='delete'),
]