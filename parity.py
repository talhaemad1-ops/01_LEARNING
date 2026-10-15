def parity():
    number = int(input("Choose a number "))

    if is_even(number):
        print("Even")
    else:
        print("Odd")

def is_even(n):
   return True if n % 2 == 0 else False

parity()