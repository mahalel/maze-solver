from cell import Cell
from time import sleep

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
        ):
        
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        
    def _create_cells(self):
        for row in range(self._num_rows):
            row = []
            for col in range(self._num_cols):
                row.append(Cell(self._win))
            self._cells.append(row)
        
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)
                
        
    def _draw_cell(self, i, j):
        if self._win is None:
            return

        x = j * self._cell_size_x + self._x1
        y = i * self._cell_size_y + self._y1
        c = Cell(self._win)
        
        c.draw(x, y, x + self._cell_size_x, y + self._cell_size_y)
        self._animate()        
        
    def _animate(self):
        self._win.redraw()
        sleep(0.05)