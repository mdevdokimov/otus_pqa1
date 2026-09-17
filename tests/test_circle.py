import sys
import os
import pytest

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
src_path = os.path.join(parent_dir, 'scr')
sys.path.append(src_path)
from circle import Circle


@pytest.mark.parametrize(
        ("rad", "area"),
        [
            pytest.param(2, 12.5664, id=" целые "),
            pytest.param(15.5, 754.7676, id=" дробные ")
        ]
)
def test_circle_area(rad, area):
    c = Circle(rad)
    assert c.area == area

@pytest.mark.parametrize(
        ("rad", "per"),
        [
            pytest.param(2, 12.5664, id=" целые "),
            pytest.param(15.5, 97.3894, id=" дробные ")
        ]
)
def test_circle_perimeter(rad, per):
    c = Circle(rad)
    assert c.perimeter == per

@pytest.mark.parametrize(
        ("rad"),
        [
            pytest.param(0, id=" ноль "),
            pytest.param(-1, id=" отрицательные ")
        ]
)
def test_circle_negative(rad):
    with pytest.raises(ValueError):
        Circle(rad)
