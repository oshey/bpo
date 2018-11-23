from django.urls import path

from accounts.views import TestView

app_name = 'jobs'

urlpatterns = [
    path('test/', TestView.detail, name='test')
]