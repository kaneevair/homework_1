import pytest
from src.circle import Circle
from src.rectangle import Rectangle


@pytest.mark.parametrize('radius, expected_perimeter, expected_area',
                         [
                            (2, 12.56, 12.56),
                            (5, 31.4, 78.5),
                            (10, 62.8, 314),
                         ]
                         )
def test_circle_creation_positive(radius, expected_perimeter, expected_area):
    circle = Circle(radius)
    assert circle.name == 'Circle', 'Expected name is Circle'
    assert circle.get_perimeter() == expected_perimeter, 'Expected correct perimeter'
    assert circle.get_area() == expected_area, 'Expected correct area'


@pytest.mark.parametrize('radius',
                         [
                             0,
                             -2
                         ],
                         )
def test_circle_creation_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)


def test_areas_sum():
    expected_sum = 86.5
    rectangle_1 = Rectangle(2, 4)
    circle_2 = Circle(5)
    assert rectangle_1.add_area(circle_2) == expected_sum, f'Expected sum is {expected_sum}'


@pytest.mark.parametrize('some_other_class', [10, 10.1, 'something'], ids=['integer', 'float', 'str'])
def test_two_circle_areas_sum_negative(some_other_class):
    circle_1 = Circle(10)
    with pytest.raises(ValueError):
        circle_1.add_area(some_other_class)
