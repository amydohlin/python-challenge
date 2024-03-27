# python-challenge
## Module 03 Challenge

### Overview

The objective of this challenge was to utilize newly developed Python skills. These skills include importing dependencies, opening and reading CSV files, calculating data to find changes and totals, parsing through the rows in the CSVs to pull out unique values, and export results to a text file. There were two parts to this challenge: PyBank and PyPoll.
------------

### Analysis

PyBank and PyPoll are two separate files within this challenge, but a lot of their code was the same in terms of starting and ending. Both started with importing os and csv as dependents from the Python library. These dependencies allow me to open and read CSV files to extract and analyze the data contained. Next, I needed to open the CSV files and specify the delimiter with the following code:
  #Open the CSV file
  with open(csvpath) as csvfile:
    # Specify the delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    #Read header row so it's skipped while reading the data
    csv_header = next(csvreader)

At various points in both PyBank and PyPoll, I needed to utilize for loops to retrieve and calculate certain values from the data. The purpose of the for loops is to read through each row of data and search for a defined parameter (such as a certain column's value, referenced by using the column's index number), then use it to perform a calculation and add the calculated value to a list. Both sections of the assignment also required the use of if statements and conditionals to parse out specific values (such as <, >, ==, +=, etc.). Finally, the last part in each section was to print the results to both the output window in VSCode and export them to a text file. This was accomplished by using print() statements with an f-string, and inserting the desired variable with {} to call the needed value. Following this step, the results were exported to text files (saved in the analysis folders of PyBank and PyPoll).

## PyBank
The specific requirements for PyBank were to count the total number of months, calculate the net total profit, calculate the daily changes in profits, find the greatest increase and its corresponding date, find the greatest decrease and its correpsonding date, and compute the average change.

First I defined a function for finding the total_months and total_profits_losses (i.e. the net total profits), and set these variables to 0. Within the function definition I used a for loop to count the number of months and add 1 to the total_months count for each line, which ended up being 86 months. This function also looped through the rows in the Profits/Losses column and added each integer value together to obtain the net profit ($22,564,198).

## PyPoll
The specific requirements for PyPoll were to count the total number of votes, how many votes each candidate received, what percentage of votes each candidate received, and the winner
----------------

### Summary
---------

### Resources
---------
Xpert Learning Assistant
Module 03 Activities
Office Hours/Instructional Staff
