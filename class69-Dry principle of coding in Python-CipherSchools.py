import random
winning_no = random.randint(1, 100)
number = int(input("guess the number betwwen 1 to 100:"))
guess = 1
game_over = False
while not game_over:
    if number == winning_no :
        print(f"You Won, and you guessed this number in {guess} times")
        game_over = True

    else:
        if number < winning_no:
            print("too low")
        else:
            print("too high")
    guess+=1
    number = int(input("guess again:"))
