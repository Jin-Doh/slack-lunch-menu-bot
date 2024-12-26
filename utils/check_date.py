from datetime import datetime, timedelta


def is_working_day(date: datetime) -> bool:
    return date.weekday() < 5  # 0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일


def is_lunch_hour(date: datetime) -> bool:
    return date.hour == 11


def is_lunch_minute(date: datetime) -> bool:
    start_minute = 10
    end_minute = 30
    return start_minute <= date.minute <= end_minute


def is_lunch_time(date: datetime) -> bool:
    return is_lunch_hour(date) and is_lunch_minute(date)


def get_next_working_day(date: datetime) -> datetime:
    while not is_working_day(date):
        date += timedelta(days=1)
    return date


def get_next_lunch_time(date: datetime) -> datetime:
    while not is_lunch_time(date):
        date += timedelta(minutes=1)
    return date
