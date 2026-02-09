import random
import copy

letters = ["A", "B", "C", "D", "E"]
numbers = ["1", "2", "3", "4", "5"]
battle_array = [[0 for x in range(5)] for x in range(5)]

def pick(battle):
    while True:
        letter = random.randint(0,4)
        number = random.randint(0,4)
        if battle[letter][number] != 1:
            battle[letter][number] = 1
            print(f"Selected square: {letters[letter]}{numbers[number]}\n")
            return battle

def setup():
    return copy.deepcopy(battle_array), 1    

def gameover(battle):
    for x in battle:
        if 0 in x:
            return False
    return True

def main():
    battle, count = setup()
    print("Press Enter for a tile, type r to reset.")
    while True:
        print(f"Turn {count}", end="")
        inp = input()
        if inp == "":
            battle = pick(battle)
            count += 1
        elif inp == "r":
            battle, count = setup() 
        else:
            print("Invalid input.")
        if gameover(battle):
            print("Game Over")
            battle, count = setup()
 
if __name__ == "__main__":
    main()