from datetime import datetime
from .lunar_calendar import solar_to_lunar

def get_lunar_date(solar_date):
    """Convert solar date to lunar date string"""
    if isinstance(solar_date, str):
        solar_date = datetime.strptime(solar_date, '%Y-%m-%d')
    
    lunar_day, lunar_month, lunar_year = solar_to_lunar(
        solar_date.year,
        solar_date.month,
        solar_date.day
    )
    
    return f"{lunar_day}/{lunar_month}"

def get_vietnamese_month_name(month):
    """Get Vietnamese month name"""
    months = [
        "Tháng Một", "Tháng Hai", "Tháng Ba", "Tháng Tư", "Tháng Năm", "Tháng Sáu",
        "Tháng Bảy", "Tháng Tám", "Tháng Chín", "Tháng Mười", "Tháng Mười Một", "Tháng Mười Hai"
    ]
    return months[month - 1]

def get_vietnamese_weekday(date):
    """Get Vietnamese weekday name"""
    weekdays = ["Chủ Nhật", "Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy"]
    return weekdays[date.weekday()]