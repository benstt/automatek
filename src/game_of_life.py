from board import Board
from life_like_automata import LifeLike

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
        
        assert self.board.range == 1, "Illegal number of states possible."

    def determine_next_cell_state(self, cell, neighbors):
        if cell == self.ALIVE_CELL:
            if neighbors == 0 or neighbors == 1 or neighbors > 3:
                cell = self.DEAD_CELL
        else:
            if neighbors == 3:
                cell = self.ALIVE_CELL

        return cell