import random

CHAMBER = [0, 0, 0, 0, 0, 0]
ATTEMPTS = 99999


def reload():
    gun = CHAMBER.copy()
    bullet_position = random.randint(0, 5)
    gun[bullet_position] = 1
    return gun


def russian_roulette():
    gun = reload()
    while True:
        if gun[0] == 1:
            return len(gun)
        else:
            gun.pop(0)


def monty_hall():
    gun = reload()
    choice = random.randint(0, 5)
    possible_open = [i for i in range(6) if i != choice and gun[i] == 0]
    chambers_shown = random.sample(possible_open, 4)
    new_choice = [i for i in range(6) if i != choice and i not in chambers_shown][0]
    if gun[new_choice] == 1:
        return True
    else:
        return False


def main():
    #  hit_array = [0, 0, 0, 0, 0, 0]
    #  for _ in range(ATTEMPTS):
    #      hit_array[russian_roulette() - 1] += 1
    #  print(hit_array)
    hit_count = 0
    for _ in range(ATTEMPTS):
        if monty_hall():
            hit_count += 1
    print(f"Shot Rate: {hit_count / ATTEMPTS * 100:.2f}%")

if __name__ == "__main__":
    main()
