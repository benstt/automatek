from board import Board
from life_like_automata import LifeLike

class BrianBrain(LifeLike):
    DYING_CELL = 2

    def __init__(self, board):
        super().__init__(board)

        assert self.board.range == 2, "Illegal number of states possible."

    def determine_next_cell_state(self, cell, neighbors):
        if cell == self.DEAD_CELL and neighbors == 2:
            cell = self.ALIVE_CELL
        elif cell == self.ALIVE_CELL:
            cell = self.DYING_CELL
        elif cell ==  self.DYING_CELL:
            cell = self.DEAD_CELL

        return cell