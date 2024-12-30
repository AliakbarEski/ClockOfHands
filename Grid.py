import GridElement

class Grid:

    def __init__(self, rows, cols, rad, width, height, digit_grid_width, digit_grid_height):
        self.rows = rows
        self.cols = cols
        self.rad = rad
        self.w = width
        self.h = height
        self.digit_grid_width = digit_grid_width
        self.digit_grid_height = digit_grid_height

        self.grid = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(GridElement.GridElement(j * self.rad + rad/2, i * self.rad + rad/2, self.rad, self.w, self.h))
            self.grid.append(row)
        
    def initialize(self, canvas):
        for row in self.grid:
            for element in row:
                element.initialize(canvas)

    def draw(self, canvas):
        for row in self.grid:
            for element in row:
                element.draw(canvas)

    def update(self):
        for row in self.grid:
            for element in row:
                element.update()

    def show_num(self, num, offset):
        for i in range(self.rows//3):
            for j in range(self.cols//3):
                self.grid[offset[0] + i][offset[1] + j].show_hands_idle()
        
        if num == 0:
            self.grid[offset[0]+0][offset[1]+0].show_hands_top_left_corner()
            self.grid[offset[0]+0][offset[1]+1].show_hands_top_right_corner()
            self.grid[offset[0]+1][offset[1]+0].show_hands_vertical()
            self.grid[offset[0]+1][offset[1]+1].show_hands_vertical()
            self.grid[offset[0]+2][offset[1]+0].show_hands_bottom_left_corner()
            self.grid[offset[0]+2][offset[1]+1].show_hands_bottom_right_corner()
        
        elif num == 1:
            self.grid[offset[0]+0][offset[1]+0].show_hands_idle()
            self.grid[offset[0]+0][offset[1]+1].show_hands_vertical_down()
            self.grid[offset[0]+1][offset[1]+0].show_hands_idle()
            self.grid[offset[0]+1][offset[1]+1].show_hands_vertical()
            self.grid[offset[0]+2][offset[1]+0].show_hands_idle()
            self.grid[offset[0]+2][offset[1]+1].show_hands_vertical_up()

        elif num == 2:
            self.grid[offset[0]+0][offset[1]+0].show_hands_horizontal_right()
            self.grid[offset[0]+0][offset[1]+1].show_hands_top_right_corner()
            self.grid[offset[0]+1][offset[1]+0].show_hands_top_left_corner()
            self.grid[offset[0]+1][offset[1]+1].show_hands_bottom_right_corner()
            self.grid[offset[0]+2][offset[1]+0].show_hands_bottom_left_corner()
            self.grid[offset[0]+2][offset[1]+1].show_hands_horizontal_left()
        
        elif num == 3:
            self.grid[offset[0]+0][offset[1]+0].show_hands_horizontal_right()
            self.grid[offset[0]+0][offset[1]+1].show_hands_top_right_corner()
            self.grid[offset[0]+1][offset[1]+0].show_hands_horizontal_right()
            self.grid[offset[0]+1][offset[1]+1].show_hands_vertical()
            self.grid[offset[0]+2][offset[1]+0].show_hands_horizontal_right()
            self.grid[offset[0]+2][offset[1]+1].show_hands_bottom_right_corner()
        
        elif num == 4:
            self.grid[offset[0]+0][offset[1]+0].show_hands_vertical_down()
            self.grid[offset[0]+0][offset[1]+1].show_hands_vertical_down()
            self.grid[offset[0]+1][offset[1]+0].show_hands_bottom_left_corner()
            self.grid[offset[0]+1][offset[1]+1].show_hands_vertical()
            self.grid[offset[0]+2][offset[1]+0].show_hands_idle()
            self.grid[offset[0]+2][offset[1]+1].show_hands_vertical_up()

        elif num == 5:
            self.grid[offset[0]+0][offset[1]+0].show_hands_top_left_corner()
            self.grid[offset[0]+0][offset[1]+1].show_hands_horizontal_left()
            self.grid[offset[0]+1][offset[1]+0].show_hands_bottom_left_corner()
            self.grid[offset[0]+1][offset[1]+1].show_hands_top_right_corner()
            self.grid[offset[0]+2][offset[1]+0].show_hands_horizontal_right()
            self.grid[offset[0]+2][offset[1]+1].show_hands_bottom_right_corner()

        elif num == 6:
            self.grid[offset[0]+0][offset[1]+0].show_hands_top_left_corner()
            self.grid[offset[0]+0][offset[1]+1].show_hands_horizontal_left()
            self.grid[offset[0]+1][offset[1]+0].show_hands_vertical()
            self.grid[offset[0]+1][offset[1]+1].show_hands_top_right_corner()
            self.grid[offset[0]+2][offset[1]+0].show_hands_bottom_left_corner()
            self.grid[offset[0]+2][offset[1]+1].show_hands_bottom_right_corner()
        
        elif num == 7:
            self.grid[offset[0]+0][offset[1]+0].show_hands_horizontal_right()
            self.grid[offset[0]+0][offset[1]+1].show_hands_top_right_corner()
            self.grid[offset[0]+1][offset[1]+0].show_hands_idle()
            self.grid[offset[0]+1][offset[1]+1].show_hands_vertical()
            self.grid[offset[0]+2][offset[1]+0].show_hands_idle()
            self.grid[offset[0]+2][offset[1]+1].show_hands_vertical_up()
        
        elif num == 8:
            self.grid[offset[0]+0][offset[1]+0].show_hands_top_left_corner()
            self.grid[offset[0]+0][offset[1]+1].show_hands_top_right_corner()
            self.grid[offset[0]+1][offset[1]+0].show_hands_bottom_left_corner()
            self.grid[offset[0]+1][offset[1]+1].show_hands_bottom_right_corner()
            self.grid[offset[0]+2][offset[1]+0].show_hands_bottom_left_corner()
            self.grid[offset[0]+2][offset[1]+1].show_hands_bottom_right_corner()
        
        elif num == 9:
            self.grid[offset[0]+0][offset[1]+0].show_hands_top_left_corner()
            self.grid[offset[0]+0][offset[1]+1].show_hands_top_right_corner()
            self.grid[offset[0]+1][offset[1]+0].show_hands_bottom_left_corner()
            self.grid[offset[0]+1][offset[1]+1].show_hands_vertical()
            self.grid[offset[0]+2][offset[1]+0].show_hands_horizontal_right()
            self.grid[offset[0]+2][offset[1]+1].show_hands_bottom_right_corner()

    def show_nums(self, nums):
        for i in range(len(nums)):
            self.show_num(nums[i], ((i//self.digit_grid_width) * (self.rows//self.digit_grid_height), (i%self.digit_grid_width) * (self.cols//self.digit_grid_width)))