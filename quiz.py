# Greeting:
print("welcome to my computer quiz")

playing = input("Do you want to play? ").capitalize()
if playing != "Yes":
    quit()

print("okay let's play :)")

score = 0
answer = input("what dose CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what dose GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what dose RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what dose PSU stand for? ").lower()
if answer == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("your score is " + str(score))
