speed = 0
speed_limit = 0
wanted_list = ["Jones", "Eric", "Dylan"]
fines = []
summary_list = []
over_limit = 0
statement = ""
user_answer = ""

def user_inputs():
    global speed
    global speed_limit
    while True:
        try:
            speed = int(input("\nWhat was the speed you were going at? : "))
            
            if speed <= 0:
                print("Please enter proper numbers\n")

            else:
                while True:
                    try:
                        speed_limit = int(input("\nWhat was the speed limit? : "))

                        if speed_limit <= 0:
                            print("Please enter proper numbers\n")
                        else:
                            break
                    except ValueError:
                        print("Please enter valid intergers\n")
                break

        except ValueError:
            print("Please enter valid intergers\n")

def calculate_fine(x, y):
    global over_limit
    over_limit = x - y
    

def fine_checker(x):
    global statement

    if x > 0 and x < 50:
        statement = "The speed of your Vechile going at was {}kms^1 and the Limit was {}; \nYou are {}km^-1 OVER the speeding limit you MUST pay a fine of {:.2f}".format(x * 10)
    elif x >= 50 and x <= 80:
        statement = "The speed of your Vechile going at was {}kms^1 and the Limit was {}; \nYou are {}km^-1 OVER the speeding limit you MUST hand in your liscence".format(speed, speed_limit ,over_limit)
    elif x > 80:
        statement = "The speed of your Vechile going at was {}kms^1 and the Limit was {}; \nYou are {}km^-1 WELL beyond the speeding limit you MUST spend time in jail".format(speed, speed_limit ,over_limit)
    else:
        statement = "The speed of your Vechile going at was {}kms^1 and the Limit was {}; \nYou are {}km^-1 BELOW the speeding limit you do not have to pay or do anything!".format(speed, speed_limit ,over_limit * -1)

    print(statement)

def summary_manager():
    global summary_list

    summary_list.append(["\nName: {}\n".format(name.lower().capitalize()),"Your speed: {}\n".format(speed), "The speed limit: {}".format(speed_limit),"\nSummary: {}".format(statement)])

    user_answer = input("\nWould you like to take a look at your list of records? (Y/N): ").strip().lower()
    while True:
        if user_answer == "y":
            while True:
                try:
                    user_answer = int(input("\nWhich record would you like to read?\nPlease enter from 1-{} for corrisponding record : ".format(len(summary_list))))

                    if user_answer <= len(summary_list) and user_answer >= 1:
                        print(''.join(summary_list[user_answer - 1]))
                        break
                    
                    elif user_answer <= 0 or isinstance(user_answer, float):
                        print("\nPlease enter valid whole numbers")
                except ValueError:
                    print("\nPlease enter valid numbers")
        elif user_answer == "n":
            break
        else:
            print("Please answer valid input Y or N")
        break
    




while True:
    name = input("Please enter your name: ")
    for i in range(0, len(wanted_list)):
        if name.upper().capitalize() == wanted_list[i]:
            print("{} is wanted for arrest".format(name.lower().capitalize()))
    
    user_inputs()
    calculate_fine(speed, speed_limit)
    fine_checker(over_limit)
    summary_manager()


    user_answer = input("\nWould you like to enter another record? (Y/N): ").lower().strip()

    if user_answer == "y":
        continue
    elif user_answer == "n":
        break
    else:
        print("Please enter Y or N")

    

    
    


        