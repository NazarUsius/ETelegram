import json

from django.shortcuts import render, redirect

from .calendar_event import create_google_calendar_event, get_upcoming_events
from django.http import JsonResponse, HttpResponse
from datetime import datetime, timedelta
from django.http import JsonResponse

from .forms import EventForm

from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .calendar_event import delete_google_calendar_event
from django.contrib import messages





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

    return render(request, 'calendar/create.html', {'form': form})



def delete_event_view(request, event_id):
    if request.method == "POST":
        try:
            delete_google_calendar_event(event_id)
            messages.success(request, "Подію успішно видалено.")
        except Exception as e:
            messages.error(request, f"Помилка при видаленні: {e}")
        return redirect('list_events')  # Перенаправляє назад до списку подій

    return render(request, "calendar/delete.html", {"event_id": event_id})


def list_events_view(request):
    events = get_upcoming_events()
    simplified = []

    for event in events:
        simplified.append({
            'id': event.get('id'),
            'summary': event.get('summary'),
            'start': event['start'].get('dateTime', event['start'].get('date')),
            'end': event['end'].get('dateTime', event['end'].get('date')),
            'description': event.get('description'),
            'link': event.get('htmlLink'),
        })

    return render(request, 'calendar/calendar.html', {'json_data': simplified})