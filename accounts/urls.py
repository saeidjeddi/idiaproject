from django.urls import path

from .views.api import UserView


app_name = "account"

urlpatterns = [
    path('', UserView.as_view(), name='user'),
]
