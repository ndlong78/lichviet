from datetime import datetime

def get_vietnamese_month_name(month):
    vietnamese_month_names = [
        "Tháng Một", "Tháng Hai", "Tháng Ba", "Tháng Tư", "Tháng Năm",
        "Tháng Sáu", "Tháng Bảy", "Tháng Tám", "Tháng Chín", "Tháng Mười",
        "Tháng Mười Một", "Tháng Mười Hai"
    ]
    return vietnamese_month_names[month - 1]

def get_lunar_date(date=None):
    if date is None:
        date = datetime.now()  # Sử dụng ngày hiện tại nếu không cung cấp ngày

    # Giả sử bạn có một logic để tính toán ngày âm lịch từ ngày dương lịch
    # Đây chỉ là ví dụ, bạn cần thay thế bằng logic thực tế của bạn.
    lunar_date = date  # Thay thế bằng logic thực tế
    lunar_day = lunar_date.day
    lunar_month = lunar_date.month
    lunar_year = lunar_date.year
    return f"{lunar_day}/{lunar_month}/{lunar_year}"

# Mẫu sử dụng hàm get_lunar_date
if __name__ == "__main__":
    print("Lunar date for today:", get_lunar_date())