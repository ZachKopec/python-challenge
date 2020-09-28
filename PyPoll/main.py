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