#Project utilizing variables, operands and operators
#2-17-2020
#CTI-110 P2T1 - Sales Prediction
#Justice Brown
#
#declare sales percentage variable
salesPercentage = .23
#gather sales figure
totalSales = int(input('Enter the total number of sales '))
Profit = salesPercentage * totalSales
#display profit
print('Expected profit is $', Profit, sep='')
