import home_work_14_1
from home_work_14_1 import rectangle_area

def test_rectangle_area_positive():
    assert rectangle_area(5, 10) == 50
    assert rectangle_area(3, 7) == 21
    assert rectangle_area(8, 2) == 16

def test_rectangle_area_zero_or_negative():
    with home_work_14_1.raises(ValueError):
        rectangle_area(-5, 10)
    with home_work_14_1.raises(ValueError):
        rectangle_area(0, 7)
    with home_work_14_1.raises(ValueError):
        rectangle_area(8, -2)