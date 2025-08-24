import random

# input level

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
        else:
            pass
    except (ValueError, TypeError, IndexError):
        pass
# if not a positive integer, prompt user again

# generate a random number [1,n]
answer = random.randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess == answer:
                print("Just right!")
                break
            elif guess < answer:
                print("Too small!")
                continue
            elif guess > answer:
                print("Too large!")
                continue
        else:
            pass
    except ValueError:
        pass
# check if not positive integer
# check if smaller or larger than the integer "Too small!" or "Too large!"
# if same, output Just right! and exit.
