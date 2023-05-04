import pytest
from src.triangle import Triangle


@pytest.mark.parametrize('side_a, side_b, side_c, expected_perimeter, expected_area',
                         [
                             (10, 10, 10, 30, 43.3),
                             (2, 2, 3, 7, 1.98),
                             (5, 6, 8, 19, 14.98),
                         ]
                         )
def test_triangle_creation_positive(side_a, side_b, side_c, expected_perimeter, expected_area):
    triangle = Triangle(side_a, side_b, side_c)
    assert triangle.name == 'Triangle', 'Expected name is Triangle'
    assert triangle.get_perimeter() == expected_perimeter, 'Expected correct perimeter'
    assert triangle.get_area() == expected_area, 'Expected correct area'


@pytest.mark.parametrize('side_a, side_b, side_c',
                         [
                             (0, 10, 10),
                             (-2, 2, 3),
                             (10, 10, 30),
                         ],
                         ids=[
                             'one side is zero',
                             'one side is negative',
                             'can not create rectangle with these sides'
                         ])
def test_triangle_creation_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


def test_two_triangle_areas_sum():
    expected_sum = 45.28
    triangle_1 = Triangle(10, 10, 10)
    triangle_2 = Triangle(2, 2, 3)
    assert triangle_1.add_area(triangle_2) == expected_sum, f'Expected sum is {expected_sum}'


@pytest.mark.parametrize('some_other_class', [10, 10.1, 'something'], ids=['integer', 'float', 'str'])
def test_two_triangle_areas_sum_negative(some_other_class):
    triangle_1 = Triangle(10, 10, 10)
    with pytest.raises(ValueError):
        triangle_1.add_area(some_other_class)
