import random

DAYS_PER_YEAR = 365
PEOPLE = 23
SIMS = 99999

def Theoretical():
    prob: int = 1
    for pair in range(1,PEOPLE):
        prob *= (365-pair)/365
    print(f"Theoretical: {(1-prob)*100:.2f}%")
            
def Simulation():
    count = 0
    for _ in range(1,SIMS):
        birthdays = []
        for _ in range(0,PEOPLE):
            day = random.randint(1,365)
            if day in birthdays:
                #print(birthdays,day)
                count+=1
                break
            birthdays.append(day)
    print(f"Simulated: {count/SIMS*100:.2f}%")


def main():
    Theoretical()
    Simulation()


if __name__ == "__main__":
    main()
