from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self._root = Tk()
        self._root.title("Testing TK")
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._canvas = Canvas(self._root, bg="white", width=width, height=height)
        self._canvas.pack(expand=True, fill=BOTH) 
        self._running = False
        
    def redraw(self):
        self._root.update_idletasks()
        self._root.update()
        
    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()
        print("Window closed...")
        
    def draw_line(self, line, fill_color="black"):
        line.draw(self._canvas, fill_color)             
  
    def close(self):
        self._running = False


class Point:  
    def __init__(self, x, y):
        self.x = x
        self.y = y        
        

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, 
            self.p1.y, 
            self.p2.x, 
            self.p2.y, 
            fill=fill_color, 
            width=2
        )
        canvas.pack(expand=True, fill=BOTH) 