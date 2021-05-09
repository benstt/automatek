from board import Board
from life_like_automata import LifeLike

#DEAD_CELL = 0
#ALIVE_CELL = 1

class GameOfLife(LifeLike):
    """
    Conway's Game of Life automata.
    Each new state follows this rules:
        * Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        * Any live cell with two or three live neighbours lives on to the next generation.
        * Any live cell with more than three live neighbours dies, as if by overpopulation.
        * Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    """
    def __init__(self, board):
        super().__init__(board)

    def set_next_state(self):
        """
        Calculates and returns a new board with updated values. 

        Returns
        -------
        new_board : Board
        """
        if not self.board.is_empty():
            new_board = Board(width = self.board.width, height = self.board.height)
            for row in range(self.board.height):
                for column in range(self.board.width):
                    # get the cell we're working on
                    cell = self.board.values[row][column]
                    # count its neighbors
                    neighbors = self.count_neighbors(row, column)
                    # check whether the cell is alive or not and update it
                    if cell == self.ALIVE_CELL:
                        if neighbors == 0 or neighbors == 1:
                            cell = self.DEAD_CELL
                        if neighbors == 2 or neighbors == 3:
                            cell = self.ALIVE_CELL
                        if neighbors > 3:
                            cell = self.DEAD_CELL
                    else:
                        if neighbors == 3:
                            cell = self.ALIVE_CELL

                    # update pos of the new board
                    new_board.change_pos_value(row, column, cell)

        return new_board