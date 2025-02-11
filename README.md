# Py Me Up, Charlie

## Welcome to the world of programming with Python! 

In this challenge, you'll apply Python scripting skills on two separate datasets, PyBank and PyPoll. 

Before You Begin:
1. Create a new repository for this project called python-challenge.
2. Clone the new repository to your computer.
3. Inside your local git repository, create a directory for both of the Python challenges. Use folder names corresponding to the challenges: PyBank and PyPoll.
4. Inside of each folder that you just created, add the following:
    - A new file called main.py. This will be the main script to run for each analysis.
    - A "Resources" folder that contains the CSV files you used. Make sure your script has the correct path to the CSV file.
    - An "analysis" folder that contains your text file that has the results from your analysis.
5. Push the above changes to GitHub or GitLab.

## PyBank 

<p align="center">
  <img width="360" height="180" src="https://github.com/leslievazquez/Python_Challenge/blob/main/Images/revenue.png">
</p>

You are tasked with creating a Python script for analyzing the financial records of a company using a file containing a set of financial data called budget_data.csv. The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, the company has rather lax standards for accounting so the records are simple.)

Create a Python script that analyzes the records to calculate each of the following:
- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The average of the changes in "Profit/Losses" over the entire period
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in losses (date and amount) over the entire period
- The final script should both print the analysis to the terminal and export a text file with the results.

The analysis should look like the one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

## PyPoll 
<img src="https://github.com/leslievazquez/Python_Challenge/blob/main/Images/vote_counting.png">

You are tasked with helping a small, rural town modernize its vote counting process using a file containing a set of poll data called election_data.csv. The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:
- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote.
- The final script should both print the analysis to the terminal and export a text file with the results.

The analysis should look like the one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```


