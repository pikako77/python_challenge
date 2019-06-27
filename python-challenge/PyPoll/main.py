# Main for PyPoll

import os
import csv

####
# Functions

# get length of data 
def get_length(var):
    return len(var)

# get candidate names
def get_candidate_name(candidate_name):
    name_list=[]

    # sort name in aphbetically
    sort_candidate_list = (sorted(candidate_name))

    name_list.append(sort_candidate_list[0])
    for i in range(len(candidate_name)-1):
        if (sort_candidate_list[i] != sort_candidate_list[i+1]):
            name_list.append(sort_candidate_list[i+1])

    #print(name_list)
    return (name_list)

# function to calculate percentage
def calc_perc(var, total):
    return (var*100/total)

# get index of max value
def get_max_index(var):

    max_val = max(var)

    for i in range(len(var)):
        if ( max_val == var[i] ):
            idx = i

    #print(idx)
    return idx

# print to terminal
def print_to_terminal(name, total, count, count_perc, max_idx):
    print("Election Results\n")
    print("------------------------")
    print ("Total vote: %i \n" %(total) )
    print("------------------------")
    print(count)
    #for i in range(len(name)):




###
# Variables
voter_ID =[]   
county = []
candidate =[]
candidate_list =[]  # kist of candidates
count_vote = []
count_perc =[]
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

# total_candidate = get_number_of_candidate(candidate)
candidate_list = get_candidate_name(candidate)

# count vote and their percentage for each candidates
for i in range(len(candidate_list)):
    count_vote.append(candidate.count(candidate_list[i]))
    count_perc.append(calc_perc(count_vote[i], total_vote))

# get the index of the vote winner
winner_index = get_max_index(count_vote)

print_to_terminal(candidate_list,total_vote,count_vote,count_perc,winner_index)

# print(total_candidate)
# print(candidate_list)
# print(count_vote)
# print(count_perc)
# print(candidate_list[winner_index])
# print(header)
# print(f"voter_id: {voter_ID[0:10]}\n\n")
# print(f"county: {county[0:10]}\n\n")
# print(f"candidate: {candidate[0:10]}\n\n")