print("Vänligen skriv tre heltal:")
number1 = int(input("Tal 1: "))
number2 = int(input("Tal 2: "))
number3 = int(input("Tal 3: "))
sum = number1 + number2 + number3


#sortering i nummerordning
if (number1 >= number2) and (number1 >= number3):
    largest_number = number1
    if (number2 >= number3):    #1,2,3
        second_largest_number = number2
    elif (number3 > number2):   #1,3,2
        second_largest_number = number3
elif(number2 >= number1) and (number2 >= number3):
    largest_number = number2
    if (number1 >= number3):    #2,1,3
          second_largest_number = number1
    elif (number3 > number1):    # 2,3,1
        second_largest_number = number3
elif(number3 >= number1) and (number3 >= number2):
    largest_number = number3
    if (number1 >= number2):    #3,1,2                                        print("Detta tal är störst: ", largest_number)
        second_largest_number = number1
    elif (number2 > number1):    # 3,2,1
        second_largest_number = number2
else:
    print("nåt gick fel!")


#finns det nummer som är lika?
if (number1 == number2 == number3):
    are_three_numbers_same = True
    are_two_numbers_same = True
else:
    are_three_numbers_same = False
    if (number1 == number2):
        are_two_numbers_same = True
    elif (number1 == number3):
         are_two_numbers_same = True
    elif (number2 == number3):
         are_two_numbers_same = True
    else:
        are_two_numbers_same = False


print("Summan av talen blir:", sum)
print("Största talet är:", largest_number)
print("mittentalet är :", second_largest_number)
if are_two_numbers_same:
    print("Det finns två nummer som är lika")
    if are_three_numbers_same:
        print("Det finns tre nummer som är lika")
else:
    print("Inga nummer är lika")
