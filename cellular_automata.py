from abc import ABC, abstractmethod
from board import Board
import time
import os

class CellularAutomata(ABC):
    """
    General interpretation of a cellular automata. It depends on a board to display results.

    Attributes
    ----------
    board : Board
        A board. It includes a source matrix with values to display, or a 25 x 25 sized one with random values.
    """
    __slots__ = ['_board']

    # constants
    DEAD_CELL = 0
    ALIVE_CELL = 1
    
    def __init__(self, board):
        self._board = board

    @abstractmethod
    def set_next_state(self):
        """
        Calculates and returns the new state of the automata. 
        """
        pass

    def update(self, seconds):
        while True:
            self.board.render()
            self.board = self.set_next_state() # update board state
            time.sleep(seconds) # wait a bit to better visualize results
            os.system('cls') # clear the screen before rendering again

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, board):
        self._board = board

    @property
    def board_values(self):
        return self._board.values