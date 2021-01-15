class Stator:
    def __init__(self, printer, character=["ﺕ"], location=[1, 1]):
        self.character = character
        self.location = location

        self.size = [len(self.character[0]), len(self.character)]
        self.printer = printer

        self.printer.add(self)

class Mover(Stator):
    def __init__(self, printer, character=["ﺕ"], location=[1, 1]):
        Stator.__init__(self, printer, character, location)
        
        self.max_speed = 3
        self.acceleration = .5
    
    def step(self, vector):
        self.location[0] += vector[0]
        self.location[1] += vector[1]
        self.printer.display()
        print(self.location)

    def move(self, vector):
        cur_speed = [0, 0]
        cur_speed[0] = vector[0] * self.acceleration * self.printer.time.delta_time ** 2
        cur_speed[1] = vector[1] * self.acceleration * self.printer.time.delta_time ** 2

        self.step(cur_speed)

    def has_valid_location(self):
        if self.location[0] > 0 and self.location[1] > 0:
            return self.location[0] <= self.printer.screen_size[0] \
                   and self.location[1] <= self.printer.screen_size[1]

        return False
