#Areas of a rectangle
#3/11/2020
#CTI-110 P3T1- Areas of a triangle
#Justice Brown

#Input the lentgh and width of rectangle 1
#Input the lentgh and width of rectangle 2
#Calculate the area of rectangle 1
#Calculate the area of rectangle 2
#if area1>area2
    #Display "Rectangle 1 has the greatest area."
#else if area2>area1
    #Display "Rectangle 2 has the greatest area."
#else
    #Display "Both Rectangles have the same area."

#Gather dimensions of rectangle 1
length1 = int(input('Enter the length of rectangle 1.'))
width1 = int(input('Enter the width of rectangle 1.'))

#Gather the dimensions of rectangle 2
length2 = int(input('Enter the length of rectangle 2.'))
width2 = int(input('Enter the width of recatangle 2.'))

#Calculate the area
area1 = length1 * width1
area2 = length2 * width2

#Display the largest rectangle
if area1 > area2:
    print('Rectangle 1 has the largest area.')
elif area2 > area1:
    print('Rectangle 2 has the largest area.')
else:
    print('Bothe rectangles have the same area,')

