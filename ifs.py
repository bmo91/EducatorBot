phrase = input("Talk to me > ")
if phrase == "hi" or phrase == "hey":
    print("hello")
elif phrase == "whats your name?" or phrase == "What's your name?":
    print("BMO")
elif phrase == "no, don't like you":
    print("Rude")
else:
    print("sorry I dont understand this " + phrase)
print("Bye")

phrase2 = input("How's your day going? > ")
if phrase2 == "good" or phrase2 == "great":
    print("That's Amazing!")
elif phrase2 == "bad" or phrase2 == "awfull":
    print("I'm sorry to hear that :(")
else:
    print("sorry I dont understand this " + phrase2)

phrase3 = input("Would you like to play a game? > ")
if phrase3 == "yes" or phrase3 == "y":
    print("Good! How about calculating the area of a square?" )
    input1 = input ( "How wide is the square in cm? Get me a number. " )
    number1 = int (input1)
    result = number1 * number1
    result_str = str(result)
    print("The area of a square is: " + result_str + " cm2" )
elif phrase3 == "no" or phrase3 == "n":
    print("Alright then. Bye!")
else:
    print("sorry I dont understand this " + phrase3)
