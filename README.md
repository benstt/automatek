# Conway's Game of Life
Game of Life implementation in Python that runs on the terminal.

The project is entirely for learning purposes and it is based on [Robert Heaton's Game of Life article](https://robertheaton.com/2018/07/20/project-2-game-of-life/).

## Use
The script either loads a .txt file from a directory or generates an entire random board to have fun with.

In `main.py`, change the `source` parameter with the file you'd want to use: <br />
`board_from_file: Board(source = '..\pattern.txt')`
or make it entirely random: <br />
`random_board: Board(15, 20)`

Keep in mind that it has to be kind of a _binary_ matrix, just as in the ones in the samples folder.
