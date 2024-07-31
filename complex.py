import time
import random
import math

goal = random.randint(1, 21)

attempt = 0

num1 = 0
num2 = 0
result = 0

method1 = 0


print("Goal is", goal)

running = True

while running:
    attempt += 1
    for i in range(random.randint(1, 300)):
        num1 = random.randint(1, 1000)
        
    for i in range(random.randint(1, 300)):
        num2 = random.randint(1, 1000)
        
    

    for x in range(random.randint(1, 400)):
        method = random.randint(1, 2)
    if method == 1:
        result = num2 - num1
        print("Attempt: ", attempt, "Numbers: ", num1, " ", num2, "with result of", result, "and a method of", method)
        if result == goal:
                print("Goal of: ", goal, "has been reached in ", attempt, "tries")
                running = False
                
    if method == 2:
        
        print("Attempt: ", attempt, "Numbers: ", num1, " ", num2, "with result of", result, "and a method of", method)
        if result == goal:
            print("Goal of: ", goal, "has been reached in ", attempt, "tries")
            running = False
        
        