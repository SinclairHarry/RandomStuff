import random

def GenerateChild():
    return random.randint(1,14)

def main():
    trials = 1000000
    count = 0
    while trials:
        a = GenerateChild()
        b = GenerateChild()
        if a == 2:
            count += (b <= 7)
        elif b == 2:
            count += (a <= 7)
        else:
            continue
        if count%10000 == 0:
            print(f"count: {count}")
        trials -= 1
    print(f"Total%: {count/1000000*100:.2f}")

if __name__ == "__main__":
    main()
