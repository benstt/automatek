from abc import ABC, abstractmethod
from cellular_automata import CellularAutomata

class LifeLike(CellularAutomata, ABC):
    """
    General interpretation of a LifeLike automata.
    A cellular automaton is Life-like if it meets the following criteria:
        * The array of cells of the automaton has two dimensions.
        * Each cell of the automaton has two states (ALIVE or DEAD).
        * The neighborhood of each cell consists of the eight adjacent cells to the one under consideration.
        * In each time step of the automaton, the new state of a cell can be expressed as a function of
          the number of adjacent cells that are in the alive state and of the cell's own state.
    """
    def __init__(self, board):
        super().__init__(board)

    @abstractmethod
    def set_next_state(self):
        """
        Calculates and returns the new state of the automata. 
        """
        pass

    def count_neighbors(self, row, column):
        """
        Counts the amount (up to 8) of neighbors of a given cell.

        Parameters
        ----------
        row : int
        column : int

        Returns
        -------
        n_live_neighbors : int
        """
        # count variable
        n_live_neighbors = 0

        # iterate around the cell's neighbors
        for x in range((row - 1), (row + 1) + 1):
            # skip if went off the edge of the board
            if x < 0 or x >= self.board.height: continue

            for y in range((column - 1), (column + 1) + 1):
                # skip if went off the edge of the board
                if y < 0 or y >= self.board.width: continue
                # make sure we don't count the cell as a neighbor of itself
                if x == row and y == column: continue

                if self.board.values[x][y] == self.ALIVE_CELL:
                    n_live_neighbors += 1

        return n_live_neighbors