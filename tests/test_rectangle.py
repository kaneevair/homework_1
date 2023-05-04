import pytest
from src.rectangle import Rectangle
from src.circle import Circle


@pytest.mark.parametrize('a_side, b_side, expected_perimeter, expected_area',
                         [
                            (2, 4, 12, 8),
                            (5, 10, 30, 50),
                            (10, 20, 60, 200),
                         ]
                         )
def test_rectangle_creation_positive(a_side, b_side, expected_perimeter, expected_area):
    rectangle = Rectangle(a_side, b_side)
    assert rectangle.name == 'Rectangle', 'Expected name is Rectangle'
    assert rectangle.get_perimeter() == expected_perimeter, 'Expected correct perimeter'
    assert rectangle.get_area() == expected_area, 'Expected correct area'


@pytest.mark.parametrize('a_side, b_side',
                         [
                             (0, 0),
                             (-5, 10),
                             (10, -20),

                         ],
                         )
def test_rectangle_creation_negative(a_side, b_side):
    with pytest.raises(ValueError):
        Rectangle(a_side, b_side)


def test_areas_sum():
    expected_sum = 58.24
    rectangle_1 = Rectangle(2, 4)
    circle_2 = Circle(4)
    assert rectangle_1.add_area(circle_2) == expected_sum, f'Expected sum is {expected_sum}'


@pytest.mark.parametrize('some_other_class', [10, 10.1, 'something'], ids=['integer', 'float', 'str'])
def test_two_rectangle_areas_sum_negative(some_other_class):
    rectangle_1 = Rectangle(2, 4)
    with pytest.raises(ValueError):
        rectangle_1.add_area(some_other_class)
