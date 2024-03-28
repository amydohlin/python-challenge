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

The next task was to calculate the daily changes in profits. First I created an empty list to store the changes as they're calculated, then initialized the variables greatest_increase and greatest_decrease as 0 to store the maximum and minimum changes. Next I used a for loop to go through every line in the CSV and read the profit lines as:
  current_profit = int(bank_data[i][1])
  previous_profit = int(bank_data[i-1][1])

Then I created a variable for change where it subtracted the previous_profit from the current_profit, and stored the integer in the changes list. I used if statements (within the for loop, so they're included in every iteration) with conditionals (< and >) to find the largest change and the smallest change. Once those steps were completed I found the average of changes using the sum of the changes divided by total changes. This was the last step before printing the results and exporting a summary to a text file.

## PyPoll
The specific requirements for PyPoll were to count the total number of votes, how many votes each candidate received, what percentage of votes each candidate received, and the winner of the election. After reading in the CSV file with the election data, I initialized the variable total_votes and made a for loop to count through the rows in the poll data and store the number of votes in the variable. Next I created an empty list called candidates and a for loop to find all the names of the candidates. The loop searches through the values in the "Candidate" column in the CVS, and uses an if statement that determines if a candidate's name has not already been added to the list, then add the name to the list.

Following the candidates list, I needed to find out how many votes each candidate won, and the percentage of votes each candidate won. In order to store this data I made an empty dictionary called candidate votes that housed the candidates' names as the keys, and the number of votes as their corresponding values. I also initialized a total_candidate_votes variable to store the values. Following this I created a for loop:

    # Iterate through the rows in poll_data
    for row in poll_data:
      total_candidate_votes += 1

    # Find number of votes for each candidate
    # Reference candidate column [2]
      candidate = row[2]

    # Use if statement to count candidate votes
      if candidate in candidate_votes:
        candidate_votes[candidate] +=1
      else:
        candidate_votes[candidate] = 1

where the if statement was used to determine the candidate in the current row being read and add a vote to their tally in the candidate_votes dictionary. This dictionary then allowed me to use its values in another for loop to calculate the percentage of votes won by each candidate. This loop took each candidate's votes and divided by the total number of votes (and multiplied by 100) to calculate the percentage. It also includes a print statement that shows each candidate's name and the percentage of votes and number of votes won.

Before creating the results summary and text export, the last task was to find the election winner. This involved utilizing the max() function to call the the candidate_votes dictionary and finding the candidate (key) with the most votes (value). Once that was found, I continued with the results and text file export, which can be found in the PyPoll folder.
----------------

### Summary
This challenge was a great introduction to Python and its capabilities to handle large quantities of data. The skills that were taught and enforced included creating lists and dictionaries to store data, using for loops and if statements to iterate through data rows and extract certain information, and apply functions to determine certain values as well as a deeper dive into data importation and exportation. These skills will form a foundation to use in future assignments.
---------

### Resources
- Xpert Learning Assistant
- Module 03 Activities
- Office Hours/Instructional Staff
---------
