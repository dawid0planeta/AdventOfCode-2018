from itertools import cycle

class Cart:
    def __init__(self, pos, direction):
        self.state = cycle([3, 0, 1]) 
        self.direction = direction
        self.pos = pos
        self.weight = self.pos[0] * 150 + self.pos[1]
        self.iteration = 0 

    def change_direction(self, direction):
        self.direction = direction

    def update(self):
        self.weight = self.pos[0] * 150 + self.pos[1]
    

