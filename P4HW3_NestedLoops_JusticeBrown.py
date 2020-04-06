#Using nested loops to display a pattern
#4-6-2020
#CTI-110 P4HW3 - Nested Loops
#Justice Brown
#

#Decide num of steps in pattern
#Decide number of rows
#Print pattern

num_steps = 6

for row in range(6):
    print('#', end='', sep='')
    for spaces in range(row):
        print(' ', end='', sep='')
    print('#', sep='')
          
