#Retrieve a running total of bugs collected over 7 days and display the total.
#3-31-2020
#CTI-110 P4T2 - Bug Collector
#Justice Brown
#
total = 0
for day in range(1, 8):
    print('Enter the bugs collected on day', day)
    bugs = int(input())
    total = total + bugs

print('You collected a total of', total, 'bugs.')
