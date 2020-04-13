#Program is designed to get a number of feet from the user and display it in inches.
#4-13-2020
#CTI-110 P5T2_FeetToInches
#Justice Brown
#

#Global Constants
Inch_to_Feet = 12

#structure main function
def main():
    #Get number if feet to be converted
    feet = float(input('Eneter the number of feet you want to convert to inches: '))

    #call the show_inch() module
    show_inch(feet)

#structure show_inch
def show_inch(ft):

    #Calculate inches
    inches = ft * Inch_to_Feet

    #Display calculation
    print(ft, 'feet equals', inches, 'inches.')

#call main
main()
