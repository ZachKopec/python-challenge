import os
import csv

#Needed variables
mth_count = 1

#Lists
mth = []
rev = []
avg_chng = []

csvpath = os.path.join('Resources','budget_data.csv')


with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csv_reader)
    first_row = next(csv_reader)
    row_prior = (int(first_row[1]))

    rev.append(int(first_row[1]))
    mth_chng = int(row_prior)
    mth.append(first_row[0])

    #loop through every row in csv file
    for row in csv_reader:
        #increment the month count by 1 for every non-header row in data set
        mth_count += 1
        #append lists in every iteration to benchmark data points
        rev.append(int(row[1]))
        avg_chng.append(int(row[1])-mth_chng)
        mth.append(row[0])
        #store current row's profit/loss value as variable at the end of the loop to preserve value for the next row's monthly change
        mth_chng = int(row[1])
        

print("Total Months: " + str(mth_count))
print("Total: " + str(sum(rev)))
print("Average Change: " + str(sum(avg_chng)/(mth_count-1)))
print("Greatest Increase in Profits: " + str(mth[avg_chng.index(max(avg_chng))+1]) + " $" + str(max(avg_chng)))
print("Greatest Increase in Profits: " + str(mth[avg_chng.index(min(avg_chng))+1]) + " $" + str(min(avg_chng)))



    
