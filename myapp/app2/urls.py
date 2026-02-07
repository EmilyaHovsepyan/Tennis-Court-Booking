from django.urls import path
from .views import HomePage, get_courts


app_name = 'myapp2'
urlpatterns = [
    path('main/', HomePage),
    path('ajax/get_courts/', get_courts)
]