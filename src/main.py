import curses
from random import *
from board import Board
from automatas import *

menu = ['What is a Cellular Automaton?', 'Choose automata', 'Play random automata', 'Make your own automata!', 'Exit']
about = [
    'A cellular automaton is a discrete model of computation studied in automata theory.',
    'Cellular automata have found application in various areas, including',
    'physics, theoretical biology and microstructure modeling.',
    'Back'
]
automatas = ["Conway's Game of Life", "Langton's Ant", "Brian's Brain", "Day 'n' Night", 'Back']
boards_display = ['Blank', 'Beacon', 'Blinker', 'Crosshair', 'Glider', 'Gosper Glider Gun', 'Little Ship', 'Ship', 'Star', 'Toad', 'Back']
boards = ['', 'beacon.txt', 'blinker.txt', 'crosshair.txt', 'glider.txt', 'gosper_glider_gun.txt', 'little_ship.txt', 'ship.txt', 'star.txt', 'toad.txt']

name = [
        '       d8888          888                                    888             888      ',
        '      d88888          888                                    888             888      ',
        "     d88P888          888                                    888             888      ",
        "    d88P 888 888  888 888888  .d88b.  88888b.d88b.   8888b.  888888  .d88b.  888  888 ",
        '   d88P  888 888  888 888    d88""88b 888 "888 "88b     "88b 888    d8P  Y8b 888 .88P ',
        "  d88P   888 888  888 888    888  888 888  888  888 .d888888 888    88888888 888888K  ",
        ' d8888888888 Y88b 888 Y88b.  Y88..88P 888  888  888 888  888 Y88b.  Y8b.     888 "88b ',
        'd88P     888  "Y88888  "Y888  "Y88P"  888  888  888 "Y888888  "Y888  "Y8888  888  888 '
    ]

def load_board(idx, automata_idx, rand = True):
    ranges = {
        0: 1,
        1: 1,
        2: 2,
        3: 1
    }
    assert idx >= 1, 'Board index must be greater than zero.'
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

def print_title(stdscr, name, height, width):
    # stdscr.addstr(height + 0, width, '       d8888          888                                    888             888      ')
    # stdscr.addstr(height + 1, width, '      d88888          888                                    888             888      ')
    # stdscr.addstr(height + 2, width, "     d88P888          888                                    888             888      ")
    # stdscr.addstr(height + 3, width, "    d88P 888 888  888 888888  .d88b.  88888b.d88b.   8888b.  888888  .d88b.  888  888 ")
    # stdscr.addstr(height + 4, width, '   d88P  888 888  888 888    d88""88b 888 "888 "88b     "88b 888    d8P  Y8b 888 .88P ')
    # stdscr.addstr(height + 5, width, "  d88P   888 888  888 888    888  888 888  888  888 .d888888 888    88888888 888888K  ")
    # stdscr.addstr(height + 6, width, ' d8888888888 Y88b 888 Y88b.  Y88..88P 888  888  888 888  888 Y88b.  Y8b.     888 "88b ')
    # stdscr.addstr(height + 7, width, 'd88P     888  "Y88888  "Y888  "Y88P"  888  888  888 "Y888888  "Y888  "Y8888  888  888 ')

    for idx, row in enumerate(name):
        stdscr.addstr(height + idx, width, row)

