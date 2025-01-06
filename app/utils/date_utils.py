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
        date = datetime.now()  # Use the current date if no date is provided

    # Assume you have a logic to calculate the lunar date from the solar date
    # This is just an example, you need to replace it with your actual logic.
    lunar_date = date  # Replace with actual logic
    lunar_day = lunar_date.day
    lunar_month = lunar_date.month
    lunar_year = lunar_date.year
    return f"{lunar_day}/{lunar_month}/{lunar_year}"

# Example usage of the get_lunar_date function
if __name__ == "__main__":
    print("Lunar date for today:", get_lunar_date())
