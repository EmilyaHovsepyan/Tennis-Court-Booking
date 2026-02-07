from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
import json

def RegisterPage(request):
   return render(request, 'app1/RegisterForm.html')

def SignInPage(request):
   return render(request, 'app1/SignInForm.html')
      

def CheckUsernameExists(request): #AJAX
   if request.method == 'POST':
      data = json.loads(request.body)

      username = data['username']
      password = data['password']
      check = User.objects.filter(username = username).exists()

      if check:
         return JsonResponse({'passed':False})
      else:
         user = User.objects.create_user(username = username, password = password)
         login(request, user)
         return JsonResponse({'passed':True})

def SignInUsernameExists(request): #AJAX
   if request.method == 'POST':
      data = json.loads(request.body)
      print(data)
      username = data['username']
      password = data['password']

      user = authenticate(request, username = username, password = password)

      if user is not None:
         login(request, user)
         return JsonResponse({'passed':True})
      else:
         return JsonResponse({'passed':False})