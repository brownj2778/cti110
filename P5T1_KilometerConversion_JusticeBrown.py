#This program calculates Kilometers to Miles
#4-13-2020
#CTI-110 P5T1_KilometerConverter
#Justice Brown
#
#Global Constants
Conversion_Factor = 0.6214


def main():
    #Get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    #display the distance by calling show_miles.
    show_miles(kilometers)

def show_miles(km):
    #Calculate miles.
    miles = km * Conversion_Factor

    #Display the miles.
    print( km, 'kilometers equals', miles, 'miles.')

#Call the main function
main()
