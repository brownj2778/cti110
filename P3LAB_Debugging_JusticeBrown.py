#CTI-110
#P3LAB - Debugging
#Justice Brown
#3-23-2020
#
#Gather score
#If score is great than or equal to an A
#Display your grad is an A
#If score is greater than or equal to a B
#Display your grade is a B
#If score is greater than or equal to a C
#Display your grad is a C
#If score is greater or equal to a D
#Display your score is a D
#Else display your grade is a F

if score >= A_score:
    print('Your grade is A.')
else:
    if score >= B_score:
        print('Your grade is B.')
    else:
        if score >= C_score:
            print('Your grade is C.')
        else:
            if score >= D_score:
                print('Your grade is D.')
            else:
                print('Your grade is F.')
