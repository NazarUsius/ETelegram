import json

from django.shortcuts import render, redirect

from .calendar_event import create_google_calendar_event, get_upcoming_events
from django.http import JsonResponse, HttpResponse
from datetime import datetime, timedelta
from django.http import JsonResponse

from .forms import EventForm





def create_event_view(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            event_link = create_google_calendar_event(
                summary=data['summary'],
                description=data['description'],
                start_time=data['start'],
                end_time=data['end']
            )
            return redirect('list_events')
    else:
        form = EventForm()

    return render(request, 'create.html', {'form': form})


def list_events_view(request):
    events = get_upcoming_events()
    simplified = []

    for event in events:
        simplified.append({
            'summary': event.get('summary'),
            'start': event['start'].get('dateTime', event['start'].get('date')),
            'end': event['end'].get('dateTime', event['end'].get('date')),
            'description': event.get('description'),
            'link': event.get('htmlLink'),
        })

    return render(request, 'calendar.html', {'json_data': simplified})