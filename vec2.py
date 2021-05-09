class Vector2:
            __slots__ = ['_x', '_y']
            def __init__(self, x, y):
                self._x = x
                self._y = y

            def rotate_right(self):
                return Vector2(self._y, -self._x)

            def rotate_left(self):
                return Vector2(-self._y, self._x)

            def distance(self, other):
                return other - self

            @property
            def x(self):
                return self._x

            @property
            def y(self):
                return self._y

            def __add__(self, other):
                return Vector2(self.x + other.x, self.y + other.y)

            def __sub__(self, other):
                return Vector2(self.x - other.x, self.y - other.y)

            def __repr__(self):
                return repr((self._x, self._y))