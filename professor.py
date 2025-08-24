import random
global x
global y

def main():
    score = None
    get_level()

    for arg in range(10):

        generate_integer(get_level)
        answer = x + y

        for attempt in range(3):
            attempt = input(f"{x} + {y} = ")
            if attempt != answer:
                print("EEE")
                pass
            elif attempt == answer:
                score =+ 1
                break
        print(f"{x} + {y} = {answer}")
        continue

    print("Score: ", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                break
            else:
                pass
        except ValueError:
            pass


def generate_integer(level):
    x = None
    y = None
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        return x and y
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        return x and y
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
        return x and y
    return None

if __name__ == "__main__":
    main()

# Prompts the user for a level, 𝑛.
# If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = ,
# wherein each of X and Y is a non-negative integer with 𝑛 digits.
"""
 The order in which you generate x and y matters. 
 Your program should generate random numbers in x, y pairs to simulate generating 
 one math question at a time (e.g., x0 with y0, x1 with y1, and so on).
 
No need to support operations other than addition (+).
"""
