#Totol # of months included in the dataset
#The net total amount of "profit/loss" over the entire period
#Average change in "profit/loss" over the entire period
#The greatest increase in profts(date and amount) over the entire period
#The greatest decrease in losse(date and amount) over the entire period
#Your final script should both print the analysis to the terminal AND
#Export a text file with the results


import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #reading the header row(and skipping)
    csvheader = next(csvreader)

    Value = 0    
    TotalMonths = 0
    change = 0
    revenue = []
    profits = []
    dates = []

    for row in csvreader:
        TotalMonths = TotalMonths + 1
        dates.append(row[0])
        revenue.append(row[1])

        change = int(row[1])-Value
        profits.append(change)


    revenueInt = map(int,revenue)
    TotalRevenue = (sum(revenueInt))
    AverageChange = (TotalRevenue / TotalMonths)

    GreatestIncrease = max(profits)
    Greatestindex = profits.index(GreatestIncrease)
    GreatestDate = dates[Greatestindex]

    GreatestDecrease = min(profits)
    LowestIndex = profits.index(GreatestDecrease)
    LowestDate = dates[LowestIndex]





print("Financial Analysis")
print("---------------------------------")
print("Total Months:",TotalMonths)
print("NetTotal: $" + str(TotalRevenue))
print("Average Change: $" + str(AverageChange))
print(f"Greatest Increase in Profits: {GreatestDate} (${str(GreatestIncrease)})")
print(f"Greatest Decrease in Profits: {LowestDate} (${str(GreatestDecrease)})")

filename = "analysis.txt"
f = open("Analysis/Analysis.txt", "w" )
f.write("Financial Analysis")
f.write('\n')
f.write("---------------------------------")
f.write('\n')
f.write("Total Months:" + str(TotalMonths))
f.write('\n')
f.write("NetTotal: $" + str(TotalRevenue))
f.write('\n')
f.write("Average Change: $" + str(AverageChange))
f.write('\n')
f.write(f"Greatest Increase in Profits: {GreatestDate} (${str(GreatestIncrease)})")
f.write('\n')
f.write(f"Greatest Decrease in Profits: {LowestDate} (${str(GreatestDecrease)})")