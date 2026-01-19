from datetime import datetime

def get_date_from_string(date:str) -> datetime:
    return datetime.strptime(date, "%Y-%m-%d").date()