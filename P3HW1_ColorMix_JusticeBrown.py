#CTI-110
#P3HW1 - Color Mixer
#Justice Brown
#3-16-2020

#Get two primary colors from user
#Display the results of combining the colors
#If a color choice is not acceptable display an error message

#Get two primary colors.
color1 = input('Enter your first primary color.')
color2 = input('Enter your second primary color.')

#Determine which color choices were made.
if color1 == 'blue' and color2 == "red":
    print('Blue and red make purple.')
elif color1 == 'red' and color2 == 'blue':
    print('Red and blue makes purple.')
elif color1 == 'red' and color2 == 'yellow':
    print('Red and yellow make orange.')
elif color1 == 'yellow' and color2 == 'red':
    print('Yellow and red make orange.')
elif color1 == 'blue' and color2 == 'yellow':
    print('Blue and yellow make green.')
elif color1 == 'yellow' and color2 == 'blue':
    print('Yellow and blue makes green.')
else:
    print('One of the chocies given is not a primary color.')
    
