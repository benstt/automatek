from board import Board
from game_of_life import GameOfLife
from langtons_ant import LangtonAnt

TIME_BETWEEN_FRAMES = 0.03

#c = Board(source = '..\samples\gosper_glider_gun.txt')
#c.update()
b = Board(r'C:\Users\benja\dev\Game of Life\samples\gosper_glider_gun.txt')
#g = GameOfLife(b)
a = LangtonAnt(b, 5, 5)
#g.update(TIME_BETWEEN_FRAMES)
#b.render()

print(a.ant_pos)
print(a.ant_facing_dir)
print(a.move_ant())
