from datetime import date, datetime, timedelta

def date_range(start_date: date, end_date: date, step: timedelta):
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += step

def datetime_range(start_datetime: datetime, end_datetime: datetime, step: timedelta):
    current_date = start_datetime
    while current_date <= end_datetime:
        yield current_date
        current_date += step
