from random import *

class Board:
    __slots__ = ['_values', '_width', '_height', '_len']

    def __init__(self, width = 0, height = 0, random = False):
        self._values = []
        self._len = 0
        self._width = width
        self._height = height
        if width > 0 and height > 0:
            if not random:
                self.fill_values(0)
            else:
                self.fill_values_randomly()

        #self._width = width
        #self._height = height

    def append(self, value):
        self._values.append(value)

    def fill_values(self, value = 0):
        """ fills the board with 0's """
        if self.is_empty():
            for row in range(self._height):
                # add a new row
                self.append([])
                for column in range(self._width):
                    # append value to the row
                    self._values[row].append(value)
                    self._len += 1
        else:
            for row in range(self._height):
                for column in range(self._width):
                    self._values[row][column] = value

        # make sure the board was filled
        assert self._len > 0, 'No elements were added'

        return self._values

    def fill_values_randomly(self):
        """ fills the board randomly with either a 0 or a 1 """
        for row in range(self._height):
            # add a new row
            self.append([])
            for column in range(self._width):
                # assign random values to every number and append that to the row
                rand_number = random()
                rand_number = 1 if rand_number >= 0.97 else 0
                self._values[row].append(rand_number)
                self._len += 1

        # make sure the board was filled
        #assert self._len > 0, 'No elements were added'        

        return self._values

    def render(self):
        """ renders the board to the terminal """
        assert not self.is_empty(), 'No elements'

        print('-' * (self._width + 2)) # top corners
        
        for row in range(self._height):
            for column in range(self._width):
                if column == 0: # left corners
                    print('|', end = '')

                # print a hash symbol if a cell is alive
                print('#' if self._values[row][column] == 1 else ' ', end = '')

                if column == self._width - 1: # right corners
                    print('|', end = '')
            print('\n', end = '')

        print('-' * (self._width + 2)) # bottom corners

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def is_empty(self):
        return self._width == 0 or self._height == 0

    def clear(self):
        self._values.clear()

    def __len__(self):
        return self._len

    def __repr__(self):
        return ('[' + ', '.join(repr(x) for x in self._values) + ']')


def dead_state(width, height):
    """ fills a width * height board with 0's """
    return State(width, height)

def random_state(width, height):
    """ sets a random state to a board """
    state = dead_state(width, height)
    for row in range(width):
        for column in range(height):
            # assign random values to every number
            rand_number = random()
            rand_number = 1 if rand_number >= 0.99 else 0
            state[row][column] = rand_number

    return state

def render(state):
    """ renders a state to the terminal """
    _width = state.width
    _height = state.height
    print('-'*_width*5)
    for row in range(_width):
        for column in range(_height):
            print('#' if state[row][column] == 1 else ' ')
        #print('\n')
        
#s = dead_state(5, 5)
#s2 = random_state(5, 5)
#render(s2)
#a = Board(150, 65, True)
#print(a)
#a.render()
b = Board(2, 2)
b.fill_values(0)
print(b)
