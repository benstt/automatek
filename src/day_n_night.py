from board import Board
from life_like_automata import LifeLike

class DayNight(LifeLike):
    """
    Day and Night is a cellular automaton rule in the same family as Game of Life.
    It is defined by rule notation B3678/S34678, meaning that:
    * a dead cell becomes live (is born) if it has 3, 6, 7, or 8 live neighbors, 
    * and a live cell remains alive (survives) if it has 3, 4, 6, 7, or 8 live neighbors.
    """
    def __init__(self, board):
        super().__init__(board)

    def set_next_state(self):
        if not self.board.is_empty():
            new_board = Board(width = self.board.width, height = self.board.height)
            for row in range(self.board.height):
                for column in range(self.board.width):
                    # get the cell we're working on
                    cell = self.board.values[row][column]
                    # count its neighbors
                    neighbors = self.count_neighbors(row, column)
                    neighbors_to_revive = {3, 6, 7, 8}
                    neighbors_to_survive = {3, 4, 6, 7, 8}
                    # check whether the cell is alive or not and update it
                    if cell == self.DEAD_CELL and neighbors in neighbors_to_revive:
                        cell = self.ALIVE_CELL
                    elif cell == self.ALIVE_CELL and neighbors in neighbors_to_survive:
                        pass
                    else:
                        cell = self.DEAD_CELL

                    # update pos of the new board
                    new_board.change_pos_value(row, column, cell)

        return new_board