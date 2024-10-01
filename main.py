from graphics import *
from cell import Cell

def main():
    win = Window(800,600)
    cell1 = Cell(win)
    cell1.draw(50,50,100,100)
    win.wait_for_close()


main()