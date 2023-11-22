from graphics import Line, Point

class Cell():

    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.__win = win

    def draw(self, x1, y1, x2, y2):    
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
              
        bot_left = Point(self.__x1, self.__y1)
        bot_right = Point(self.__x2, self.__y1)
        top_left = Point(self.__x1, self.__y2)
        top_right = Point(self.__x2, self.__y2)
        
        if self.has_left_wall:
            line = Line(bot_left, top_left)
            self.__win.draw_line(line)
        if self.has_right_wall:
            line = Line(bot_right, top_right)
            self.__win.draw_line(line)      
        if self.has_top_wall:
            line = Line(top_left, top_right)
            self.__win.draw_line(line)    
        if self.has_bottom_wall:
            line = Line(bot_left, bot_right)
            self.__win.draw_line(line)
            
            
    def draw_move(self, to_cell, undo=False):
        