from datetime import datetime
from lunardate import LunarDate

def convert_to_lunar(solar_date):
    """
    Chuyển đổi ngày dương lịch sang âm lịch
    """
    lunar = LunarDate.fromSolarDate(
        solar_date.year,
        solar_date.month,
        solar_date.day
    )
    return lunar

def get_lunar_date(year, month, day):
    """
    Lấy thông tin ngày âm lịch
    """
    lunar = LunarDate.fromSolarDate(year, month, day)
    can_chi = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
    chi = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
    
    return {
        'year': lunar.year,
        'month': lunar.month,
        'day': lunar.day,
        'leap_month': lunar.isLeapMonth,
        'year_name': f"{can_chi[lunar.year % 10]} {chi[lunar.year % 12]}",
        'month_name': f"Tháng {lunar.month}{'(N)' if lunar.isLeapMonth else ''}",
        'day_name': f"Ngày {lunar.day}"
    }