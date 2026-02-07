from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from .models import TennisClub

def HomePage(request):
   return render(request, 'app2/HomePage.html')

def get_courts(request):
   page = request.GET.get('page', 1)
   court = TennisClub.objects.all().order_by('id')
   paginator = Paginator(court, 4) # [page1, page2] each page 4 courts
   page_obj = paginator.get_page(page)

   data = {
      'court': [
         {
            'name': i.name,
            'location': i.location,
            'price': i.price,
            'image': i.image_main.url if i.image_main else None
         }for i in page_obj
      ],
      'has_next': page_obj.has_next(),
      'has_previous' : page_obj.has_previous()
   }
   print('vuuuuuuuuuuuux')
   print(data)

   return JsonResponse(data)



