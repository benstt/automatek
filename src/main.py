import curses
from random import *
from board import Board
from automatas import *
from menu_info import *

automatas_ranges = {
        0: 1,
        1: 1,
        2: 2,
        3: 1
 }

n_automatas = {
        0: GameOfLife,
        1: LangtonAnt,
        2: BrianBrain,
        3: DayNight
 }

def load_board(idx, automata_idx, rand = True):
    """
    Loads a board with the file path determined by the given index.

    Parameters
    ----------
    idx : int
        The index of the row selected in a menu.
    automata_idx : int
        The index of the automata wanted. This is used to tell the number of the possible values the board can have.
    """
    assert idx >= 1, 'Board index must be greater than zero.'
    return Board('..\samples\\' + boards[idx], n_range = automatas_ranges[automata_idx], random = rand)

def create_automata(idx, board):
    """
    Instantiates an automata based on the given index.

    Returns
    -------
    n_automatas[idx] : CellularAutomata
    """
    return n_automatas[idx](board)

def select_random_automata_and_board():
    rand_automata = randrange(0, len(n_automatas))
    rand_board = randrange(1, len(boards_display) - 1)

    return rand_automata, rand_board

def print_title(stdscr, name, height, width):
    """
    Prints every row of a list to form an ASCII text.

    Parameters
    ----------
    name : List
        A list containing the rows of the text.
    height : int
        The height wanted for the text to be displayed.
    width : int
        The width wanted for the text to be displayed.
    """
    stdscr.attron(curses.color_pair(2))
    for idx, row in enumerate(name):
        stdscr.addstr(height + idx, width, row)
    
    stdscr.attroff(curses.color_pair(2))

