shopping = []

how_many = input("how many items of shopping do you have? ")
how_many = int(how_many)

for item_number in range(how_many):
    item = input("what is item number " + str(item_number  + 1) + "? ")
    shopping.append(item)

for item in shopping: 
    print(item)

print("you have " + str(len(shopping)) + " different products in your bascet")
