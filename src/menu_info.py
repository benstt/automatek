menu = ['What is a Cellular Automaton?', 'Choose automata', 'Play random automata', 'Make your own automata!', 'Exit']
about = [
    'A cellular automaton is a discrete model of computation studied in automata theory.',
    '',
    'It consists of a regular grid of cells,',
    'each in one of a finite number of states, such as on and off.',
    '',
    'For each cell, a set of cells called its neighborhood is defined relative',
    'to the specified cell.',
    '',
    'An initial state (time t = 0) is selected by assigning a state for each cell.',
    'A new generation is created (advancing t by 1), according to some fixed rule',
    '(generally, a mathematical function)  that determines the new state of each cell',
    'in terms of the current state of the cell and the states of the cells in its neighborhood.',
    '',
    'Back'
    ]
controls = ['Press ENTER to stop', 'Press UP/DOWN arrow keys to adjust velocity']

automatas = ["Conway's Game of Life", "Langton's Ant", "Brian's Brain", "Day 'n' Night", 'Back']
boards_display = ['Blank Board', 'Beacon', 'Blinker', 'Crosshair', 'Glider', 'Gosper Glider Gun', 'Little Ship', 'Ship', 'Star', 'Toad', 'Back']
boards = ['', 'beacon.txt', 'blinker.txt', 'crosshair.txt', 'glider.txt', 'gosper_glider_gun.txt', 'little_ship.txt', 'ship.txt', 'star.txt', 'toad.txt']

conways_about = [
    '* Any live cell with two or three live neighbours survives.',
    '* Any dead cell with three live neighbours becomes a live cell.',
    '* All other live cells die in the next generation.',
    'Similarly, all other dead cells stay dead.'
    ]

langton_about = [
    '* At a white square, turn 90° clockwise, flip the color of the square, move forward one unit', 
    '* At a black square, turn 90° counter-clockwise, flip the color of the square, move forward one unit'
    ]

brian_about = [
    '* A cell turns on if it was off but had exactly two neighbors that were on',
    '* All cells that were "on" go into the "dying" state',
    '* Cells that were in the dying state go into the off state.'
    ]

day_night_about = [
    '* A dead cell becomes live (is born) if it has 3, 6, 7, or 8 live neighbors',
    '* A live cell remains alive (survives) if it has 3, 4, 6, 7, or 8 live neighbors.'
    ]

automatas_about = {
    0: conways_about,
    1: langton_about,
    2: brian_about,
    3: day_night_about
}

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

subtitle = 'A Cellular Automata visualization tool'