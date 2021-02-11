speed = 0
speed_limit = 0
wanted_list = ["Jones", "Eric", "Dylan"]

import os
            
def calculate_fine(x, y):   
    over_limit = x - y
    return over_limit

def speeding_summary(x):
    if x > 0 and x < 50:
        print(name, "You are over the speeding limit you must pay a fine of {:.2f}".format(x * 10))
    elif x >= 50 and x <= 80:
        print(name, "You are well over the speeding limit you must hand in your liscence")
    elif x > 80:
        print(name, "You are well beyond the speeding limit you must spend time in jail")
    else:
        print(name, "You are below the speeding limit you do not have to pay or do anything!")    
    
name = input("Please enter your name: ")

for x in range(0, len(wanted_list)):
    if name.lower().strip() == wanted_list[x].lower():
        print("{}, you are wanted by the police".format(name.strip().lower().capitalize()))

while True:
    try:
        speed = int(input("What is the speed that you were going: "))
        if speed < 0:
            print("Please enter a valid interger")
        else:
            break
    except ValueError:
        print("Please enter an interger")
        
while True:
    try:
        speed_limit = int(input("What is the speed limit?: ")) 
        if speed_limit < 0:
            print("Please enter a valid interger")
        else:
            break
    except ValueError:
        print("Please enter an interger")

over_limit = calculate_fine(speed, speed_limit)
over_limit = calculate_fine(speed, speed_limit)
summary = speeding_summary(over_limit)