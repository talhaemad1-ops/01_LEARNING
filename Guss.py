import random
number = random.randint(1, 10)

while True:
    guss = input("guss what's the number between 1 and 10: ")
    if number > int(guss):
        print("more! ")

    elif number < int(guss):
        print("less! ")

    else:
        print("Correct!")
        break

