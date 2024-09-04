import math
def format_string(value1, value2):
    return "{} and '{}'".format(value1, value2)
formatted_string = format_string(145, 'o')
print("Formatted String:", formatted_string)
radius = 84
pi = 3.14
area_of_pond = pi * radius ** 2
print("Area of the pond (in square meters):", area_of_pond)
water_per_square_meter = 1.4
total_water = area_of_pond * water_per_square_meter
total_water_rounded = round(total_water)
print("Total amount of water in liters (rounded):", total_water_rounded)

distance = 490
time = 7 * 60   
speed = distance / time
speed_rounded = round(speed)
print("Speed in meters per second (rounded):", speed_rounded)
