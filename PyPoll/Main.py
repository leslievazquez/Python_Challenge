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
election_csv = os.path.join('Resources', 'election_data.csv')



