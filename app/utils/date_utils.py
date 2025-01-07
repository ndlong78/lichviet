from datetime import datetime
from .lunar_solar_converter import converter

def get_vietnamese_month_name(month):
    vietnamese_month_names = [
        "Tháng Một", "Tháng Hai", "Tháng Ba", "Tháng Tư", "Tháng Năm",
        "Tháng Sáu", "Tháng Bảy", "Tháng Tám", "Tháng Chín", "Tháng Mười",
        "Tháng Mười Một", "Tháng Mười Hai"
    ]
    return vietnamese_month_names[month - 1]

def get_lunar_date(date=None):
    if date is None:
        date = datetime.now()
        
    lunar_day, lunar_month, lunar_year = converter.solar_to_lunar(
        date.day, date.month, date.year
    )
    festival = converter.get_lunar_festival(lunar_day, lunar_month)
    
    result = f"{lunar_day}/{lunar_month}"
    if festival:
        result += f" - {festival}"
    return result