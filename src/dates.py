from datetime import datetime


def calculate_month_difference(date_start: datetime, date_end: datetime) -> int:
    year_diff = date_end.year - date_start.year
    month_diff = date_end.month - date_start.month

    total_months = year_diff * 12 + month_diff

    return total_months


def get_month_start(date: datetime) -> datetime:
    return date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
