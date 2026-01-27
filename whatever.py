import random

def __main__():
    number = random.randint(1, 5)
    try:
        guess = int(input("Guess the number 1-5: "))
    except ValueError:
        print("Please enter a valid integer.")
        return
    if guess == number:
        print("Good boy~~")
    else:
        print("Fuck you.")
    
if __name__ == "__main__":
    __main__()