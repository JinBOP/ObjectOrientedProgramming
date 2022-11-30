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
        
bug_object = Vehicle("Beetle", "Yellow", 4, 1) #object of the vehicle class and an instance of the vehicle class
turtle_object = Vehicle("Turtle", "Green", 2, 5)
rover_object = Vehicle("Rover", "Purple", 4, 25)

bug_object.print_details()
# turtle_object.print_details()
# rover_object.print_details()

bug_object.paint_vehicle("blue")
bug_object.print_details()