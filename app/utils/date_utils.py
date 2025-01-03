# app/utils/date_utils.py
def get_vietnamese_month_name(month):
    vietnamese_month_names = [
        "Tháng Một", "Tháng Hai", "Tháng Ba", "Tháng Tư", "Tháng Năm",
        "Tháng Sáu", "Tháng Bảy", "Tháng Tám", "Tháng Chín", "Tháng Mười",
        "Tháng Mười Một", "Tháng Mười Hai"
    ]
    return vietnamese_month_names[month - 1]

def get_lunar_date(date):
    # Logic to calculate the lunar date from the given date
    # This is a placeholder function
    return "Lunar Date Placeholder"