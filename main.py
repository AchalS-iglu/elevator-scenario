IDLE = 0
UP = 1
DOWN = 2

class Building():
    def __init__(self, floor_count = 6, elevator_count = 3):
        self.FLOOR_COUNT = floor_count
        self.floors = list(range(1, floor_count + 1))
        self.elevators = []
        for i in range(elevator_count):
            self.elevators.append(Elevator(8))
    
    def call(self, floor, direction):
        dist = []
        for elevator in self.elevators:
            if elevator.dir == IDLE:
                dist.append(abs(elevator.cur_floor - floor)) 
            if direction == UP:
                if elevator.cur_floor < floor and elevator.dir == UP:
                    dist.append((abs(elevator.cur_floor - floor)) * (1/self.floors))
                else:
                    dist.append((abs(elevator.cur_floor - floor)) * (self.floors))
            elif direction == DOWN:
                if elevator.cur_floor > floor and elevator.dir == DOWN:
                    dist.append((abs(elevator.cur_floor - floor)) * (1/self.floors))
                else:
                    dist.append((abs(elevator.cur_floor - floor)) * (self.floors))
            else:
                dist.append((abs(elevator.cur_floor - floor)) * (self.floors))
            #dist.append([elevator.dir, abs(elevator.cur_floor - floor)])
        #self.elevators[dist[dist.index(min(dist))]].call(floor)
        

class Elevator():
    def __init__(self, max_capacity = 8):
        self.cur_floor = 0
        self.dir = IDLE
        self.max_capacity = max_capacity
    
    def call(self, floor):
        pass