# Main code for pyBank

import os
import csv

date=[]
profit=[]
line=[]

count_month = 0  # count month
NetProfit   = 0  # NetProfit

# Path to collect data from the Resources folder
# Input data file
budget_csv = os.path.join('Resources', 'budget_data.csv')
output_file = os.path.join('output','budget_out.txt')
#print(output_file)

#------------------------
#  Count the number of months in the data
def get_month_total(var1):
    count_month =1
    
    for i in range(len(var1)-1):
        month1 = var1[i].split('-')[0]
        month2 = var1[i+1].split('-')[0]

        if (month1 != month2): # check if the consecutive months are different
            count_month = count_month +1

    #print(f"count_month: {count_month}") 
    return count_month

# calculate total net profit
def calc_net_total(var1):
    total = 0
    for i in range(len(var1)):
        total = total + float(var1[i])

    #print(total)
    return total

# calculate change
def calc_change(var1):
    change =[]

    for i in range(len(var1)-1):
        change.append(float(var1[i+1])-float(var1[i]))
    
    return change

# calcuate the average
def average(var1):
    total=0
    for i in range(len(var1)):
        total = total + var1[i]
    return (total/(len(var1)))
  
# get index of the greatest increase
def get_max_change_index(var1):

    max_val = max(var1)

    for i in range(len(var1)):
        if ( max_val == var1[i] ):
            idx = i

    #print(idx)
    return idx

# get index of the greatest Decrease
def get_min_change_index(var1):

    min_val = min(var1)

    for i in range(len(var1)):
        if ( min_val == var1[i] ):
            idx = i

    #print(idx)
    return idx



######################################
# Main
#Read data
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        date.append(row[0])
        profit.append(row[1])

# count total months
count_month = get_month_total(date)
print("count_month : %i"% (count_month) )

# calculate the net total Profit/losses
NetProfit= calc_net_total(profit)
print("NetProfit : %i"% (NetProfit))

# calcuate change month-by-month
change = calc_change(profit)

# calculate average change
Average_NetProfit = average(change)
print("Average_NetProfit : %8.2f"% (Average_NetProfit) )

# calculate max increase
max_change_idx = get_max_change_index(change)
print(f"Greatest Increase in Profits : {date[max_change_idx+1]} ($ {change[max_change_idx]})" )

# calculate max decrease = min increase
min_change_idx = get_min_change_index(change)
print(f"Greatest Decrease in Profits : {date[min_change_idx+1]} ($ {change[min_change_idx]})" )

# Output to file
f =open(output_file ,"w+")
f.write("count_month : %i \n"% (count_month) )
f.write("NetProfit : %i\n"% (NetProfit))
f.write("Average_NetProfit : %8.2f\n"% (Average_NetProfit) )
f.write(f"Greatest Increase in Profits : {date[max_change_idx+1]} ($ {change[max_change_idx]})\n" )
f.write(f"Greatest Decrease in Profits : {date[min_change_idx+1]} ($ {change[min_change_idx]})\n" )
f.close()