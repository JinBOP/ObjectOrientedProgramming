# import info from class
from Vehicle import Vehicle

bug_object = Vehicle("Beetle", "Yellow", 4, 1) #object of the vehicle class and an instance of the vehicle class
turtle_object = Vehicle("Turtle", "Green", 2, 5)
rover_object = Vehicle("Rover", "Purple", 4, 25)

bug_object.print_details()
# turtle_object.print_details()
# rover_object.print_details()

bug_object.paint_vehicle("blue")
bug_object.print_details()