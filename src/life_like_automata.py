from abc import ABC, abstractmethod
from board import Board
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
    def determine_next_cell_state(self, cell, neighbors):
        """
        Process the logic necesarry to update a given cell of the automata.
        
        Returns
        -------
        cell : int
            A number that represents the state of a cell.
        """
        pass

    def set_next_state(self):
        """
        Calculates and returns a new board with updated values. 

        Returns
        -------
        new_board : Board
        """
        if not self.board.is_empty():
            n_board_rows = self.board.height
            n_board_cols = self.board.width
            new_board = Board(width = n_board_cols, height = n_board_rows)

            for row in range(n_board_rows):
                for column in range(n_board_cols):
                    # get the cell we're working on and count its neighbors
                    cell = self.cell_at(row, column)
                    neighbors = self.count_neighbors(row, column)

                    # update the cell based on given rules
                    cell = self.determine_next_cell_state(cell, neighbors)

                    # update pos of the new board
                    new_board.change_pos_value(row, column, cell)

        return new_board

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