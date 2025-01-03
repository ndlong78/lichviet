def solar_to_lunar(solar_year, solar_month, solar_day):
    """
    Convert solar date to lunar date
    Returns: (lunar_day, lunar_month, lunar_year)
    """
    # Bảng tính âm lịch cho năm 2024-2025
    LUNAR_MONTHS = {
        2024: [
            (1, 1, 2024, "Tết Nguyên Đán"),  # Tết 2024
            (2, 1, 2024, None),
            # ... Thêm các ngày khác
        ],
        2025: [
            (1, 1, 2025, "Tết Nguyên Đán"),  # Tết 2025
            (2, 1, 2025, None),
            # ... Thêm các ngày khác
        ]
    }
    
    # Tạm thời trả về ngày dương lịch - 1 làm ví dụ
    # Trong thực tế cần có bảng tra cứu hoặc thuật toán chuyển đổi chính xác
    return (solar_day - 1, solar_month, solar_year)

def get_lunar_festivals(lunar_day, lunar_month):
    """Get lunar festival for given lunar date"""
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