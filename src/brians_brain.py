from board import Board
from life_like_automata import LifeLike

class BrianBrain(LifeLike):
    """
    Brian's Brain is a cellular automaton devised by Brian Silverman, which is very similar to his Seeds rule.
    Each new state follows this rules:
        * A cell turns on if it was off but had exactly two neighbors that were on
        * All cells that were "on" go into the "dying" state
        * Cells that were in the dying state go into the off state.
    """
    DYING_CELL = 2

    def __init__(self, board):
        super().__init__(board)

        assert self.board.range == 2, "Illegal number of states possible."

    def determine_next_cell_state(self, cell, neighbors):
        """
        Process the logic necesarry to update a given cell of the automata.

        Returns
        -------
        cell : int
            A number that represents the state of a cell, a 0, a 1 or a 2.
        """
        # each cell will 'decay' one state at a time
        if cell == self.DEAD_CELL and neighbors == 2:
            cell = self.ALIVE_CELL
        elif cell == self.ALIVE_CELL:
            cell = self.DYING_CELL
        elif cell ==  self.DYING_CELL:
            cell = self.DEAD_CELL

        return cell