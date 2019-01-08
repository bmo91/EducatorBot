def do_calculation():
    print("lets " + command + " some numbers")
    input1 = input("Number 1>")
    input2 = input("Number 2>")
    number1 = int(input1)
    number2 = int(input2)
    if command == "add":
        result = number1 + number2
    elif command == "subtract":
        result = number1 - number2
    output = str(result)
    if command == "add":
        print(input1 + " + " + input2 + " = " + output)
    elif command == "subtract":
        print(input1 + " - " + input2 + " = " + output)

finished = False
while finished == False:
    print("Hi, I am BMO, your personal bot.")
    command = input("How can I help? ")
    if command == "add":
        do_calculation()
    elif command == "subtract":
        do_calculation()
    elif command == "divide":
        print("Divided we fall...")
        input3 = input("Number 1> ")
        input4 = input("Number 2> ")
        number3 = int(input3)
        number4 = int(input4)
        result2 = number3 / number4
        output = str(result2)
        print(input3 + " : " + input4  + " = " + output)
    elif command == "square":
        print("Square Up!" )
        input8 = input ( "How wide is the square in cm? Get me a number. " )
        number8 = int (input8)
        result4 = number8 * number8
        result_str = str(result4)
        print("The area of a square is: " + result_str + " cm2" )
    elif command == "average":
        print("You're above Average")
        how_many = input("How many numbers> ")
        how_many = int(how_many)
        total = 0
        for number_count in range(how_many):
            number = input("Enter number " + str(number_count) + "> ")
            total = total + int(number)
        result = total / how_many
        print("the average = " + str(result))
    elif command == "shopping":
        print("Get in the car loser! We're going shopping")
        shopping = []
        how_many = input("how many items of shopping do you have? ")
        how_many = int(how_many)
        for item_number in range(how_many):
            item = input("what is item number " + str(item_number  + 1) + "? ")
            shopping.append(item)
        for item in shopping: 
            print(item)
        print("you have " + str(len(shopping)) + " different products in your bascet")
    elif command == "total":
        print("Totally!" )
        input9 = input ( "How many numbers? > " )
        number9 = int (input9)
        result5 = number9 * number9
        result_str = str(result5)
        print("The area of a square is: " + result_str + " cm2" )

    elif command == "bye":
        finished = True
    else:
        print("sorry I don't understand")
