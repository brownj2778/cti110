#A random number gussing game.
#4-28-2020
#CTI-110 Random Number
#Justice Brown
#
import random

#A random number gussing game.
#4-28-2020
#CTI-110 Random Number
#Justice Brown
#
import random

#Create a list for a user to chose from.
options = ['1) Play Game', '2) Exit']

#Display menu
print('-----Menu-----')
print(*options, sep = '\n')

def main():
   choice = input('Enter menu option. ')
   if choice == '1':
      #Generate random number
      number = random.randint(1, 100)
      print(number)

      #get user guess
      
      
      #Compare the two numbers
      compare_guess( number)
      
      

      print( number)

   elif choice == '2':
      print('This program will terminate.')
      
#define get_user_guess
def get_user_guess():
   guess = int(input('Enter your guess '))
   return guess

#define compare guess.
def compare_guess( number):
    value = 'y'
    while value == 'y':
        guess = get_user_guess()
        if guess == number:
            print('Awsome, you guessed correctly!')
            value = 'n'

        elif guess > number:
            print('The number is too high try a lower number')

        else: 
            print('The number is too low, try a bigger number.')
      

     

      
      
   
main()      




        
            
           
                  
        



