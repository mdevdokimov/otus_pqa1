import pytest

from src.square import Square


@pytest.mark.parametrize(
        ("side", "area"),
        [
            pytest.param(2, 4, id=" целые "),
            pytest.param(15.5, 240.25, id=" дробные ")
        ]
)
def test_square_area(side, area):
    s = Square(side)
    assert s.area == area

@pytest.mark.parametrize(
        ("side", "per"),
        [
            pytest.param(2, 8, id=" целые "),
            pytest.param(15.5, 62, id=" дробные ")
        ]
)
def test_square_perimeter(side, per):
    s = Square(side)
    assert s.perimeter == per

@pytest.mark.parametrize(
        ("side"),
        [
            pytest.param(0, id=" ноль "),
            pytest.param(-1, id=" отрицательные ")
        ]
)
def test_square_negative(side):
    with pytest.raises(ValueError):
        Square(side)
