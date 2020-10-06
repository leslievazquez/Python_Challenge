# Financial Analysis 

# Create a Python script that analyzes the records to calculate:
# a) Total number of months included in the dataset
# b) The net total amount of "profit/losses" over the entire period
# c) The average of the changes in "profit/losses" over the entire period
# d) The greatest increase in profits (date and amount) over the entire period
# e) The greatest decrease in losses (date and amount) over the entire period 
# f) The final script should print the analysis to the terminal and export a text file with the results.

# Import modules
import os 
import csv

# Set cvs path (directory - folder of the cvs file, file_name including file extension)
csv_path = os.path.join('Resources', 'budget_data.csv')

# Define main function
def pybank(data):

    # Define variables
    tot_months = 0 
    net_amt = 0 
    avg_changes = 0.0 
    change = 0
    max_profit = ['', 0]
    min_losses = ['', 0]
    # Two lists 
    date_list = []
    net_list = []

# Begin the loop with for
    for row in data:
        tot_months += 1
        net_amt += float(row[1])
        # Add each month to the date_list
        date_list.append(str(row[0]))
        # Calculate month to month changes in profit
        if change != 0:
            net_amt = int(row[1])
            change = net_amt - change
            # Add change value to the net_list
            net_list.append(change)
            # Reset the change value to the value in the current cell
            change = int(row[1])
             
        elif change == 0:
            change = int(row[1])  
            # Remove the first month from date_list since no change occurs
            date_list.pop(0)
            
    # Find the index position of the greatest increase in profits
    indxmax = net_list.index(max(net_list))
            
    # Find the index position of the greatest decrease in losses
    indxmin = net_list.index(min(net_list))
            
    # Use index positions to find the month that corresponds with max and min values from the net_list 
    max_profit = (date_list[int(indxmax)], max(net_list))
    min_losses = (date_list[int(indxmin)], min(net_list))
   
    # Calculate the average of the net_list (Profit/Losses)
    avg_changes = sum(net_list)/float(len(net_list))
    avg_changes = round(avg_changes,2)
       
    # Print the results
    print(f'Financial Analysis')
    print(f'-------------------------------------------')
    print(f'Total Months: {tot_months}')
    print(f'Net Profit: {net_amt}')
    print(f'Average Monthly Change: {avg_changes}')
    print(f'Greatest Increase in Profits: {max_profit}')
    print(f'Greatest Loss In Profits: {min_losses}')

    # Set the path for the text file 
    pybank_output = os.path.join('Resources', "PyBank_Analysis.txt")    

    # Write script to create text file with results 
    with open(pybank_output, 'w') as text:
        text.write('Financial Analysis')
        text.write('\n------------------------------------')
        text.write(f'\nTotal Months: {tot_months}')
        text.write(f'\nNet Profit: {net_amt}')
        text.write(f'\nAverage Monthly Change: {avg_changes}')
        text.write(f'\nGreatest Increase In Profits: {max_profit}')
        text.write(f'\nGreatest Loss In Profits: {min_losses}')

with open(csv_path, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    if csv.Sniffer().has_header:
        next(csvreader)    
    # Use function
    pybank(csvreader)
