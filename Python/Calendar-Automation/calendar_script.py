import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import dateutil.relativedelta as rd

google_colors = {1: 110, 2: 78, 3: 133, 4: 210, 5: 221,
                 6: 209, 7: 38, 8: 241, 9: 68, 10: 35, 11: 160}

SCOPES = ['https://www.googleapis.com/auth/calendar']


def create_event(service, calendar_id, start_time, end_time, summary, description=None, location=None, colorId=0, recurrence=None):
    event = {
        'summary': summary,
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': 'America/Sao_Paulo',
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': 'America/Sao_Paulo',
        },
        'colorId': colorId,
        'description': description,
        'location': location,
        'recurrence': recurrence,
    }

    event = service.events().insert(calendarId=calendar_id, body=event).execute()
    print(f'Event created: {event["htmlLink"]}')


def print_color(text, color_code):
    print(f'\033[38;5;{color_code}m{text}\033[0m')


def main():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        calendar_summary = input("Enter a name for the calendar: ")
        calendar = {
            'summary': calendar_summary,
            'timeZone': 'America/Sao_Paulo'
        }

        created_calendar = service.calendars().insert(body=calendar).execute()

        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            num_events = int(
                input(f'Enter the number of events for {day}: '))
            for i in range(num_events):
                summary = input("Enter the event name: ")
                if not summary or summary.isspace():
                    summary = f'event {i+1}'
                start_date = datetime.datetime.now() + rd.relativedelta(
                    weekday=getattr(rd, day[0:2].upper()))
                start_time = input(
                    "Enter the start time for the event: (HH:MM) ")
                start_time = datetime.datetime.strptime(
                    f'{start_date.strftime("%Y-%m-%d")} {start_time}', '%Y-%m-%d %H:%M')
                end_time = input("Enter the end time for the event: (HH:MM) ")
                end_time = datetime.datetime.strptime(
                    f'{start_date.strftime("%Y-%m-%d")} {end_time}', '%Y-%m-%d %H:%M')
                professor = input("Enter the description of the event: ")
                location = input("Enter the location of the event: ")
                print("Choose a color for the event:")
                for n, color in google_colors.items():
                    print(f'{n}. ', end='')
                    print_color('█', color)
                color = int(input("Enter the color number: "))
                rec_until = input(
                    "Enter the date until the event repeats weekly: (YYYY-MM-DD) ")
                recurrence = [
                    f'RRULE:FREQ=WEEKLY;UNTIL={rec_until.replace("-", "")}T235959Z'] if rec_until else None
                create_event(
                    service, created_calendar['id'], start_time, end_time, summary, professor, location, color, recurrence)

    except HttpError as error:
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()
