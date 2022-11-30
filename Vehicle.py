class Vehicle:
    def __init__(self, name, color, num_wheels, speed):
        self.name = name
        self.color = color
        self.num_wheels = num_wheels
        self.speed = speed

bug_object = Vehicle() #object of the vehicle class and an instance of the vehicle class
turtle_object = Vehicle()
rover_object = Vehicle()

bug_object.color = "yellow"
bug_object.num_wheels = 4
bug_object.speed = 1

turtle_object.color = "green"
turtle_object.num_wheels = 2
turtle_object.speed = 5

rover_object.color = "purple"
rover_object.num_wheels = 4
rover_object.speed = 25

print("This vehicle is", bug_object.color, "and has a top speed of", bug_object.speed, "mph")
print("This vehicle is", turtle_object.color, "and has a top speed of", turtle_object.speed, "mph")
print("This vehicle is", rover_object.color, "and has a top speed of", rover_object.speed, "mph")