class Vehicle:

    # class level attribute
    type = "ground"
    propulsion = "battery"


    def __init__(self, name, color, num_wheels, speed):
        self.name = name
        self.color = color
        self.num_wheels = num_wheels
        self.speed = speed
        self.type = "ground"

    def print_details(self):
        print(self.name, "is", self.color, "and has a top speed of", self.speed, "mph")

    def paint_vehicle(self, new_color):
        self.color = new_color