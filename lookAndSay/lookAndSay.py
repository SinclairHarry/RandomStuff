
def look_and_say(trials, term=None):
    if trials <= 0:
        return
    next = ""
    if term is None:
        next = "1"
        return look_and_say(trials-1, next)
    count = 1
    print(term)
    for i in range(0, len(term)-1):
        if term[i] != term[i+1]:
            next += f"{count}{term[i]}"
            count = 1
        else:
            count += 1 
    next += f"{count}{term[-1]}"
    trials -= 1
    look_and_say(trials, next)

def main():
    trials = 20
    look_and_say(trials)

if __name__ == "__main__":
    main()
