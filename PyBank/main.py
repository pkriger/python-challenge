import os
import csv

current_directory=os.path.dirname(os.path.abspath(__file__))
budget_path= os.path.join(current_directory,"Resources","budget_data.csv")

with open (budget_path, 'r') as budget_file:
    csvreader = csv.reader (budget_file, delimiter = ",")

    #skip header
    headerline = next(csvreader)

    #define variables
    months = 0
    total_PL = 0
    change = 0
    increase = 0
    decrease = 0
    prior_value= 0

    #loop through file to count
    for row in csvreader:
        curr_value = int(row[1])
        change = (curr_value - prior_value)
        #Total number of months (1/5)
        months+= 1
        # The net total amount of "Profit/Losses" over the entire period (2/5)
        total_PL += int(row[1])
        #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes (3/5)
        if months == 1:
            initial_value = int((row)[1])
        #The greatest increase in profits (date and amount) over the entire period (4/5)
        #The greatest decrease in losses (date and amount) over the entire period (5/5)
        elif change > 0:
            if change > increase:
                increase = change
                increase_mo = (row[0])
        elif change < 0:
            if change < decrease:
                decrease = change
                decrease_mo = (row[0])

        final_value = int(row[1])

        prior_value = int(row[1])
    

row1 = ("Financial Analysis")
row2 = ("----------------------------")
row3 = (f"Total Months: {months}")
row4 = (f"Total: ${total_PL}")
row5 = (f"Average  Change: ${round((final_value-initial_value)/(months-1),2)}")
row6 = (f"Greatest Increase in Profits: {increase_mo} (${increase})")
row7 = (f"Greatest Decrease in Profits: {decrease_mo} (${decrease})")

analysispath= os.path.join(current_directory,"Analysis",'PyBank Summary.txt')
with open (analysispath, 'w') as pybank_sum:

    pybank_sum.write(row1 + '\n')
    pybank_sum.write(row2 + '\n')
    pybank_sum.write(row3 + '\n')
    pybank_sum.write(row4 + '\n')
    pybank_sum.write(row5 + '\n')
    pybank_sum.write(row6 + '\n')
    pybank_sum.write(row7 + '\n')


with open (analysispath, 'r') as pybank_sum:
    for lines in pybank_sum:
        print(lines)

    
