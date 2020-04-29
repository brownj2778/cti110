#Math Quiz with randomly generated numbers
#4-28-2020
#CTI-110 P5HW2 - Math Quiz
#Justice Brown
#
import random

#Create a list for a user to chose from.
options = ['1) Add Random Numbers', '2) Subtract Random Numbers', '3) Exit']

#Display menu
print('-----Menu-----')
print(*options, sep = '\n')

def main():
    
    selection = input('Enter 1 or 2 to proceed, 3 to Exit this program. ')

    #generate and assign 2 random numbers
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    

    if selection == '1':
        
        #add the two numbers
        add = num1 + num2
        #get user to guess the problem
        add_guess(add, num1, num2)
        main()

    elif selection == '2':
        #subtract the two numbers
        sub = num1 - num2
        #get user to guess the problem
        sub_guess(sub, num1, num2)
        main()

    elif selection == '3':
        print('This program will now terminate.')
#define user guess for use in add_guess and sub_guess
def get_user_guess():
    guess = int(input('Enter your answer. '))
    return guess

#define add_guess
def add_guess(add, num1, num2):
    print('Enter the total of', num1, 'and', num2)
    value = 'y'
    while value == 'y':
        guess = get_user_guess()
        if guess == add:
            print('Congrats, you are correct.')
            value = 'n'

        else:
            print('Try again')

#define sub_guess
def sub_guess(sub, num1, num2):
    print('Enter the remainder of', num1, 'and', num2)
    value = 'y'
    while value == 'y':
        guess = get_user_guess()
        if guess == sub:
            print('Congrats, you are correct.')
            value = 'n'

        else:
            print('Try again')



    
        
    
        
main()
