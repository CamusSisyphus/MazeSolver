from graphics import *
from cell import Cell
from maze import Maze
def main():
    win = Window(800,600)
    maze = Maze(50,50,10,15,40,40,win)
    maze._break_entrance_and_exit()

    win.wait_for_close()


main()