def print_menu(stdscr, selected_row_idx, list):
    """
    Prints a menu to the terminal.
    """
    #stdscr.clear()

    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(list):
        x = w // 2 - len(row) // 2
        if list is menu:
            y = (h - (h // 4)) - (len(list) // 2) + idx
        else:
            y = h // 2 - (len(list) // 2) + idx

        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

    #stdscr.refresh()

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

def main(stdscr):
    curses.curs_set(0) # set cursor to not display
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_CYAN)
    
    TIME_BETWEEN_FRAMES = 0.03
    MINIMUM_SCREEN_HEIGHT = 28
    MINIMUN_SCREEN_WIDTH = 108
    MAXIMUM_SCREEN_HEIGHT = 81
    MAXIMUM_SCREEN_WIDTH = 360
    
    current_row_idx = 0
    current_menu = menu
    current_state = 's_menu'
    current_menu_state = 's_menu_menu'

    screen_height, screen_width = stdscr.getmaxyx()

    # don't go over this values
    if screen_height < MINIMUM_SCREEN_HEIGHT and screen_width < MINIMUN_SCREEN_WIDTH:
        screen_height = MINIMUM_SCREEN_HEIGHT
        screen_width = MINIMUN_SCREEN_WIDTH
    elif screen_height > MAXIMUM_SCREEN_HEIGHT and screen_width > MAXIMUM_SCREEN_WIDTH:
        screen_height = MAXIMUM_SCREEN_HEIGHT
        screen_width = MAXIMUM_SCREEN_WIDTH
    
    title_start_height = screen_height // 16
    title_start_width = screen_width // 2 - len(name[0]) // 2

    subtitle = 'A Cellular Automata visualization tool'
    subtitle_start_height = title_start_height + 10
    subtitle_start_width = screen_width // 2 - len(subtitle) // 2

    exit = False

    print_title(stdscr, name, title_start_height, title_start_width)
    stdscr.addstr(subtitle_start_height, subtitle_start_width, subtitle, curses.A_BOLD)
    print_menu(stdscr, current_row_idx, current_menu)

    while not exit:
        # general menu state
        if current_state == 's_menu':
            key = stdscr.getch()
            stdscr.clear()

            # revert the getch to wait for a key
            # this prevents high cpu usage
            stdscr.nodelay(False)

            if key == curses.KEY_UP and current_menu is not about:
                if current_row_idx == 0:
                    current_row_idx = len(current_menu) - 1
                else:
                    # go up a row
                    current_row_idx -= 1
            elif key == curses.KEY_DOWN and current_menu is not about:
                if current_row_idx == len(current_menu) - 1:
                    current_row_idx = 0
                else:
                    # go down a row
                    current_row_idx += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                # go to next menu or change state
                if current_menu_state == 's_menu_menu':
                    # main menu

                    # choose 'what is a cellular automaton?' option
                    if current_row_idx == 0:
                        current_menu_state = 's_menu_about'

                    # 'choose automata' option
                    elif current_row_idx == 1:
                        current_menu_state = 's_menu_choose_automata'

                    # choose 'exit' option
                    elif current_row_idx == len(current_menu) - 1:
                        # exit loop
                        exit = True

                elif current_menu_state == 's_menu_about':
                    current_menu_state = 's_menu_menu'

                elif current_menu_state == 's_menu_choose_automata':
                    # choose automata menu

                    # if not selecting 'back' option
                    if current_row_idx != len(current_menu) - 1:
                        selected_automata_idx = current_row_idx            # remember the automata selected
                        current_menu_state = 's_menu_displaying_boards'

                    # selecting 'back' option
                    elif current_row_idx == len(current_menu) - 1:
                        current_menu_state = 's_menu_menu'

                elif current_menu_state == 's_menu_displaying_boards':
                    # displaying boards menu

                    # 'blank' board
                    if current_row_idx == 0:
                        h, w = stdscr.getmaxyx()
                        # generate blank board
                        board = Board(height = h, width = w // 3, random = False)
                        current_state = 's_display_automata' # change state

                    # if not selecting 'back' option
                    elif current_row_idx != 0 and current_row_idx != len(current_menu) - 1:
                        board = load_board(current_row_idx, selected_automata_idx) # load the board selected
                        current_state = 's_display_automata'

                    # selecting 'back' option
                    elif current_row_idx == len(current_menu) - 1:
                        current_menu_state = 's_menu_choose_automata'

                if current_menu_state == 's_menu_menu':
                    # show main menu
                    current_menu = menu
                    current_row_idx = 0
                elif current_menu_state == 's_menu_about':
                    # show about menu
                    current_menu = about
                    current_row_idx = len(about) - 1
                elif current_menu_state == 's_menu_choose_automata':
                    # show automata selection menu
                    current_menu = automatas
                    current_row_idx = 0
                elif current_menu_state == 's_menu_displaying_boards':
                    # show board display menu
                    current_menu = boards_display
                    current_row_idx = 0

            # render the menu to the screen
            stdscr.clear()
            if current_menu_state == 's_menu_menu':
                print_title(stdscr, name, title_start_height, title_start_width)
                stdscr.addstr(subtitle_start_height, subtitle_start_width, subtitle, curses.A_BOLD)
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

            # set the getch to not wait for a key
            stdscr.nodelay(True)

            while True:
                key = stdscr.getch()

                if key == curses.KEY_ENTER or key in [10, 13]:
                    current_state = 's_menu'
                    current_menu_state = 's_menu_displaying_boards'
                    break
                elif key == curses.KEY_UP:
                    if TIME_BETWEEN_FRAMES > 0.01:
                        TIME_BETWEEN_FRAMES -= 0.01
                elif key == curses.KEY_DOWN:
                    TIME_BETWEEN_FRAMES += 0.01

                print_board(stdscr, board, y, x) # print the board
                board = automata.update(TIME_BETWEEN_FRAMES) # update the board

if __name__ == '__main__':
    curses.wrapper(main)