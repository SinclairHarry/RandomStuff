import random

bonnie_ai = 12
chica_ai = 12
opportunities = 47

def Chance(ai):
    return random.randint(1,20) <= ai

def Movement(pos):
    if pos == 0:            # At Middle
        return 1            # Move to Hall
    elif pos == 1:          # At Hall
        if random.randint(0,1):
            return -1       # Move to Attack
    return 0                # Move to Middle

def Night():
    b_pos = 0  # Starting at middle
    c_pos = 0  
    for _ in range(opportunities):
        if Chance(bonnie_ai):
            b_pos = Movement(b_pos)
        #if Chance(chica_ai):
        #    c_pos = Movement(c_pos)
        if b_pos == -1 or c_pos == -1:
            return False
    return True

def UntilComplete():
    complete = False
    count = 0
    while not complete:
        count += 1
        complete = Night()
    return count

def main():
    count = 0
    time = 0
    while True:
        count += 1
        time += UntilComplete()
        print(f"Avg: {time/count:.2f} Trials: {count}")


if __name__ == "__main__":
    main()