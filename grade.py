# Asking users for their score 
score = int(input("Whats your score? "))

# Giving a grade to all scores 
if score >= 90 :
    print("Grade: A")
elif score >= 80 :
    print("Grade B")
elif score >= 70 :
    print("Grade c")
elif score >= 60:
    print("Grade D")
elif score >= 50 :
    print("Grade E")
elif score >= 0 :
    print("Grade F")
else :
    score = int(input("Please choose a number from 0-100 "))
