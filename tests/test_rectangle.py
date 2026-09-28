import pytest

from src.rectangle import Rectangle


@pytest.mark.parametrize(
        ("side_a", "side_b", "area"),
        [
            pytest.param(2, 3, 6, id=" целые "),
            pytest.param(15.5, 10.2, 158.1, id=" дробные ")
        ]
)
def test_rectangle_area(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.area == area

@pytest.mark.parametrize(
        ("side_a", "side_b", "per"),
        [
            pytest.param(2, 3, 10, id=" целые "),
            pytest.param(15.5, 10.2, 51.4, id=" дробные ")
        ]
)
def test_rectangle_perimeter(side_a, side_b, per):
    r = Rectangle(side_a, side_b)
    assert r.perimeter == per

@pytest.mark.parametrize(
        ("side_a", "side_b"),
        [
            pytest.param(0, 0, id=" ноль "),
            pytest.param(-1, -3, id=" отрицательные ")
        ]
)
def test_rectangle_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)
