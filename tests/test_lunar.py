import pytest
from app.utils.lunar.converter import LunarConverter

def test_solar_to_lunar():
    converter = LunarConverter()
    lunar_date = converter.solar_to_lunar(1, 1, 2024)
    assert lunar_date == (21, 11, 2023)

def test_lunar_festivals():
    from app.utils.lunar.festivals import LUNAR_FESTIVALS
    assert LUNAR_FESTIVALS.get((1, 1)) == "Tết Nguyên Đán"