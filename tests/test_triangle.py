import pytest
from src.triangle import Triangle

@pytest.mark.parametrize(
        ("side_a", "side_b", "side_c", "area"),
        [
            pytest.param(2, 3, 4, 2.9047, id=" целые "),
            pytest.param(15.5, 10.2, 6, 17.5708, id=" дробные ")
        ]
)
def test_triangle_area(side_a, side_b, side_c, area):
    t = Triangle(side_a, side_b, side_c)
    assert t.area == area

@pytest.mark.parametrize(
        ("side_a", "side_b", "side_c", "per"),
        [
            pytest.param(2, 3, 4, 9, id=" целые "),
            pytest.param(15.5, 10.2, 6, 31.7, id=" дробные ")
        ]
)
def test_triangle_perimeter(side_a, side_b, side_c, per):
    t = Triangle(side_a, side_b, side_c)
    assert t.perimeter == per

@pytest.mark.parametrize(
        ("side_a", "side_b", "side_c",),
        [
            pytest.param(0, 0, 0, id=" ноль "),
            pytest.param(-2, -3, -4, id=" отрицательные "),
            pytest.param(5, 9, 1, id=" несуществующий треугольник ")
        ]
)
def test_triangle_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)
