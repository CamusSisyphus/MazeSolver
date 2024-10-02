import random
import time
from cell import Cell

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            seed = None
        ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.seed = seed
        if not self.seed:
            random.seed(seed)

        self.__create_cells()
        self._reset_cells_visited()

    def __create_cells(self):
        self._cells = []
        for _ in range(self.__num_cols):
            col = []
            for _ in range(self.__num_rows):
                col.append(Cell(self.__win))
            self._cells.append(col)
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i,j)

    def __draw_cell(self, i, j):
        if not self.__win:
            return
        cell = self._cells[i][j]
        x1 = self.__x1 + i * self.__cell_size_x
        x2 = self.__x1 + (i + 1) * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        y2 = self.__y1 + (j + 1) * self.__cell_size_y
        cell.draw(x1,y1,x2,y2)
        self.__animate()

    def __animate(self):
        self.__win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        exit = self._cells[self.__num_cols - 1][ self.__num_rows - 1]
        entrance.has_top_wall = False        
        # self.__draw_cell(0,0)
        exit.has_bottom_wall = False
        # self.__draw_cell(self.__num_cols - 1,self.__num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            direction = [(0,1),(0,-1),(1,0),(-1,0)]
            for dx, dy in direction:
                x = i + dx
                y = j + dy
                if min(x,y) < 0 or x >= self.__num_cols or y >= self.__num_rows:
                    continue
                if self._cells[x][y].visited:
                    continue
                to_visit.append((x,y))
            if not to_visit:
                return
            x, y = random.choice(to_visit)

            if i == x:

                #down
                if j < y:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[x][y].has_top_wall = False
                # up
                else:
                    self._cells[i][j].has_top_wall = False
                    self._cells[x][y].has_bottom_wall = False
            else:

                #left
                if i > x:
                    self._cells[i][j].has_left_wall = False
                    self._cells[x][y].has_right_wall = False
                # right
                else:
                    self._cells[i][j].has_right_wall = False
                    self._cells[x][y].has_left_wall = False
            self._break_walls_r(x,y)

    def _reset_cells_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self._cells[i][j].visited = False
