from datetime import datetime
from .lunar_solar_converter import solar_to_lunar

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
    
    lunar = solar_to_lunar(date)
    
    # Định dạng ngày âm lịch với can chi
    can = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
    chi = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
    
    nam_am = can[lunar.year % 10] + " " + chi[lunar.year % 12]
    
    return {
        'day': lunar.day,
        'month': lunar.month,
        'year': lunar.year,
        'nam_am': nam_am,
        'text': f"{lunar.day}/{lunar.month} ({nam_am})"
    }

def get_lunar_festivals(lunar_day, lunar_month):
    festivals = {
        (1, 1): "Tết Nguyên Đán",
        (15, 1): "Tết Nguyên Tiêu",
        (10, 3): "Giỗ Tổ Hùng Vương",
        (15, 4): "Phật Đản",
        (5, 5): "Tết Đoan Ngọ",
        (15, 7): "Vu Lan",
        (15, 8): "Tết Trung Thu",
        (23, 12): "Ông Táo Chầu Trời"
    }
    return festivals.get((lunar_day, lunar_month))