from datetime import datetime


def is_working_day(date: datetime) -> bool:
    return date.weekday() < 5  # 0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일


def is_lunch_hour(date: datetime) -> bool:
    return date.hour == 11


def is_lunch_minute(date: datetime) -> bool:
    return date.minute == 10


def is_lunch_time(date: datetime) -> bool:
    return is_lunch_hour(date) and is_lunch_minute(date)
