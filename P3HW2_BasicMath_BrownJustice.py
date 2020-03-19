#CTI-110
#P3HW2 - Basic Math
#Justice Brown
#3-16-2020
#
#Input 2 numbers
#Display a menu with options to 1)add, 2)multiply, 3)subtract or 4)exit
#Gather selction and perform intended operation
#If user enters 1: Display the sum of the two numbers
#If users enters 2: Multiply the numbers and display the result
#If user enters 3: Subtract the two numbers and display the result
#If user enters 4: Display a message that tells the user the program will terminate
#If user enters a number not listed in the options: Display an error messeage and tell the user to an incorrect choice has been entered

#Input two numbers
number1 = int(input("Enter your first number."))
number2 = int(input("Enter you second number."))

#Display a menu of options
options = ["1)Add Numbers", "2)Multiply Numbers", "3)Subtract Numbers", "4)Exit"]
print("----Menu----")
print(*options, sep = "\n")

#Gather selction and perform intended action
selection = int(input("Enter a menu option "))


#Display results
if selection == 1:
    print('The sum of the two numbers is', (number1 + number2))
elif selection == 2:
    print('The results of multiplying the numbers is', (number1 * number2))
elif selection == 3:
    print('The results of subtracting the numbers is', (number1 - number2))
elif selection == 4:
    print('The program will now terminate')
else:
    print('ERROR! An incorrect chocie has been entered.')
    
