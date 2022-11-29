class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = 0

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return self.passengers

    def pick_up(self, person_name):
        self.passengers += 1

    def drop_off(self, person_name):
        self.passengers -= 1
    
    def empty(self):
        self.passengers = 0 

    def pick_up_from_stop(self, bus_stop):
        for name in bus_stop.queue:
            self.pick_up(name)
        bus_stop.clear()
