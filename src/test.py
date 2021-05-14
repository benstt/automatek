import curses
from board import Board
from automatas import *

TIME_BETWEEN_FRAMES = 0.01

if __name__ == '__main__':
    pass
    b = Board(r'C:\Users\benja\dev\Game of Life\samples\gosper_glider_gun.txt', n_range=1)
    c = Board(width=60, height= 30)
    #g = GameOfLife(b)
    #g.update(0.03)
    #print(b.width, b.height)
    #test_daynight = Board(r'C:\Users\benja\dev\Game of Life\samples\crosshair.txt')
    #day_night = DayNight(test_daynight)
    #day_night.update(0.3)