# Cellular Automatas
Different cellular automatas implementation in Python that runs on the terminal.

The project is entirely for learning purposes and it is based on [Robert Heaton's Game of Life article](https://robertheaton.com/2018/07/20/project-2-game-of-life/).

## Use
The script either loads a .txt file from a directory or generates an entire random board to have fun with.

In `main.py`, change the `source` parameter with the file you'd want to use:
```python
board_from_file = Board(source = '..\pattern.txt')
```
or make it entirely random:
```python
random_board = Board(15, 20)
```
Then, specify the automata you'll want to use and set to update it (as of 10/05/21 only has two of them):
```python
langton = LangtonAnt(board, ant_x, ant_y)
langton.update(time_between_frames)
```

Lastly, run the code on the terminal by using
```
$ python main.py
```

Keep in mind that the .txt file has to be kind of a _binary_ matrix, just as in the ones in the samples folder.

Enjoy!
