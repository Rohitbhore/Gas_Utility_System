from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('status/<int:request_id>/', views.request_status, name='request_status'),
]
