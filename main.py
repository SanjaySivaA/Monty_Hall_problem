import random

print("This is a simulation of the monty hall problem .....\n")

print("There are three doors and one of them contains a prize.\nYou can choose one of the doors following which one of the\nempty doors is opened.")
print("You can choose to stick with your initial choice or switch.\n\nOn examining switching seems to have a higher probablity of\npicking the door with the prize.\n")
print("Let 'A' denote the event of winning when we did not switch and \nlet 'B' denote the event of winning when we switched")
print("In theory P(A) = 1/6 and P(B) = 1/3 and\nP(A)/P(B) = 0.5 \n")
n = int(input("Enter the number of trials : "))

doors = [0, 1, 2]
without_switch = 0
with_switch = 0

with open('trials.txt','w') as file :
    file.write(f'Trial number   with switch   without switch\n\n')

def simulate_without_switch() :
    if initial_choice == door_with_prize :
        return 1
    return 0

def simulate_with_switch() :
    if initial_choice == door_with_prize :
        return 0 
    else :
        return 1

for i in range(n) :
    door_with_prize = random.randint(0, 2)
    initial_choice = random.randint(0, 2)
    
    without_switch += simulate_without_switch()
    with_switch += simulate_with_switch()

    with open('trials.txt', 'a+') as file :
        file.write(f'     {i+1}               {simulate_with_switch()}                  {simulate_without_switch()}\n')
    

print('\nResult : \n')
print(f' n(A) = {without_switch}      n(B) = {with_switch}\n')
print(f' P(A) = {without_switch/n}    P(B) = {with_switch/n}\n')
print(f' P(A)/P(B) = {without_switch/with_switch}\n')