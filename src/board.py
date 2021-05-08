from random import *
import time
import os

# constants
DEAD_CELL = 0
ALIVE_CELL = 1
SPAWNING_PROBABILITY = 0.85
TIME_BETWEEN_FRAMES = 0.03

# TODO: add error checking
class Board:
    """
    Matrix that holds integer values interpreted as cells.

    Attributes
    ----------
    values : List
        A list of ints.

    width : int
        Number of columns.

    height : int
        Number of rows.

    len : int
        Total number of values.
    """
    # attributes
    __slots__ = ['_values', '_width', '_height', '_len']

    def __init__(self, width = 0, height = 0, random = True, source = ''):
        self._values = []
        self._len = 0
        if source != '':
            # load information from file
            file = self.load_from_file(source)
            self._width = len(file[0])
            self._height = len(file)
            self.fill_values_from_file(file)
        else:
            # create a board filled with values
            self._width = width
            self._height = height
            if width > 0 and height > 0:
                if random:
                    self.fill_values_randomly()
                else:
                    self.fill_values(0)

    def fill_values(self, value = 0):
        """
        Fills a board with the value given.

        Parameters
        ----------
        value : int, default: 0

        Returns
        -------
        values : List
        """
        if self.is_empty():
            # add rows and fill them with values
            for row in range(self._height):
                # add a new row
                self.append([])
                for column in range(self._width):
                    # append value to the row
                    self._values[row].append(value)
                    self._len += 1
        else:
            # change each value with the given
            for row in range(self._height):
                for column in range(self._width):
                    self._values[row][column] = value

        # make sure the board was filled
        assert not self.is_empty(), 'No elements were added'

        return self._values

    def fill_values_randomly(self):
        """
        Fills a board with either a 0 or a 1.

        Returns
        -------
        values : List
        """
        for row in range(self._height):
            # add a new row
            self.append([])
            for column in range(self._width):
                # assign random values to every number and append that to the row
                rand_number = random()
                rand_number = 1 if rand_number >= SPAWNING_PROBABILITY else 0
                self._values[row].append(rand_number)
                self._len += 1

        # make sure the board was filled
        assert not self.is_empty(), 'No elements were added'

        return self._values

    def fill_values_from_file(self, file):
        """
        Fills a board with the information given by a file.

        Parameters
        ----------
        file : string

        Returns
        -------
        values : List
        """
        for row in range(self._height):
            self.append([])
            for column in range(self._width):
                self._values[row].append(int(file[row][column])) # cast the value as an int
                self._len += 1

        # make sure the board was filled
        assert not self.is_empty(), 'No elements were added'

        return self._values

    def load_from_file(self, file):
        """
        Loads and returns a file.

        Parameters
        ----------
        file : string

        Returns
        -------
        f : File
        """
        f = open(file, 'r').read().split()
        return f

    def change_pos_value(self, row, column, value):
        """
        Changes the value of the given cell with another value.

        Parameters
        ----------
        cell : Cell
        value : int
        """
        self._values[row][column] = value

    def next_board_state(self):
        """
        Calculates and returns a new board with updated values. 

        Returns
        -------
        new_board : Board
        """
        if not self.is_empty():
            new_board = Board(self._width, self._height)
            for row in range(self._height):
                for column in range(self._width):
                    # get the cell we're working on
                    cell = self._values[row][column]
                    # count its neighbors
                    neighbors = self.count_neighbors(row, column)
                    # check whether the cell is alive or not and update it
                    if cell == ALIVE_CELL:
                        if neighbors == 0 or neighbors == 1:
                            cell = DEAD_CELL
                        if neighbors == 2 or neighbors == 3:
                            cell = ALIVE_CELL
                        if neighbors > 3:
                            cell = DEAD_CELL
                    else:
                        if neighbors == 3:
                            cell = ALIVE_CELL

                    # update pos of the new board
                    new_board.change_pos_value(row, column, cell)

        return new_board

    def count_neighbors(self, row, column):
        """
        Counts the amount of neighbors of a given cell.

        Parameters
        ----------
        cell : Cell

        Returns
        -------
        n_live_neighbors : int
        """
        # count variable
        n_live_neighbors = 0

        # iterate around the cells neighbors
        for x in range((row - 1), (row + 1) + 1):
            # skip if went off the edge of the board
            if x < 0 or x >= self._height: continue

            for y in range((column - 1), (column + 1) + 1):
                # skip if went off the edge of the board
                if y < 0 or y >= self._width: continue
                # make sure we don't count the cell as a neighbor of itself
                if x == row and y == column: continue

                if self._values[x][y] == ALIVE_CELL:
                    n_live_neighbors += 1

        return n_live_neighbors

    def render(self):
        """
        Renders a board to the terminal and adds borders.
        Prints every 1 as a symbol and every 0 as a blank space.
        """
        # make sure there are elements in the board
        assert not self.is_empty(), 'No elements'

        print('-' * (self._width + 2)) # top corners

        for row in range(self._height):
            for column in range(self._width):
                if column == 0: # left corners
                    print('|', end = '')

                # print a symbol if a cell is alive
                print(u"\u2588" if self._values[row][column] == ALIVE_CELL else ' ', end = '')

                if column == self._width - 1: # right corners
                    print('|', end = '')
            # jump row
            print('\n', end = '')

        print('-' * (self._width + 2)) # bottom corners

    def update(self):
        """
        Updates a board every given number of seconds.
        """
        while True:
            self.render()
            self = self.next_board_state() # update board state
            time.sleep(TIME_BETWEEN_FRAMES) # wait a bit to better visualize results
            os.system('cls') # clear the screen before rendering again

    def append(self, value):
        self._values.append(value)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def is_empty(self):
        return self._len == 0

    def clear(self):
        self._values.clear()

    def __len__(self):
        return self._len

    def __repr__(self):
        return ('[' + ', '.join(repr(x) for x in self._values) + ']')