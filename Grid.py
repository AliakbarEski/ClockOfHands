import GridElement
import HandPositions as hp

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
        
        # initialize the hands positions for each digit
        self.hand_positions = [ 
                               # 0
                               [[hp.HandPositions.top_left_corner,    hp.HandPositions.top_right_corner], 
                               [hp.HandPositions.vertical,            hp.HandPositions.vertical], 
                               [hp.HandPositions.bottom_left_corner,  hp.HandPositions.bottom_right_corner]], 

                               # 1
                               [[hp.HandPositions.idle,               hp.HandPositions.vertical_down], 
                               [hp.HandPositions.idle,                hp.HandPositions.vertical], 
                               [hp.HandPositions.idle,                hp.HandPositions.vertical_up]], 

                               # 2
                               [[hp.HandPositions.horizontal_right,   hp.HandPositions.top_right_corner], 
                               [hp.HandPositions.top_left_corner,     hp.HandPositions.bottom_right_corner], 
                               [hp.HandPositions.bottom_left_corner,  hp.HandPositions.horizontal_left]], 

                               # 3
                               [[hp.HandPositions.horizontal_right,   hp.HandPositions.top_right_corner], 
                               [hp.HandPositions.horizontal_right,    hp.HandPositions.vertical], 
                               [hp.HandPositions.horizontal_right,    hp.HandPositions.bottom_right_corner]],

                               # 4
                               [[hp.HandPositions.vertical_down,      hp.HandPositions.vertical_down], 
                               [hp.HandPositions.bottom_left_corner,  hp.HandPositions.vertical], 
                               [hp.HandPositions.idle,                hp.HandPositions.vertical_up]],

                               # 5
                               [[hp.HandPositions.top_left_corner,    hp.HandPositions.horizontal_left], 
                               [hp.HandPositions.bottom_left_corner,  hp.HandPositions.top_right_corner], 
                               [hp.HandPositions.horizontal_right,    hp.HandPositions.bottom_right_corner]],

                               # 6
                               [[hp.HandPositions.top_left_corner,    hp.HandPositions.horizontal_left], 
                               [hp.HandPositions.vertical,            hp.HandPositions.top_right_corner], 
                               [hp.HandPositions.bottom_left_corner,  hp.HandPositions.bottom_right_corner]],

                               # 7
                               [[hp.HandPositions.horizontal_right,   hp.HandPositions.top_right_corner], 
                               [hp.HandPositions.idle,                hp.HandPositions.vertical], 
                               [hp.HandPositions.idle,                hp.HandPositions.vertical_up]],

                               # 8
                               [[hp.HandPositions.top_left_corner,    hp.HandPositions.top_right_corner], 
                               [hp.HandPositions.bottom_left_corner,  hp.HandPositions.bottom_right_corner], 
                               [hp.HandPositions.bottom_left_corner,  hp.HandPositions.bottom_right_corner]],

                               # 9
                               [[hp.HandPositions.top_left_corner,    hp.HandPositions.top_right_corner], 
                               [hp.HandPositions.bottom_left_corner,  hp.HandPositions.vertical], 
                               [hp.HandPositions.horizontal_right,    hp.HandPositions.bottom_right_corner]]
        ]

    def draw(self, canvas):
        for row in self.grid:
            for element in row:
                element.draw(canvas)

    def update(self):
        for row in self.grid:
            for element in row:
                element.update()

    def show_num(self, num, offset):
        for i in range(self.rows//self.digit_grid_height):
            for j in range(self.cols//self.digit_grid_width):
                self.grid[offset['h'] + i][offset['w'] + j].set_hands(self.hand_positions[num][i][j])

    def show_nums(self, nums):
        for i in range(len(nums)):
            self.show_num(nums[i], 
                          {
                           'h':(i//self.digit_grid_width) * (self.rows//self.digit_grid_height), 
                           'w':(i%self.digit_grid_width) * (self.cols//self.digit_grid_width)
                          }
                        )