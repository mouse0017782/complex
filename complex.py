import time
import random
import math

goal = random.randint(1, 21)

attempt = 0

num1 = 0
num2 = 0
num3 = 0
result = 0
list = [num1, num2, num3]

method1 = 0


print("Goal is", goal)

running = True

while running:
    attempt += 1
    for i in range(random.randint(1, 300)):
        num1 = random.randint(1, 100)
        
    for i in range(random.randint(1, 300)):
        num2 = random.randint(1, 100)
        
    for i in range(random.randint(1, 300)):
        num3 = random.randint(1, 100)
    print("Attempt: ", attempt, "Numbers: ", num1, " ", num2, " ", num3)

    for x in range(random.randint(1, 400)):
        method = random.randint(1, 2)
    if method == 1:
        x = list[random.randint(0, 2)]
        y = list[random.randint(0, 2)]
        result = x - y
        
        if result == goal:
                print("Goal of: ", goal, "has been reached in ", attempt, "tries")
                running = false
                
    if method == 2:
        x = list[random.randint(0, 2)]
        y = list[random.randint(0, 2)]
        result = x + y
        
        if result == goal:
            print("Goal of: ", goal, "has been reached in ", attempt, "tries")
            running = false
        
        