def print_menu(stdscr, selected_row_idx, list, height, width):
    """
    Prints a menu to the terminal.
    Prints every word of a given list centered on the screen and one below the other.

    Parameters
    ----------
    selected_row_idx : int
        The index of the row selected. Used to add a little color to the row.
    list : List
        A list of different options.
    height : int
        The height of the screen.
    width : int
        The width of the screen.
    """
    for idx, row in enumerate(list):
        # get the center of the screen for every option
        x = width // 2 - len(row) // 2
        if list is menu:
            # print at the bottom
            y = (height - (height // 4)) - (len(list) // 2) + idx
        else:
            # print at the middle of the screen
            y = height // 2 - (len(list) // 2) + idx

        # print the text
        if idx == selected_row_idx:
            # add some color to the row
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

def print_board(stdscr, board, height, width, size = 2):
    """
    Renders a board to the terminal.
    Prints every 1 as a symbol and every 0 as a blank space.

    Parameters
    ----------
    board : Board
        A board to display.
    height : int
        The height where the board will be printed.
    width : int
        The width where the board will be printed.
    size : int
        The width of the cells to display.
    """
    #stdscr.clear()

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
            line += (display_as[val]) * size
        lines.append(line)
    # jump row and display lines
    # adds spaces at the beginning based on given width
    stdscr.addstr(height, width, ('\n').join(line for line in lines).replace('\n', '\n' + (' ' * width)))
    #stdscr.refresh()

def print_rules(stdscr, selected_automata_idx, height, width):
    """
    Prints the rules of the automata selected to the screen.
    """
    for idx, row in enumerate(automatas_about[selected_automata_idx]):
        stdscr.addstr(height + idx, width, row)

def print_controls(stdscr, height, width):
    """
    Prints the controls of a given list to the screen.
    """
    stdscr.addstr(height, width - len(controls[0]) // 2, controls[0])
    stdscr.addstr(height + 1, width - len(controls[1]) // 2, controls[1])

def print_current_automata_and_board(stdscr, height, width, automata, board):
    """
    Prints the current automata and board used to the screen.
    """
    # add some color to the text
    stdscr.attron(curses.color_pair(2))
    stdscr.addstr(height, width - len(automata) // 2 - 9, 'Current automata: ' + automata)
    stdscr.addstr(height + 1, width - len(board) // 2 - 7, 'Current board: ' + board)
    stdscr.attroff(curses.color_pair(2))

def clamp_value(actual, min, max):
    if actual < min:
        return min
    elif actual > max:
        return max
    
    return actual

def main(stdscr):
    # set cursor to not display
    curses.curs_set(0) 
    # initialize colors
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    
    # default number of seconds between each frame
    TIME_BETWEEN_FRAMES = 0.03

    # screen constants
    MINIMUM_SCREEN_HEIGHT = 28
    MINIMUN_SCREEN_WIDTH = 108
    MAXIMUM_SCREEN_HEIGHT = 81
    MAXIMUM_SCREEN_WIDTH = 360

    # get the size of the screen
    SCREEN_HEIGHT, SCREEN_WIDTH = stdscr.getmaxyx()
    
    # variables used to change the flow of the menu
    current_row_idx = 0
    current_display_options = menu
    current_loop_state = 'menu_state'
    current_menu_state = 'main_menu'
    selected_automata_idx = 0
    selected_randomly = False

    # clamp the screen sizes
    SCREEN_HEIGHT = clamp_value(SCREEN_HEIGHT, MINIMUM_SCREEN_HEIGHT, MAXIMUM_SCREEN_HEIGHT)
    SCREEN_WIDTH = clamp_value(SCREEN_WIDTH, MINIMUN_SCREEN_WIDTH, MAXIMUM_SCREEN_WIDTH)
    
    # start pos of the title
    title_start_height = SCREEN_HEIGHT // 4
    title_start_width = SCREEN_WIDTH // 2 - len(name[0]) // 2

    # start pos of the subtitle
    subtitle_start_height = title_start_height + 10
    subtitle_start_width = SCREEN_WIDTH // 2 - len(subtitle) // 2

    # variables for readability
    ABOUT_OPTION = 0
    CHOOSE_AUTOMATA_OPTION = 1
    PLAY_RANDOM_AUTOMATA_OPTION =  2

    # app loop flag
    exit = False

    # print UI to the screen
    print_title(stdscr, name, title_start_height, title_start_width)
    stdscr.addstr(subtitle_start_height, subtitle_start_width, subtitle, curses.A_BOLD)
    print_menu(stdscr, current_row_idx, current_display_options, SCREEN_HEIGHT, SCREEN_WIDTH)

    # main loop
    while not exit:
        # general menu state
        if current_loop_state == 'menu_state':
            key = stdscr.getch()
            stdscr.clear()

            # revert the getch to wait for a key
            # this prevents high cpu usage
            stdscr.nodelay(False)

            # variables for readability
            is_first_row = current_row_idx == 0
            back_option = len(current_display_options) - 1

            # check for key press
            if key == curses.KEY_UP and current_display_options is not about:
                if is_first_row:
                    # skip row to last
                    current_row_idx = back_option
                else:
                    # go up a row
                    current_row_idx -= 1
            elif key == curses.KEY_DOWN and current_display_options is not about:
                if current_row_idx == back_option:
                    # skip row to beginning
                    current_row_idx = 0
                else:
                    # go down a row
                    current_row_idx += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                # go to next menu or change state
                if current_menu_state == 'main_menu':
                    # main menu

                    # choose 'what is a cellular automaton?' option
                    if current_row_idx == ABOUT_OPTION:
                        current_menu_state = 'about_menu'

                    # 'choose automata' option
                    elif current_row_idx == CHOOSE_AUTOMATA_OPTION:
                        current_menu_state = 'choose_automata_menu'

                    # 'random automata' option
                    elif current_row_idx == PLAY_RANDOM_AUTOMATA_OPTION:
                        selected_randomly = True

                        selected_automata_idx, board_idx = select_random_automata_and_board()
                        board = load_board(board_idx, selected_automata_idx)
                        current_loop_state = 'display_automata_state'

                    elif current_row_idx == back_option:
                        # exit loop
                        exit = True

                elif current_menu_state == 'about_menu':
                    # can only go back to the menu
                    current_menu_state = 'main_menu'

                elif current_menu_state == 'choose_automata_menu':
                    # choose automata menu

                    if current_row_idx != back_option:
                        # remember the automata selected
                        selected_automata_idx = current_row_idx
                        current_menu_state = 'boards_display_menu'

                    elif current_row_idx == back_option:
                        current_menu_state = 'main_menu'

                elif current_menu_state == 'boards_display_menu':
                    # displaying boards menu

                    # 'blank' board
                    if is_first_row:
                        # generate blank board
                        board_range = automatas_ranges[selected_automata_idx]
                        board = Board(height = SCREEN_HEIGHT, width = SCREEN_WIDTH // 3, n_range = board_range, random = False)
                        current_loop_state = 'display_automata_state'

                    elif current_row_idx != 0 and current_row_idx != back_option:
                        # load the board selected
                        board = load_board(current_row_idx, selected_automata_idx) 
                        current_loop_state = 'display_automata_state'

                    elif current_row_idx == back_option:
                        current_menu_state = 'choose_automata_menu'

                if current_menu_state == 'main_menu':
                    # show main menu
                    current_display_options = menu
                    current_row_idx = 0
                elif current_menu_state == 'about_menu':
                    # show about menu
                    current_display_options = about
                    current_row_idx = len(about) - 1
                elif current_menu_state == 'choose_automata_menu':
                    # show automata selection menu
                    current_display_options = automatas
                    current_row_idx = 0
                elif current_menu_state == 'boards_display_menu':
                    # show board display menu
                    current_display_options = boards_display
                    current_row_idx = 0

            # render a menu to the screen depending on the current state
            stdscr.clear()
            if current_menu_state == 'main_menu':
                # display title and subtitle
                print_title(stdscr, name, title_start_height, title_start_width)
                stdscr.addstr(subtitle_start_height, subtitle_start_width, subtitle, curses.A_BOLD)
            elif current_menu_state == 'choose_automata_menu':
                # display select sentence
                text = 'Select an automata'
                stdscr.addstr(10, SCREEN_WIDTH // 2 - len(text) // 2, text, curses.A_BOLD)

                # not selecting 'back' option
                if current_row_idx != len(automatas) - 1:
                    # display automata rules
                    # get information about the automata selected
                    current_automata_about = automatas_about[current_row_idx]

                    # determine position to display based on how many rules and length of the sentece
                    height = SCREEN_HEIGHT - len(current_automata_about) - 2
                    width = SCREEN_WIDTH // 2 - (len(current_automata_about[0]) // 2)
                    # print rules
                    stdscr.addstr(height - 2, SCREEN_WIDTH // 2 - 3, 'RULES:')
                    print_rules(stdscr, current_row_idx, height, width)
            elif current_menu_state == 'boards_display_menu':
                # display select sentence
                text = 'Select a board'
                stdscr.addstr(6, SCREEN_WIDTH // 2 - len(text) // 2, text, curses.A_BOLD)

            # print the menu
            print_menu(stdscr, current_row_idx, current_display_options, SCREEN_HEIGHT, SCREEN_WIDTH)
            stdscr.refresh()

        # automata playing state
        elif current_loop_state == 'display_automata_state':
            # create instance of automata
            automata = create_automata(selected_automata_idx, board)

            # get center of the screen
            y = SCREEN_HEIGHT // 2 - (board.height // 2)
            x = SCREEN_WIDTH // 2 - (board.width)

            # set the getch to not stall waiting for a key
            stdscr.nodelay(True)

            while True:
                # check if a key is pressed
                key = stdscr.getch()

                if key == curses.KEY_ENTER or key in [10, 13]:
                    # return to menus
                    current_loop_state = 'menu_state'
                    if selected_randomly:
                        # go back to main menu
                        current_menu_state = 'main_menu'
                    else:
                        current_menu_state = 'boards_display_menu'
                    break
                elif key == curses.KEY_UP:
                    # increase velocity of display
                    if TIME_BETWEEN_FRAMES > 0.01:
                        TIME_BETWEEN_FRAMES -= 0.01
                elif key == curses.KEY_DOWN:
                    # decrease velocity of display
                    TIME_BETWEEN_FRAMES += 0.01

                # print board and controls
                stdscr.clear()
                print_board(stdscr, board, y, x)
                print_controls(stdscr, SCREEN_HEIGHT - 2, SCREEN_WIDTH // 2)
                if selected_randomly:
                    # get the names to display
                    current_automata_name = automatas[selected_automata_idx]
                    current_board_name = boards_display[board_idx]

                    print_current_automata_and_board(stdscr, SCREEN_HEIGHT - 5, SCREEN_WIDTH // 2, current_automata_name, current_board_name)
                stdscr.refresh()
                # update the board for the next frame
                board = automata.update(TIME_BETWEEN_FRAMES)

if __name__ == '__main__':
    curses.wrapper(main)