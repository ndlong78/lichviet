# app/utils/lunar_solar_converter.py

import numpy as np
from datetime import datetime, date

class LunarSolarConverter:
    def __init__(self):
        self.PI = np.pi
        self.TIME_ZONE = 7.0  # Múi giờ Việt Nam (UTC+7)
        
    def jd_from_date(self, dd, mm, yy):
        """Chuyển ngày dương lịch sang số ngày Julius"""
        a = int((14 - mm) / 12)
        y = yy + 4800 - a
        m = mm + 12 * a - 3
        jd = dd + int((153 * m + 2) / 5) + 365 * y + int(y / 4) - int(y / 100) + int(y / 400) - 32045
        
        if jd < 2299161:
            jd = dd + int((153 * m + 2) / 5) + 365 * y + int(y / 4) - 32083
        return jd

    def get_new_moon_day(self, k, time_zone):
        """Tính ngày sóc"""
        T = k / 1236.85  # Time in Julian centuries from 1900 January 0.5
        T2 = T * T
        T3 = T2 * T
        dr = self.PI / 180
        
        Jd1 = 2415020.75933 + 29.53058868 * k + 0.0001178 * T2 - 0.000000155 * T3
        Jd1 = Jd1 + 0.00033 * np.sin((166.56 + 132.87 * T - 0.009173 * T2) * dr)
        
        return int(Jd1 + 0.5 + time_zone / 24)

    def get_sun_longitude(self, jdn):
        """Tính vị trí mặt trời"""
        T = (jdn - 2451545.0) / 36525
        T2 = T * T
        dr = self.PI / 180
        
        M = 357.52910 + 35999.05030 * T - 0.0001559 * T2
        L0 = 280.46645 + 36000.76983 * T + 0.0003032 * T2
        DL = (1.914600 - 0.004817 * T) * np.sin(dr * M) + (0.019993 - 0.000101 * T) * np.sin(dr * 2 * M)
        L = L0 + DL
        
        L = L * dr
        L = L - 2 * self.PI * int(L / (2 * self.PI))
        return L

    def solar_to_lunar(self, dd, mm, yy):
        """Chuyển đổi ngày dương lịch sang âm lịch
        Returns: (lunar_day, lunar_month, lunar_year, is_leap_month)
        """
        dayNumber = self.jd_from_date(dd, mm, yy)
        k = int((dayNumber - 2415021.076998695) / 29.530588853)
        monthStart = self.get_new_moon_day(k + 1, self.TIME_ZONE)
        
        if monthStart > dayNumber:
            monthStart = self.get_new_moon_day(k, self.TIME_ZONE)
            
        a11 = self.get_lunar_month11(yy)
        b11 = a11
        
        if a11 >= monthStart:
            lunarYear = yy
            a11 = self.get_lunar_month11(yy - 1)
        else:
            lunarYear = yy + 1
            b11 = self.get_lunar_month11(yy + 1)
            
        lunarDay = dayNumber - monthStart + 1
        diff = int((monthStart - a11) / 29.530588853)
        lunarMonth = diff + 11
        
        if b11 - a11 > 365:
            leapMonthDiff = self.get_leap_month_offset(a11)
            if diff >= leapMonthDiff:
                lunarMonth = diff + 10
                if diff == leapMonthDiff:
                    isLeapMonth = True
                    
        if lunarMonth > 12:
            lunarMonth = lunarMonth - 12
            
        if lunarMonth >= 11 and diff < 4:
            lunarYear -= 1
            
        return lunarDay, lunarMonth, lunarYear, False

    def get_lunar_month11(self, yy):
        """Tìm ngày bắt đầu tháng 11 âm lịch"""
        off = self.jd_from_date(31, 12, yy) - 2415021
        k = int(off / 29.530588853)
        nm = self.get_new_moon_day(k, self.TIME_ZONE)
        sunLong = self.get_sun_longitude(nm)
        
        if sunLong > 3 * self.PI / 2:
            nm = self.get_new_moon_day(k - 1, self.TIME_ZONE)
        return nm

    def get_leap_month_offset(self, jdn):
        """Xác định tháng nhuận"""
        k = int((jdn - 2415021.076998695) / 29.530588853 + 0.5)
        last = 0
        i = 1
        arc = self.get_sun_longitude(self.get_new_moon_day(k + i, self.TIME_ZONE))
        
        while True:
            last = arc
            i += 1
            arc = self.get_sun_longitude(self.get_new_moon_day(k + i, self.TIME_ZONE))
            if i > 14 or arc > last:
                break
        return i - 1

    @staticmethod
    def get_can_chi(year):
        """Lấy Can Chi của năm"""
        CAN = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
        CHI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
        return f"{CAN[year % 10]} {CHI[year % 12]}"

    @staticmethod
    def get_tiet_khi(d):
        """Lấy Tiết khí của ngày"""
        TIET_KHI = [
            "Xuân phân", "Thanh minh", "Cốc vũ", "Lập hạ", "Tiểu mãn", "Mang chủng",
            "Hạ chí", "Tiểu thử", "Đại thử", "Lập thu", "Xử thử", "Bạch lộ",
            "Thu phân", "Hàn lộ", "Sương giáng", "Lập đông", "Tiểu tuyết", "Đại tuyết",
            "Đông chí", "Tiểu hàn", "Đại hàn", "Lập xuân", "Vũ thủy", "Kinh trập"
        ]
        return TIET_KHI[int(d.strftime("%j")) * 24 // 365]

    def get_lunar_date_str(self, solar_date):
        """Lấy chuỗi biểu diễn ngày âm lịch"""
        if isinstance(solar_date, str):
            solar_date = datetime.strptime(solar_date, '%Y-%m-%d')
            
        lunar_day, lunar_month, lunar_year, is_leap = self.solar_to_lunar(
            solar_date.day, solar_date.month, solar_date.year
        )
        
        result = f"{lunar_day}/{lunar_month}"
        if is_leap:
            result += " (nhuận)"
        return result

    def get_lunar_info(self, solar_date):
        """Lấy thông tin đầy đủ của ngày âm lịch"""
        if isinstance(solar_date, str):
            solar_date = datetime.strptime(solar_date, '%Y-%m-%d')
            
        lunar_day, lunar_month, lunar_year, is_leap = self.solar_to_lunar(
            solar_date.day, solar_date.month, solar_date.year
        )
        
        return {
            'lunar_day': lunar_day,
            'lunar_month': lunar_month,
            'lunar_year': lunar_year,
            'is_leap_month': is_leap,
            'can_chi': self.get_can_chi(lunar_year),
            'tiet_khi': self.get_tiet_khi(solar_date)
        }

# Tạo instance để sử dụng
converter = LunarSolarConverter()

# Hàm tiện ích
def get_lunar_date(solar_date):
    """Wrapper để lấy ngày âm lịch dạng chuỗi"""
    return converter.get_lunar_date_str(solar_date)

def get_lunar_info(solar_date):
    """Wrapper để lấy thông tin âm lịch đầy đủ"""
    return converter.get_lunar_info(solar_date)