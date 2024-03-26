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

At various points in both PyBank and PyPoll, I needed to utilize for loops to retrieve and calculate certain values from the data. The purpose of the for loops is to read through each row of data and search for a defined parameter (such as a certain column's value, referenced by using the column's index number), then use it to perform a calculation and add the calculated value to a list. 
----------------

### Summary
---------

### Resources
---------
Xpert Learning Assistant
Module 03 Activities
Office Hours/Instructional Staff
