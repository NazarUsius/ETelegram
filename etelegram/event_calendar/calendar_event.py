from google.oauth2 import service_account
from googleapiclient.discovery import build
from django.conf import settings
from datetime import datetime, timedelta

from google.oauth2 import service_account
from googleapiclient.discovery import build
from django.conf import settings


def create_google_calendar_event(summary, description, start_time, end_time):
    # Аутентифікація
    credentials = service_account.Credentials.from_service_account_info(
        settings.GOOGLE_CREDENTIALS,
        scopes=['https://www.googleapis.com/auth/calendar']
    )

    service = build('calendar', 'v3', credentials=credentials)

    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': 'Europe/Kyiv',
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': 'Europe/Kyiv',
        },
    }

    event = service.events().insert(calendarId=settings.GOOGLE_CALENDAR_ID, body=event).execute()
    return event.get('htmlLink')  # Посилання на подію



from google.oauth2 import service_account
from googleapiclient.discovery import build
from django.conf import settings
from datetime import datetime, timezone

def get_upcoming_events(max_results=10):
    credentials = service_account.Credentials.from_service_account_info(
        settings.GOOGLE_CREDENTIALS,
        scopes=['https://www.googleapis.com/auth/calendar.readonly']
    )

    service = build('calendar', 'v3', credentials=credentials)

    now = datetime.utcnow().isoformat() + 'Z'  # поточний час в UTC, якого вимагає Google API

    events_result = service.events().list(
        calendarId=settings.GOOGLE_CALENDAR_ID,
        timeMin=now,
        maxResults=max_results,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])
    return events


from google.oauth2 import service_account
from googleapiclient.discovery import build
import os
import json

# Імпортуй ключі з settings або окремого файлу
from django.conf import settings

def get_calendar_service():
    credentials_info = settings.GOOGLE_CREDENTIALS
    credentials = service_account.Credentials.from_service_account_info(
        credentials_info,
        scopes=["https://www.googleapis.com/auth/calendar"]
    )
    service = build("calendar", "v3", credentials=credentials)
    return service

def delete_google_calendar_event(event_id):
    service = get_calendar_service()
    service.events().delete(calendarId=settings.GOOGLE_CALENDAR_ID, eventId=event_id).execute()