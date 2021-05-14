import math

class Vector2:
    """
    Class that represents a 2D mathematical vector.
    """
    __slots__ = ['_x', '_y']
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def rotate_right(self):
        return Vector2(self.y, -self.x)

    def rotate_left(self):
        return Vector2(-self.y, self.x)

    def distance(self, other):
        return other - self

    def normalize(self):
        pow_x = pow(self.x, 2)
        pow_y = pow(self.y, 2)
        return int(math.sqrt(pow_x + pow_y))

    def to_unit_vector(self):
        return self // self.normalize()

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def copy(self):
        return Vector2(self.x, self.y)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __floordiv__(self, other):
        return Vector2(self.x // other, self.y // other)

    def __eq__(self, other):
        return self.x is other.x and self.y is other.y

    def __repr__(self):
        return repr((self._x, self._y))