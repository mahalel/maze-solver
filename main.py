from graphics import Window
from cell import Cell
from maze import Maze
       
def main():
    win = Window(800,600)
    
    # c = Cell(win)
    # c.has_left_wall = False
    # c.draw(50, 50, 100, 100)
    
    # c = Cell(win)
    # c.has_right_wall = False
    # c.draw(125, 125, 200, 200)

    # # c = Cell(win)
    # # c.has_bottom_wall = False
    # # c.draw(225, 225, 250, 250)

    # y = Cell(win)
    # y.has_top_wall = False
    # y.draw(300, 300, 500, 500)

    # c.draw_move(y)
    
    maze = Maze(10, 10, 3, 3, 200, 180, win)
    
    win.wait_for_close()
    
main()