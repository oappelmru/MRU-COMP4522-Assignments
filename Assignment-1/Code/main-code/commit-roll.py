# Skeleton for commit and roll-back exercise

import random

# loouup table for process codes               
def lookup(status:int)->str:
    POS_STATES = ( (1, 'retrieve-1'),
               (2, 'update-1'),
               (3, 'retrieve-2'),
               (4, 'update-2'),
               (5, 'update-3'),
               (6, 'update-4'),
               (7, 'commit'),
               (8, 'update-5'),
               (9, 'exception'),
               (10, 'update-6'))

    for item in POS_STATES:
        if item[0] == status:
            return item[1]


# The code you must write to solve the exercise
def your_code(process:str):
    print(f"I'm in your_code with a process called {process}")
    

# Your main program
def main():
    status = 1

    while status != 9:
        status_name = lookup(status)
        print("Current Status= ", status_name)
        your_code(status_name)
        status = random.randint(1, 10)
    your_code(lookup(status))


main()



