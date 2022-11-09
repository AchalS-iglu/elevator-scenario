UP = 0
DOWN = 1

class Building():
    def __init__(self, floor_count = 6, elevator_count = 3):
        self.FLOOR_COUNT = floor_count
        self.floors = list(range(1, floor_count + 1))
        self.elevators = []
        for i in range(elevator_count):
            self.elevators.append(Elevator())
    
    def call(self, floor, direction):
        pass

class Elevator():
    pass