import os
import csv


tot_votes = 0

#Lists
id_lst = []
country_lst = []
candidate_list = []

csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

    for row in csv_reader:

        tot_votes += 1
        id_lst.append(str(row[0]))
        candidate_list.append(str(row[2]))

khanTot = candidate_list.count("Khan")
correyTot = candidate_list.count("Correy")
liTot = candidate_list.count("Li")
oToolTot = candidate_list.count("O'Tooley")

print("Total Votes: " + str(tot_votes))
print("Khan: " + str(format(round((khanTot/tot_votes)*100),'.3f')) + "% " + "(" + str(khanTot) + ")")
print("Correy: " + str(format(round((correyTot/tot_votes)*100),'.3f')) + "% " + "(" + str(correyTot) + ")")
print("Li: " + str(format(round((liTot/tot_votes)*100),'.3f')) + "% " + "(" + str(liTot) + ")")
print("O'Tooley: " + str(format(round((oToolTot/tot_votes)*100),'.3f')) + "% " + "(" + str(oToolTot) + ")")
if khanTot > correyTot and khanTot > liTot and khanTot > oToolTot:
    print("Winner: Khan")
elif correyTot > khanTot and correyTot > liTot and correyTot > oToolTot:
    print("Winner: Correy")
elif liTot > khanTot and liTot > correyTot and correyTot > oToolTot:
    print("Winner: Li")
elif oToolTot > khanTot and oToolTot > correyTot and oToolTot > liTot:
    print("Winner: O'Tooley")


# Specify the file to write to
output_file = os.path.join("PyPoll", "Analysis", "poll_data.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_file, 'w') as txtfile:

    #write each data point to an individual line in the text file
    txtfile.write("Total Votes: " + str(tot_votes) + "\n")
    txtfile.write("Khan: " + str(format(round((khanTot/tot_votes)*100),'.3f')) + "% " + "(" + str(khanTot) + ")" + "\n")
    txtfile.write("Correy: " + str(format(round((correyTot/tot_votes)*100),'.3f')) + "% " + "(" + str(correyTot) + ")" + "\n")
    txtfile.write("Li: " + str(format(round((liTot/tot_votes)*100),'.3f')) + "% " + "(" + str(liTot) + ")" + "\n")
    txtfile.write("O'Tooley: " + str(format(round((oToolTot/tot_votes)*100),'.3f')) + "% " + "(" + str(oToolTot) + ")" + "\n")
    if khanTot > correyTot and khanTot > liTot and khanTot > oToolTot:
        txtfile.write("Winner: Khan")
    elif correyTot > khanTot and correyTot > liTot and correyTot > oToolTot:
        txtfile.write("Winner: Correy")
    elif liTot > khanTot and liTot > correyTot and correyTot > oToolTot:
        txtfile.write("Winner: Li")
    elif oToolTot > khanTot and oToolTot > correyTot and oToolTot > liTot:
        txtfile.write("Winner: O'Tooley")

    txtfile.close()