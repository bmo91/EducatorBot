guess = input("guess my name >")
count = 0
while guess != "BMO":
    guess = input("wrong - guess again >")
    count = count + 1
print("Well done! You've guessed my name " + str(count) + " times before")