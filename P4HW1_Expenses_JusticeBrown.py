#CTI-110
#P4HW1 - Expenses
#Justice Brown
#3-30-2020

expense = 0
total = 0
count = 0

keepgoing = "y" or "Y"
control = "n" or "N"

account = int(input('Enter starting amount in account. '))
while keepgoing != control:
    count = count + 1

    expense = int(input("Enter expense "))
    total = total + expense

    keepgoing = input("Do you want to enter another expense? (y/n). ")
   
    
else:
    print("Amount in account before expense subtraction is $",account)
    print("Number of expenses entered:", count )
    total = account - total

    print("Amount in account after expenses subtracted is $",total)
            
    
    

    
        
    
    
    

