# app/utils/lunar_solar_converter.py

import numpy as np
from datetime import datetime

class LunarSolarConverter:
    def __init__(self):
        self.PI = np.pi
        self.TIMEZONE = 7.0  # Múi giờ VN = UTC+7

    def jd_from_date(self, dd, mm, yy):
        """Chuyển ngày dương dd/mm/yyyy sang Julius Day"""
        a = int((14 - mm) / 12)
        y = yy + 4800 - a
        m = mm + 12 * a - 3
        jd = dd + int((153 * m + 2) / 5) + 365 * y + int(y / 4) - int(y / 100) + int(y / 400) - 32045
        if jd < 2299161:
            jd = dd + int((153 * m + 2) / 5) + 365 * y + int(y / 4) - 32083
        return jd

    def jd_to_date(self, jd):
        """Chuyển số ngày Julius Day sang ngày dương dd/mm/yyyy"""
        if jd > 2299160:  # After 5/10/1582, Gregorian calendar
            a = jd + 32044
            b = int((4 * a + 3) / 146097)
            c = a - int((b * 146097) / 4)
        else:
            b = 0
            c = jd + 32082
        
        d = int((4 * c + 3) / 1461)
        e = c - int((1461 * d) / 4)
        m = int((5 * e + 2) / 153)
        
        day = e - int((153 * m + 2) / 5) + 1
        month = m + 3 - 12 * int(m / 10)
        year = b * 100 + d - 4800 + int(m / 10)
        
        return (day, month, year)

    def new_moon(self, k):
        """Tính thời điểm Sóc (New Moon) của tháng âm lịch thứ k (k = 0 ứng với 1/1/1900)"""
        T = k / 1236.85  # Time in Julian centuries from 1900 January 0.5
        
        T2 = T * T
        T3 = T2 * T
        dr = self.PI / 180
        
        Jd1 = 2415020.75933 + 29.53058868 * k + 0.0001178 * T2 - 0.000000155 * T3
        Jd1 = Jd1 + 0.00033 * np.sin((166.56 + 132.87 * T - 0.009173 * T2) * dr)
        
        M = 359.2242 + 29.10535608 * k - 0.0000333 * T2 - 0.00000347 * T3
        M = M * dr
        Mpr = 306.0253 + 385.81691806 * k + 0.0107306 * T2 + 0.00001236 * T3
        Mpr = Mpr * dr
        F = 21.2964 + 390.67050646 * k - 0.0016528 * T2 - 0.00000239 * T3
        F = F * dr
        
        C1 = (0.1734 - 0.000393 * T) * np.sin(M)
        C1 = C1 + 0.0021 * np.sin(2 * M)
        C1 = C1 - 0.4068 * np.sin(Mpr)
        C1 = C1 + 0.0161 * np.sin(2 * Mpr)
        C1 = C1 - 0.0004 * np.sin(3 * Mpr)
        C1 = C1 + 0.0104 * np.sin(2 * F)
        C1 = C1 - 0.0051 * np.sin(M + Mpr)
        C1 = C1 - 0.0074 * np.sin(M - Mpr)
        C1 = C1 + 0.0004 * np.sin(2 * F + M)
        C1 = C1 - 0.0004 * np.sin(2 * F - M)
        C1 = C1 - 0.0006 * np.sin(2 * F + Mpr)
        C1 = C1 + 0.0010 * np.sin(2 * F - Mpr)
        C1 = C1 + 0.0005 * np.sin(M + 2 * Mpr)
        
        delta_T = 0.5 + self.TIMEZONE / 24.0 # Timezone correction
        JdNew = Jd1 + C1 - delta_T
        
        return JdNew

    def sun_longitude(self, jdn):
        """Tính kinh độ mặt trời"""
        T = (jdn - 2451545.0) / 36525
        T2 = T * T
        dr = self.PI / 180
        M = 357.52910 + 35999.05030 * T - 0.0001559 * T2 - 0.00000048 * T * T2
        M = M * dr
        
        L0 = 280.46645 + 36000.76983 * T + 0.0003032 * T2
        DL = (1.914600 - 0.004817 * T - 0.000014 * T2) * np.sin(M)
        DL = DL + (0.019993 - 0.000101 * T) * np.sin(2 * M) + 0.000290 * np.sin(3 * M)
        L = L0 + DL
        L = L * dr
        L = L - self.PI * 2 * (int(L / (self.PI * 2)))
        return L

    def get_sun_longitude_major_term(self, jdn):
        """Tính Major Term của kinh độ mặt trời"""
        T = (jdn - 2451545.0) / 36525
        T2 = T * T
        dr = self.PI / 180
        M = 357.52910 + 35999.05030 * T - 0.0001559 * T2 - 0.00000048 * T * T2
        M = M * dr
        L0 = 280.46645 + 36000.76983 * T + 0.0003032 * T2
        DL = (1.914600 - 0.004817 * T - 0.000014 * T2) * np.sin(M)
        L = L0 + DL
        L = L * dr
        return int(L / (self.PI * 12)) * self.PI * 12

    def get_lunar_month11(self, yy):
        """Tính tháng 11 âm lịch"""
        off = self.jd_from_date(31, 12, yy) - 2415021
        k = int(off / 29.530588853)
        nm = self.new_moon(k)
        sunLong = self.sun_longitude(nm)
        
        # Tháng 11 âm lịch phải nằm trong khoảng từ đông chí đến tiểu hàn
        while sunLong > 3 * self.PI / 2:
            nm = self.new_moon(k - 1)
            sunLong = self.sun_longitude(nm)
            k = k - 1
            
        return nm

    def get_leap_month_offset(self, a11, jd):
        """Xác định tháng nhuận"""
        k = int((jd - a11) / 29.530588853 + 0.5)
        last = 0
        i = 1  # Start with month following lunar month 11
        arc = self.sun_longitude(self.new_moon(k + i))
        while arc != last and i < 14:
            last = arc
            i += 1
            arc = self.sun_longitude(self.new_moon(k + i))
        return i - 1

    def solar_to_lunar(self, dd, mm, yy):
        """Chuyển đổi ngày dương lịch sang âm lịch"""
        dayNumber = self.jd_from_date(dd, mm, yy)
        k = int((dayNumber - 2415021.076998695) / 29.530588853)
        monthStart = self.new_moon(k)
        
        if monthStart > dayNumber:
            monthStart = self.new_moon(k - 1)
            
        a11 = self.get_lunar_month11(yy)
        b11 = self.get_sun_longitude_major_term(a11)
        lunarYear = yy
        if a11 >= monthStart:
            lunarYear = yy - 1
            a11 = self.get_lunar_month11(lunarYear)
            b11 = self.get_sun_longitude_major_term(a11)
            
        lunarDay = int(dayNumber - monthStart + 1)
        diff = int((monthStart - a11) / 29.530588853 + 0.5)
        lunarMonth = diff + 11
        if b11 > self.get_sun_longitude_major_term(monthStart):
            lunarMonth = diff + 12
            
        if lunarMonth > 12:
            lunarMonth = lunarMonth - 12
            
        if lunarMonth >= 11 and diff < 4:
            lunarYear -= 1
            
        leap = self.get_leap_month_offset(a11, monthStart)
        if leap != 0 and lunarMonth > leap:
            lunarMonth -= 1
            
        return lunarDay, lunarMonth, lunarYear, leap != 0 and lunarMonth == leap

    def lunar_to_solar(self, lunar_day, lunar_month, lunar_year, leap_month=False):
        """Chuyển đổi ngày âm lịch sang dương lịch"""
        if lunar_month < 11:
            a11 = self.get_lunar_month11(lunar_year - 1)
        else:
            a11 = self.get_lunar_month11(lunar_year)
            
        b11 = self.get_sun_longitude_major_term(a11)
        k = int((a11 - 2415021.076998695) / 29.530588853 + 0.5)
        off = lunar_month - 11
        if off < 0:
            off