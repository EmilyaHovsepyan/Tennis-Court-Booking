from django.shortcuts import render, get_object_or_404
from datetime import date, time
from django.http import HttpResponse, JsonResponse
from myapp.app2.models import TennisClub, SlotAvailability
import json, requests
from django.db.models import F


def BookingPage(request):
    id = 3
    day = 1
    court = get_object_or_404(TennisClub, id=id)

    Slot = SlotAvailability.objects.filter(TennisClub = court, date = date(2026, 2, day))

    mapp = {}
    for i in Slot:
        mapp[i.time.strftime('%H:%M')] = i.taken

    print(mapp)

    # print(court)
    return render(request, 'app3/BookingPage.html', 
            {'court':court, 
            'available':mapp, 
            'quantity':court.quantity})


def AjaxBookCourt(request):
    id = 3
    day = 1
    court = get_object_or_404(TennisClub, id = id)
    print('mmmmmmm')
    print(SlotAvailability.objects.filter(TennisClub=court, date = date(2026, 2, day)))
    print('mmmmmmm')

    if request.method == 'POST':

        # print(slot)
        res = json.loads(request.body)['timetable']

        for i in res:
            k, j = map(int, i.split(':'))
            t = time(k, j, 0)
            try:
                mr = SlotAvailability.objects.get(
                    TennisClub=court, date = date(2026, 2, day),time = t)
                SlotAvailability.objects.filter(pk = mr.pk).update(taken=F('taken') + 1)
            except SlotAvailability.DoesNotExist:
                SlotAvailability.objects.create(
                    TennisClub=court,
                    date = date(2026, 2, day),
                    time = t
                )
    print(SlotAvailability.objects.filter(TennisClub=court, date = date(2026, 2, day)))
    print('mmmmmmm')
    send_to_telegram('emmy reserved')
    return JsonResponse({'success':True})

def send_to_telegram(message):
    token = '-'
    chat_id = '-5108235380'
    url = f"-"
    payload = {'chat_id':chat_id, 'text':message}
    requests.post(url, data=payload)


