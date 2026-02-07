from django.shortcuts import render
from django.http import HttpResponse
from myapp.app2.models import TennisClub
from django.db import connection
import json

def CourtDetails(request):

    res = TennisClub.objects.get(name = 'Ararat Tennis Club')

    print(connection.queries[-1]['sql'])
    print(res)


    data = {
        'name' : res.name,
        'location' : res.location,
        'quantity' : res.quantity,
        'price' : res.price,
        'image_main' : res.image_main.url if res.image_main else '/media/tennis_clubs/9.jpg/',
        'image_hover1' : res.image_hover1.url if res.image_hover1 else '/media/tennis_clubs/1.jpg/',
        'image_hover2' : res.image_hover2.url if res.image_hover1 else '/media/tennis_clubs/2.png/',
        'image_hover3':'/media/tennis_clubs/2.png/'
    }

    print(data['price'])
    return render(request, 'app4/CourtDetails.html', {'data':json.dumps(data)})
