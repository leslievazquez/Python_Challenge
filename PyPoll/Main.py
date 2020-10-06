# Counting Votes Process

# Create a Python script that analyzes the records to calculate:
# a) The total number of votes cast
# b) A complete list of candidates who received votes
# c) The percentage of votes each candidate won
# d) The total number of votes each candidate won
# e) The winner of the election based on popular vote.
# f) The final script should print the analysis to the terminal and export a text file with the results.

# Import modules 
import os
import csv

# Set cvs path (directory - folder of the cvs file, file_name including file extension)
csv_path = os.path.join('Resources', 'election_data.csv')

# Create a function to calculate percentage of votes
def percentage (part, whole):
    return 100 * float(part)/float(whole)

def pypoll(data):
    # Define variables 
    # Reset the vote counts to zero
    totalcount = 0; khan = 0; correy = 0; li = 0; otooley = 0; max_votecount = 0
    voterid = [0]  
    candidate = [2]

    # Begin the loop with for
    for i in data:
        # Find total count of votes 
        totalcount = totalcount + 1
    
        # Find votecount by candidates
        candidate = i[2]
        if candidate =="Khan":
           khan = khan + 1
        if candidate =="Correy":
           correy = correy + 1
        if candidate =="Li":
           li = li + 1
        if candidate =="O'Tooley":
           otooley = otooley + 1
                
        # Create a list 
        candidatevote = {"Khan": khan,"Correy": correy,"Li" :li, "O'Tooley": otooley}
        
    # Find the winner 
    for candidate, value in candidatevote.items():
        if value > max_votecount:
            max_votecount = value
            winner = candidate
                
    # Print the results       
    print(f'Election Results'+'\n')
    print(f'-------------------------------'+'\n')
    print(f'Total Votes: {totalcount}'+'\n')
    print(f'-------------------------------'+'\n')
    print(f'Khan: {percentage(khan,totalcount):.3f}%  ({khan})')
    print(f'Correy: {percentage(correy, totalcount):.3f}%  ({correy})')
    print(f'Li: {percentage(li, totalcount):.3f}%  ({li})')
    print(f'O\'Tooley: {percentage(otooley, totalcount):.3f}%  ({otooley})')
    print(f'--------------------------------'+'\n')
    print(f'Winner: {winner} '+'\n')
    print(f'--------------------------------'+'\n')    

    # Set the path for the text file 
    pypoll_output = os.path.join('Analysis', "PyPoll_Analysis.txt")    
   
    # Write script to create text file with results 
    with open(pypoll_output, 'w') as text:
        text.write(f'Election Results'+'\n')
        text.write(f'-------------------------------'+'\n')
        text.write(f'Total Votes: {totalcount}'+'\n')
        text.write(f'-------------------------------'+'\n')
        text.write(f'Khan: {percentage(khan,totalcount):.3f}%  ({khan})')
        text.write(f'Correy: {percentage(correy, totalcount):.3f}%  ({correy})')
        text.write(f'Li: {percentage(li, totalcount):.3f}%  ({li})')
        text.write(f'O\'Tooley: {percentage(otooley, totalcount):.3f}%  ({otooley})')
        text.write(f'--------------------------------'+'\n')
        text.write(f'Winner: {winner} '+'\n')
        text.write(f'--------------------------------'+'\n')   

# Open and read the cvs file 
with open(csv_path, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    if csv.Sniffer().has_header:
        next(csvreader)
    # Use main function
    pypoll(csvreader)