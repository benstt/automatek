from board import Board
from life_like_automata import LifeLike

class BrianBrain(LifeLike):
    DYING_CELL = 2

    def __init__(self, board):
        super().__init__(board)

        assert self.board.range == 2, "Illegal number of states possible."

    def set_next_state(self):
        if not self.board.is_empty():
            new_board = Board(width = self.board.width, height = self.board.height, n_range = 2)
            for row in range(self.board.height):
                for column in range(self.board.width):
                    # get the cell we're working on
                    cell = self.board.values[row][column]
                    # count its neighbors
                    neighbors = self.count_neighbors(row, column)
                    if cell == self.DEAD_CELL and neighbors == 2:
                        cell = self.ALIVE_CELL
                    elif cell == self.ALIVE_CELL:
                        cell = self.DYING_CELL
                    elif cell ==  self.DYING_CELL:
                        cell = self.DEAD_CELL

                    # update pos of the new board
                    new_board.change_pos_value(row, column, cell)

        return new_board