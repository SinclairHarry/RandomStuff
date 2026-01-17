import random

CLOCK = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
TRIALS = 999999

def singlepass():
    passed = set()
    initial = 11
    passed.add(initial)
    while len(passed) < 11:
        if random.randint(0,1):
            initial += 1
            initial %= 12
        else:
            initial -= 1
        if initial < 0:
            initial = 11
        passed.add(initial)
    return CLOCK - passed

def main():
    final_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for _ in range(TRIALS):
        final_array[next(iter(singlepass()))] += 1
    print(final_array)
    for i in range(len(final_array)):
        print(f"{i+1}: {final_array[i]/TRIALS:.4f}")

if __name__ == "__main__":
    main()