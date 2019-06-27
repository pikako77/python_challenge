# Main for PyPoll

import os
import csv

####
# Functions

# get length of data 
def get_length(var):
    return len(var)

def get_number_of_candidate(candidate_name):
    count_cadidate = 0

    # sort name in aphbetically
    sort_candidate_list = (sorted(candidate_name))
    
    for i in range(len(candidate_name)-1):
        if (sort_candidate_list[i] != sort_candidate_list[i+1]):
            count_cadidate = count_cadidate+1
 
    print (count_cadidate)


    return count_cadidate


def count_vote(var, name):
    count = 0

    for i in range(len(var)):
        if (name == var[i]):
            count = count +1
    print (count)        
    return count

###
# Variables
voter_ID =[]
county = []
candidate =[]

count = []

total_candidate = 0

# Path to collect data from the Resources folder
# Input data file
election_csv = os.path.join('Resources', 'election_data.csv')



######################################
# Main
#Read data
with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        voter_ID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

total_vote = get_length(voter_ID)
print (total_vote)

total_candidate = get_number_of_candidate(candidate)
# print(header)
# print(f"voter_id: {voter_ID[0:10]}\n\n")
# print(f"county: {county[0:10]}\n\n")
# print(f"candidate: {candidate[0:10]}\n\n")