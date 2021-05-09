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
    """
    @dataclass
    class _Ant:
        pos: 'Vector2' = None

    __slots__ = ['_ant_pos', '_ant_facing_dir']

    def __init__(self, board, ant_x, ant_y):
        super().__init__(board)
        self._ant_pos = Vector2(ant_x, ant_y)
        # set ant to face up.
        # x is a row, so it's orders are inverted.
        self._ant_facing_dir = Vector2(self.ant_pos.x - 1, self.ant_pos.y)

    def determine_next_ant_position(self):
        cur_x = self.ant_pos.x
        cur_y = self.ant_pos.y
        ant_facing_pos = self.ant_facing_dir
        next_desired_position = ant_facing_pos.rotate_right() if self.board.value_at(cur_x, cur_y) == 1 else ant_facing_pos.rotate_left()

        #return next_desired_position
        return ant_facing_pos.rotate_right()

    def move_ant(self):
        self.ant_pos = self.determine_next_ant_position()
        return self.ant_pos

    def set_next_state(self):
        if not self.board.is_empty():
            pass

    @property
    def ant_pos(self):
        return self._ant_pos

    @ant_pos.setter
    def ant_pos(self, new):
        self._ant_pos = new

    @property
    def ant_facing_dir(self):
        return self._ant_facing_dir

    @ant_facing_dir.setter
    def ant_facing_dir(self, new):
        self._ant_facing_dir = new

    @property
    def ant_next_pos(self):
        return LangtonAnt._Ant.next_pos
        

#ant_pos = Vector2(1, 1)
#facing_pos = Vector2(0, 1)
#desired_pos = ant_pos.distance(facing_pos).rotate_right()
#print(desired_pos)
#ant = LangtonAnt._Ant(ant_pos, facing_pos) # creo una ant
#d = ant.determine_next_position(ant.pos.distance(facing_pos)) # determino donde tendria que moverse. tendria que dar (0, 1)
#print(d)