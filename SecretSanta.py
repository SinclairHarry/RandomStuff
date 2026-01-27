from random import randint
import matplotlib.pyplot as plt
import numpy as np

def CreateGroup(size):
    return [x for x in range(size)]
    
def FindRandomPair(not_paired, i):
    random = randint(0,len(not_paired)-1)
    random_person = not_paired[random]

    # Edge case: Last person cannot pair with themselves
    if random_person == i and len(not_paired) == 1:
        return -1
    
    # Normal case
    if random_person != i:
        return random_person
    
    # Retry finding pair when self-selection occurs
    return FindRandomPair(not_paired, i)

def Pairing(group_array):
    paired = []
    not_paired = group_array[:]
    for i in range(len(group_array)):

        # Finding a valid random person
        random_person = FindRandomPair(not_paired, i)

        # Retry entire pairing when last person attempts to pair with themselves
        if random_person == -1:
            return Pairing(group_array)
        
        not_paired.remove(random_person)
        paired.append(random_person)
    return paired

def FindNumberOfGroups(group):
    checked = []
    num_of_groups = 0

    # Counting number of unique cycles in the pairing
    for i in range(len(group)):

        # If person not already checked, start a new cycle
        if i not in checked:
            num_of_groups += 1
            current = i

            # Traverse the cycle until returning to the starting person
            while True:
                checked.append(current)
                current = group[current]
                if current == i:
                    break
    return num_of_groups

def SecretSanta(people, interval):
    ypoints = []
    for i in range(5, people, interval):
        x = Pairing(CreateGroup(i))
        num_of_groups = FindNumberOfGroups(x)
        ypoints.append(num_of_groups)
    return ypoints

def __main__():
    TESTS = 10000
    PEOPLE = 500
    INTERVAL = 25
    ypoints = []
    count = 0
    for i in range(TESTS):
        count += 1
        y = SecretSanta(PEOPLE, INTERVAL)
        ypoints.append(y)
        print(f"Completed: {count}/{TESTS}")
    yavg = list(map(sum, zip(*ypoints)))
    xplot = [x + 5 for x in range(0, PEOPLE - 5, INTERVAL)]
    print(f"xplot: {xplot}\nyavg: {yavg}")
    yplot = np.array(yavg) / TESTS

    plt.scatter(xplot, yplot)
    plt.show()

if __name__ == "__main__":
    __main__()