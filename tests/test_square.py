import pytest
from src.square import Square
from src.triangle import Triangle


@pytest.mark.parametrize('a_side, expected_perimeter, expected_area',
                         [
                            (2, 8, 4),
                            (5, 20, 25),
                            (10, 40, 100),
                         ]
                         )
def test_square_creation_positive(a_side, expected_perimeter, expected_area):
    square = Square(a_side)
    assert square.name == 'Square', 'Expected name is Square'
    assert square.get_perimeter() == expected_perimeter, 'Expected correct perimeter'
    assert square.get_area() == expected_area, 'Expected correct area'


@pytest.mark.parametrize('a_side',
                         [
                             0,
                             -2
                         ],
                         )
def test_square_creation_negative(a_side):
    with pytest.raises(ValueError):
        Square(a_side)


def test_areas_sum():
    expected_sum = 5.98
    square_1 = Square(2)
    triangle_2 = Triangle(2, 2, 3)
    assert square_1.add_area(triangle_2) == expected_sum, f'Expected sum is {expected_sum}'


@pytest.mark.parametrize('some_other_class', [10, 10.1, 'something'], ids=['integer', 'float', 'str'])
def test_two_square_areas_sum_negative(some_other_class):
    square_1 = Square(2)
    with pytest.raises(ValueError):
        square_1.add_area(some_other_class)
