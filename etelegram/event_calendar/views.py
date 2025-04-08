from .calendar_event import create_google_calendar_event, get_upcoming_events
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.http import JsonResponse


def create_event_view(request):
    # Просто приклад
    summary = "Нова зустріч"
    description = "Деталі зустрічі..."
    start_time = datetime(2025, 4, 10, 14, 0)
    end_time = start_time + timedelta(hours=1)

    event_link = create_google_calendar_event(summary, description, start_time, end_time)
    return JsonResponse({"event_link": event_link})




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

    return JsonResponse(simplified, safe=False)