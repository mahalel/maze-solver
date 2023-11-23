from graphics import Line, Point

class Cell():

    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):    
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
              
        bot_left = Point(self._x1, self._y1)
        bot_right = Point(self._x2, self._y1)
        top_left = Point(self._x1, self._y2)
        top_right = Point(self._x2, self._y2)
        
        if self.has_left_wall:
            line = Line(bot_left, top_left)
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(bot_right, top_right)
            self._win.draw_line(line)      
        if self.has_top_wall:
            line = Line(top_left, top_right)
            self._win.draw_line(line)    
        if self.has_bottom_wall:
            line = Line(bot_left, bot_right)
            self._win.draw_line(line)
            
            
    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
            
        fill_color = "red"
        if undo:
            fill_color = "gray"
        
        x_mid = (self._x1 + self._x2) / 2
        y_mid = (self._y1 + self._y2) / 2
        
        to_x_mid = (to_cell._x1 + to_cell._x2) / 2
        to_y_mid = (to_cell._y1 + to_cell._y2) / 2
        
        # Move Left
        if self._x1 > to_cell._x1:
            line = Line(Point(x_mid, y_mid),Point(self._x1, y_mid))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_cell._x2, to_y_mid), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)
            
        # moving right
        elif self._x1 < to_cell._x1:
            line = Line(Point(x_mid, y_mid), Point(self._x2, y_mid))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_cell._x1, to_y_mid), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving up
        elif self._y1 > to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y1))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_cell._y2), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving down
        elif self._y1 < to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y2))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_x_mid, to_cell._y1))
            self._win.draw_line(line, fill_color)