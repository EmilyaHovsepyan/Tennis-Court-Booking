from django.urls import path
from .views import CourtDetails

urlpatterns = [
    path('', CourtDetails)
]