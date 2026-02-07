from django.urls import path
from .views import RegisterPage, CheckUsernameExists, SignInPage, SignInUsernameExists

app_name = 'myapp'

urlpatterns = [

    path('', RegisterPage, name='RegisterPage1'),
    path('s', SignInPage),
    path('ajax/CheckUsernameExists/', CheckUsernameExists,name='CheckUsernameValid'),
    path('ajax/SignInUsernameExists/', SignInUsernameExists),
]