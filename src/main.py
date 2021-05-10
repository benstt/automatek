from board import Board
from game_of_life import GameOfLife
from langtons_ant import LangtonAnt

TIME_BETWEEN_FRAMES = 0.01

if __name__ == '__main__':
    b = Board(r'C:\Users\benja\dev\Game of Life\samples\gosper_glider_gun.txt')
    a = LangtonAnt(b, 2, 2)
    a.update(TIME_BETWEEN_FRAMES)
    