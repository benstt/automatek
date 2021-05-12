from board import Board
from vec2 import Vector2
from cellular_automata import CellularAutomata
from dataclasses import dataclass

class LangtonAnt(CellularAutomata):
    """
    Langton's ant is a two-dimensional universal Turing machine and runs on a square lattice of black and white cells.
    We arbitrarily identify one square as the "ant". The ant can travel in any of the four cardinal directions at each step it takes.
    Each new state follows this rules:
        * At a white square, turn 90° clockwise, flip the color of the square, move forward one unit.
        * At a black square, turn 90° counter-clockwise, flip the color of the square, move forward one unit.

    Attributes
    ----------
    ant : Ant
        The ant that will move through the board.
    """

    # class that will help to work with the ant
    @dataclass
    class _Ant:
        pos: 'Vector2' = None
        facing_dir: 'Vector2' = None

    __slots__ = ['_ant']

    def __init__(self, board):
        super().__init__(board)

        # set position of the ant
        pos = Vector2(self.board.height // 2, self.board.width // 2)
        # set ant to face a direction based on board value under it
        facing_dir = Vector2(0, 1) # right -- orders are inverted as x means rows and y means columns

        # set ant
        self._ant = LangtonAnt._Ant(pos, facing_dir)

    def determine_next_ant_direction(self):
        """
        Determines the next ant direction based on the current cell it's standing on.
        Turns right if it's standing on a square, and left if not.

        Returns
        -------
        ant_facing_pos : Vector2
            A unit vector.
        """
        cur_x = self.ant.pos.x
        cur_y = self.ant.pos.y
        # determine in which direction to move
        move_dir = self.ant.facing_dir

        # get desired position based on cell under ant
        if self.board.value_at(cur_x, cur_y) == self.ALIVE_CELL:
            # rotate right
            ant_facing_pos = move_dir.rotate_right()
        else:
            # rotate left
            ant_facing_pos = move_dir.rotate_left()

        return ant_facing_pos

    def move_ant(self, m_dir):
        """
        Moves the ant one unit towards the facing direction.

        Parameters
        ----------
        m_dir : Vector2
            The direction (a unit vector) desired to move the ant
        """
        # update position
        self.ant.pos += m_dir

        return self.ant.pos

    def set_next_state(self):
        """
        Set next state of the board.
        Moves the ant depending on the cell it's standing on and flips the color of the cell.
        """
        if not self.board.is_empty():
            pos = self.ant.pos
            self.ant.facing_dir = self.determine_next_ant_direction() # calculate which way to go
            self.ant.pos = self.move_ant(self.ant.facing_dir) # update position
            self.board.values[pos.x][pos.y] = int(not self.board.values[pos.x][pos.y]) # flip cell the ant's standing on

        return self.board

    @property
    def ant(self):
        return self._ant