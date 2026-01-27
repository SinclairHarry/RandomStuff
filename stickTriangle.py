import random

def cut_stick():
    p_1 = random.uniform(0, 1)
    p_2 = random.uniform(0, 1)
    if p_1 < p_2:
        l_1 = p_1
        l_2 = p_2 - p_1
        l_3 = 1 - p_2
    else:
        l_1 = p_2
        l_2 = p_1 - p_2
        l_3 = 1 - p_1
    return l_1, l_2, l_3

def possible_triangle(l_1, l_2, l_3):
    if l_1 + l_2 > l_3 and l_2 + l_3 > l_1 and l_1 + l_3 > l_2:
        return True
    else:
        return False
    
def main():
    ATTEMPTS = 999999
    triangle_count = 0
    for _ in range(ATTEMPTS):
        l_1, l_2, l_3 = cut_stick()
        if possible_triangle(l_1, l_2, l_3):
            triangle_count += 1
    print(f"Triangle Formation Rate: {triangle_count / ATTEMPTS * 100:.2f}%")

if __name__ == "__main__":
    main()