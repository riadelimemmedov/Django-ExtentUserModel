from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('change-password/',MyPasswordChangeView.as_view(),name='change-password'),
    path('change-password/done/',MyPasswordDoneView.as_view(),name='change-password-done')
]