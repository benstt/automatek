import curses
from board import Board
from automatas import *

menu = ['Choose automata', 'Play random automata', 'Make your own automata!', 'Exit']
automatas = ["Conway's Game of Life", "Langton's Ant", "Brian's Brain", "Day 'n' Night", 'Back']
boards_display = ['Blank', 'Beacon', 'Blinker', 'Crosshair', 'Glider', 'Gosper Glider Gun', 'Little Ship', 'Ship', 'Star', 'Toad', 'Back']
boards = ['', 'beacon.txt', 'blinker.txt', 'crosshair.txt', 'glider.txt', 'gosper_glider_gun.txt', 'little_ship.txt', 'ship.txt', 'star.txt', 'toad.txt']

TIME_BETWEEN_FRAMES = 0.03

def load_board(idx, automata_idx, rand = True):
    ranges = {
        0: 1,
        1: 1,
        2: 2,
        3: 1
    }
    assert idx > 1, 'Board index must be greater than zero.'
    return Board('..\samples\\' + boards[idx], n_range = ranges[automata_idx], random = rand)

def create_automata(idx, board):
    """
    Instantiates an automata based on the given index.

    Returns
    -------
    n_automatas[idx] : CellularAutomata
    """
    n_automatas = {
        0: GameOfLife,
        1: LangtonAnt,
        2: BrianBrain,
        3: DayNight
    }

    return n_automatas[idx](board)

def print_menu(stdscr, selected_row_idx, list):
    """
    Prints a menu to the terminal.
    """
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(list):
        x = w // 2 - len(row) // 2
        y = h // 2 - (len(list) // 2) + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()

def print_board(stdscr, board, height, width):
    """
    Renders a board to the terminal.
    Prints every 1 as a symbol and every 0 as a blank space.
    """
    stdscr.clear()

    # make sure there are elements in the board
    assert not board.is_empty(), 'No elements'
    # where the lines will be appended to
    lines = []

    # symbols to represent numbers
    display_as = {
        0: ' ',           # dead cell
        1: u"\u2588",     # alive cell
        2: u"\u2593"      # dying cell
    }

    for row in range(board._height):
        # create a new line
        line = ''
        for column in range(board._width):
            # add a char to the line depending on the cell
            val = board._values[row][column]
            line += (display_as[val]) * 2
        lines.append(line)
    # jump row and display lines
    # adds spaces at the beginning based on given width
    stdscr.addstr(height, width, ('\n').join(line for line in lines).replace('\n', '\n' + (' ' * width)))

    stdscr.refresh()

if __name__ == '__main__':
    def main(stdscr):
        curses.curs_set(0) # set cursor to not display
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)
        
        current_row_idx = 0
        current_menu = menu
        current_state = 's_menu'
        current_menu_state = 's_menu_menu'

        exit = False

        print_menu(stdscr, current_row_idx, current_menu)

        while not exit:
            # general menu state
            if current_state == 's_menu':
                key = stdscr.getch()
                stdscr.clear()

                if key == curses.KEY_UP and current_row_idx > 0:
                    # go up a row
                    current_row_idx -= 1
                elif key == curses.KEY_DOWN and current_row_idx < len(current_menu) - 1:
                    # go down a row
                    current_row_idx += 1
                elif key == curses.KEY_ENTER or key in [10, 13]:
                    # go to next menu or change state
                    if current_menu_state == 's_menu_menu':
                        # main menu

                        # if not selecting 'exit' option
                        if current_row_idx == 0:
                            current_menu = automatas                           # change menu to display
                            current_menu_state = 's_menu_choose_automata'      # change state

                        # selecting 'exit' option
                        elif current_row_idx == len(current_menu) - 1:
                            exit = True                                        # exit loop
                    elif current_menu_state == 's_menu_choose_automata':
                        # choose automata menu

                        # if not selecting 'back' option
                        if current_row_idx != len(current_menu) - 1:
                            current_menu = boards_display                      # change menu to display
                            selected_automata_idx = current_row_idx            # remember the automata selected
                            current_row_idx = 0                                # set cursor to first row
                            current_menu_state = 's_menu_displaying_boards'    # change state

                        # selecting 'back' option
                        elif current_row_idx == len(current_menu) - 1:
                            current_menu = menu                                # change menu to display
                            current_row_idx = 0                                # set cursor to first row
                            current_menu_state = 's_menu_menu'                 # change state

                    elif current_menu_state == 's_menu_displaying_boards':
                        # displaying boards menu

                        # 'blank' board
                        if current_row_idx == 0:
                            h, w = stdscr.getmaxyx()
                            board = Board(height = h // 2, width = w // 3, random = False)
                            current_state = 's_display_automata'

                        # if not selecting 'back' option
                        elif current_row_idx != 0 and current_row_idx != len(current_menu) - 1:
                            board = load_board(current_row_idx, selected_automata_idx) # load the board selected
                            current_state = 's_display_automata' # change state

                        # selecting 'back' option
                        elif current_row_idx == len(current_menu) - 1:
                            current_menu = automatas                           # change menu to display
                            current_row_idx = 0                                # set cursor to first row
                            current_menu_state = 's_menu_choose_automata'      # change state

                print_menu(stdscr, current_row_idx, current_menu)
                stdscr.refresh()

            # automata playing state
            elif current_state == 's_display_automata':
                # create instance of automata
                automata = create_automata(selected_automata_idx, board) 
                h, w = stdscr.getmaxyx()
                # get center of the screen
                y = h // 2 - (board.height // 2)
                x = w // 2 - (board.width)
                while True:
                    print_board(stdscr, board, y, x) # print the board
                    board = automata.update(TIME_BETWEEN_FRAMES) # update the board

    curses.wrapper(main)