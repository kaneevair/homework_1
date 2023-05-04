from src.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, a_side: int):
        if not (a_side > 0):
            raise ValueError(f'Sides must be greater than 0. Got: {a_side}')

        super().__init__(a_side, a_side)
        self.name = 'Square'
