import numpy as np
from datetime import datetime

class LunarConverter:
    def __init__(self):
        self.PI = np.pi
        self.TIME_ZONE = 7.0
        
    def solar_to_lunar(self, dd, mm, yy):
        """Chuyển đổi dương lịch sang âm lịch"""
        julian_day_number = self.jd_from_date(dd, mm, yy)
        return self.lunar_from_julian(julian_day_number)
        
    def lunar_to_solar(self, lunar_day, lunar_month, lunar_year, lunar_leap=False):
        """Chuyển đổi âm lịch sang dương lịch"""
        julian_day_number = self.lunar_to_julian(lunar_day, lunar_month, lunar_year, lunar_leap)
        return self.date_from_julian(julian_day_number)
        
    # Thêm các phương thức hỗ trợ khác