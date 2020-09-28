import os
import csv

#Lists
id_lst = []
country_lst = []
candidate_list = []

csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")


