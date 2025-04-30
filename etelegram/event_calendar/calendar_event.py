from google.oauth2 import service_account
from googleapiclient.discovery import build
from django.conf import settings
from datetime import datetime, timedelta

import google.auth.transport.requests

from google.oauth2 import service_account
from googleapiclient.http import HttpRequest
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

import logging
import time
from google.auth.exceptions import GoogleAuthError
from googleapiclient.errors import HttpError

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import HttpRequest
import google.auth.transport.requests
from datetime import datetime
import time
from django.conf import settings
import requests

def get_upcoming_events(max_results=10, retries=3, timeout=15):
    # Создание креденшелов
    credentials = service_account.Credentials.from_service_account_info(
        settings.GOOGLE_CREDENTIALS,
        scopes=['https://www.googleapis.com/auth/calendar.readonly']
    )

    # Создаём кастомный http с таймаутом
    session = requests.Session()
    request_adapter = google.auth.transport.requests.Request(session=session)

    now = datetime.utcnow().isoformat() + 'Z'  # Текущий UTC

    for attempt in range(retries):
        try:
            service = build(
                'calendar',
                'v3',
                credentials=credentials,
                cache_discovery=False  # важно для избежания лишних запросов
            )

            events_result = service.events().list(
                calendarId=settings.GOOGLE_CALENDAR_ID,
                timeMin=now,
                maxResults=max_results,
                singleEvents=True,
                orderBy='startTime'
            ).execute(num_retries=0)  # отключаем внутренние повторы

            events = events_result.get('items', [])
            return events

        except Exception as e:
            print(f"[Попытка {attempt + 1}] Ошибка запроса к Google Calendar: {e}")
            if attempt < retries - 1:
                time.sleep(2)  # пауза между попытками
            else:
                raise  # если все попытки исчерпаны — выбрасываем

    return []



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