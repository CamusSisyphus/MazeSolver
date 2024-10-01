from tkinter import Tk, BOTH, Canvas

class Window:

    def __init__(self,width,height) -> None:
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title('Maze Solver!')
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__root, width = self.width, height = self.height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("Window Closed..!")

    def close(self):
        self.running = False