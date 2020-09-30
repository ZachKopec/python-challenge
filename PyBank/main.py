import os
import csv

#Needed variables
mth_count = 1

#Needed Lists
mth = []
rev = []
avg_chng = []

#file path
csvpath = os.path.join('PyBank','Resources','budget_data.csv')

#when code is run: open file 
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #
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
        
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(mth_count))
print("Total: " + str(sum(rev)))
print("Average Change: " + str(round(sum(avg_chng)/(mth_count-1),2)))
print("Greatest Increase in Profits: " + str(mth[avg_chng.index(max(avg_chng))+1]) + " ($" + str(max(avg_chng)) + ")")
print("Greatest Decrease in Profits: " + str(mth[avg_chng.index(min(avg_chng))+1]) + " ($" + str(min(avg_chng)) + ")")


# Specify the file to write to
output_file = os.path.join("PyBank", "Analysis", "budget_data.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_file, 'w') as txtfile:

    #write each data point to an individual line in the text file
    txtfile.write("Financial Analysis" + "\n")
    txtfile.write("----------------------------" + "\n")
    txtfile.write("Total Months: " + str(mth_count) + "\n")
    txtfile.write("Total: " + str(sum(rev)) + "\n")
    txtfile.write("Average Change: " + str(round(sum(avg_chng)/(mth_count-1),2)) + "\n")
    txtfile.write("Greatest Increase in Profits: " + str(mth[avg_chng.index(max(avg_chng))+1]) + " $" + str(max(avg_chng)) + "\n")
    txtfile.write("Greatest Deacrease in Profits: " + str(mth[avg_chng.index(min(avg_chng))+1]) + " $" + str(min(avg_chng)) + "\n")

    txtfile.close()


    

