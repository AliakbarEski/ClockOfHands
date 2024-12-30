import tkinter
import Grid
import datetime
import time

radius = 80
digit_height = 3
digit_width = 2
digit_grid_height = 3
digit_grid_width = 2

grid_height = digit_height * digit_grid_height
grid_width = digit_width * digit_grid_width

canvas_height = radius * grid_height
canvas_width = radius * grid_width

update_interval = 5

def update():
    update.last_update = 0 if not hasattr(update, 'last_update') else update.last_update
    if (time.time() - update.last_update) >= update_interval:
        s = datetime.datetime.now().second//update_interval * update_interval
        grid.show_nums([datetime.datetime.now().hour // 10, datetime.datetime.now().hour % 10, datetime.datetime.now().minute // 10, datetime.datetime.now().minute % 10, s // 10, s % 10])
        update.last_update = time.time()     
    
    grid.update()
    grid.draw(C)
    root.after(33, update)


if __name__ == "__main__":
    root = tkinter.Tk()
    root.after(33, update)
    root.title("Clock Of Hands")

    root.geometry(str(canvas_width) + "x" + str(canvas_height))
    C = tkinter.Canvas(root, bg="black", height=canvas_height, width=canvas_width)
    C.pack()

    grid = Grid.Grid(grid_height, grid_width, radius, canvas_width, canvas_height, digit_grid_width, digit_grid_height)
    grid.initialize(C)

    root.mainloop()

