import math

class GridElement:    

    def __init__(self, x, y, r, width, height):
        self.x_offset = x
        self.y_offset = y
        self.radius = r
        self.w = width
        self.h = height
        self.hand_length = 0.85 * self.radius

        self.lines = []
        self.hand_angles = []
        self.current_hand_angles = []
        self.step_size = 3
        self.epsilon = 0

        self.hand_angles.append(225)
        self.hand_angles.append(225)

        self.current_hand_angles.append(0)
        self.current_hand_angles.append(0)
        self.need_update = False

    def _get_line_coords_for_hands(self, hand_angle):
        # why negative? because the y axis is inverted in tkinter, hence we count angles clockwise instead of counter clockwise
        rads = -math.radians(hand_angle)
        return (self.x_offset, self.y_offset, self.x_offset + self.hand_length/2 * math.cos(rads), self.y_offset + self.hand_length/2 * math.sin(rads))

    
    def set_hands(self, hand_angles):
        self.hand_angles = hand_angles    

    def initialize(self, canvas):
        self.lines.append(canvas.create_line(self._get_line_coords_for_hands(self.current_hand_angles[0])))
        self.lines.append(canvas.create_line(self._get_line_coords_for_hands(self.current_hand_angles[1])))
        canvas.create_oval(self.x_offset - self.radius/2, self.y_offset - self.radius/2, self.x_offset + self.radius/2, self.y_offset + self.radius/2, outline="#505050")

    def update(self):

        for i in range(0, len(self.hand_angles)):
            if (self.hand_angles[i] - self.current_hand_angles[i]) > self.epsilon:
                self.current_hand_angles[i] += self.step_size
                self.need_update = True

            if (self.hand_angles[i] - self.current_hand_angles[i]) < self.epsilon:
                self.current_hand_angles[i] -= self.step_size
                self.need_update = True

    def draw(self, canvas):
        if self.need_update:
            self.need_update = False
            for i in range(0, len(self.lines)):
                canvas.coords(self.lines[i], self._get_line_coords_for_hands(self.current_hand_angles[i]))
