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

        assert self.board.range == 1, "Illegal number of states possible."

    def determine_next_cell_state(self, cell, neighbors):
        """
        Process the logic necesarry to update a given cell of the automata.

        Returns
        -------
        cell : int
            A number that represents the state of a cell, either a 0 or a 1.
        """
        neighbors_to_revive = {3, 6, 7, 8}
        neighbors_to_survive = {3, 4, 6, 7, 8}

        # revive a cell if it has the right amount of neighbors
        if cell == self.DEAD_CELL and neighbors in neighbors_to_revive:
            cell = self.ALIVE_CELL
        elif cell == self.ALIVE_CELL and neighbors in neighbors_to_survive:
            pass
        else:
            cell = self.DEAD_CELL

        return cell