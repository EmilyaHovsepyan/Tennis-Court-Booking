from django.urls import path
from .views import BookingPage, AjaxBookCourt

urlpatterns = [
    path('', BookingPage),
    path('ajax/bookcourt', AjaxBookCourt)
]