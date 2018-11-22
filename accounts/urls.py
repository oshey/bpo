from django.urls import path

from accounts.views import TestView

app_name = 'accounts'

urlpatterns = [
    path('test', TestView.detail, name='test')
]