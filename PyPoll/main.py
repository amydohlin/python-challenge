# Impoprt os and csv modules 
import os
import csv

# Create path to csv resource
# python-challenge\PyPoll\Resources\election_data.csv
csvpath = os.path.join("python-challenge", "PyPoll","Resources","election_data.csv")

# Read the csv file
with open(csvpath) as csvfile:

    # Specify delimiter in csvreader variable
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read header row first so it's skipped while reading the data
    csv_header = next(csvreader)


# Count total number of votes cast
    

# Complete list of candidates who received votes
    

# Calculate percentage of votes that each candidate won
    

# Calculate total number of votes that each candidate won
    

# Determine election winner based on popular vote (highest total number)
    

# Print summary of results