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
print("Khan: " + str((khanTot/tot_votes)*100) + "% " + "(" + str(khanTot) + ")")
print("Correy: " + str((correyTot/tot_votes)*100) + "% " + "(" + str(correyTot) + ")")
print("Li: " + str((liTot/tot_votes)*100) + "% " + "(" + str(liTot) + ")")
print("O'Tooley: " + str((oToolTot/tot_votes)*100) + "% " + "(" + str(oToolTot) + ")")
if khanTot > correyTot and khanTot > liTot and khanTot > oToolTot:
    print("Winner: Khan")
elif correyTot > khanTot and correyTot > liTot and correyTot > oToolTot:
    print("Winner: Correy")
elif liTot > khanTot and liTot > correyTot and correyTot > oToolTot:
    print("Winner: Li")
elif oToolTot > khanTot and oToolTot > correyTot and oToolTot > liTot:
    print("Winner: O'Tooley")