import os
import csv

#Needed variables
tot_votes = 0

#Needed Lists
id_lst = []
country_lst = []
candidate_list = []

#file path
csvpath = os.path.join('PyPoll','Resources','election_data.csv')

#when code is run: open file 
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    #initialize header row
    csv_header = next(csv_reader)

    #loop through every row in csv file
    for row in csv_reader:

        #increment the vote count by 1 for every non-header row in data set
        tot_votes += 1
        #append lists in every iteration to benchmark data points
        id_lst.append(str(row[0]))
        candidate_list.append(str(row[2]))

#store a count of each candidate's list to determine vote totals
khanTot = candidate_list.count("Khan")
correyTot = candidate_list.count("Correy")
liTot = candidate_list.count("Li")
oToolTot = candidate_list.count("O'Tooley")

#print required text & analysis to the terminal 
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(tot_votes))
print("-------------------------")
print("Khan: " + str(format(round((khanTot/tot_votes)*100),'.3f')) + "% " + "(" + str(khanTot) + ")")
print("Correy: " + str(format(round((correyTot/tot_votes)*100),'.3f')) + "% " + "(" + str(correyTot) + ")")
print("Li: " + str(format(round((liTot/tot_votes)*100),'.3f')) + "% " + "(" + str(liTot) + ")")
print("O'Tooley: " + str(format(round((oToolTot/tot_votes)*100),'.3f')) + "% " + "(" + str(oToolTot) + ")")
print("-------------------------")
#conditional to print winner's name
if khanTot > correyTot and khanTot > liTot and khanTot > oToolTot:
    print("Winner: Khan")
elif correyTot > khanTot and correyTot > liTot and correyTot > oToolTot:
    print("Winner: Correy")
elif liTot > khanTot and liTot > correyTot and correyTot > oToolTot:
    print("Winner: Li")
elif oToolTot > khanTot and oToolTot > correyTot and oToolTot > liTot:
    print("Winner: O'Tooley")
print("-------------------------")

# Specify the file to write to
output_file = os.path.join("PyPoll", "Analysis", "poll_data.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_file, 'w') as txtfile:

    #write each data point to an individual line in the text file
    txtfile.write("Election Results" + "\n")
    txtfile.write("-------------------------" + "\n")
    txtfile.write("Total Votes: " + str(tot_votes) + "\n")
    txtfile.write("-------------------------" + "\n")
    txtfile.write("Khan: " + str(format(round((khanTot/tot_votes)*100),'.3f')) + "% " + "(" + str(khanTot) + ")" + "\n")
    txtfile.write("Correy: " + str(format(round((correyTot/tot_votes)*100),'.3f')) + "% " + "(" + str(correyTot) + ")" + "\n")
    txtfile.write("Li: " + str(format(round((liTot/tot_votes)*100),'.3f')) + "% " + "(" + str(liTot) + ")" + "\n")
    txtfile.write("O'Tooley: " + str(format(round((oToolTot/tot_votes)*100),'.3f')) + "% " + "(" + str(oToolTot) + ")" + "\n")
    txtfile.write("-------------------------" + "\n")
    if khanTot > correyTot and khanTot > liTot and khanTot > oToolTot:
        txtfile.write("Winner: Khan" + "\n")
    elif correyTot > khanTot and correyTot > liTot and correyTot > oToolTot:
        txtfile.write("Winner: Correy" + "\n")
    elif liTot > khanTot and liTot > correyTot and correyTot > oToolTot:
        txtfile.write("Winner: Li" + "\n")
    elif oToolTot > khanTot and oToolTot > correyTot and oToolTot > liTot:
        txtfile.write("Winner: O'Tooley" + "\n")
    txtfile.write("-------------------------" + "\n")

    txtfile.close()