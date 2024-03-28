# Impoprt os and csv modules 
import os
import csv

# Create path to csv resource
# python-challenge\PyPoll\Resources\election_data.csv
csvpath = os.path.join("Resources/election_data.csv")

# Read the csv file
with open(csvpath) as csvfile:

    # Specify delimiter in csvreader variable
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read header row first so it's skipped while reading the data
    csv_header = next(csvreader)

    # Read in the data
    poll_data = list(csvreader)


# Count total number of votes cast
# Initialize total_votes
total_votes = 0
for row in poll_data:
    total_votes += 1

# Complete list of candidates who received votes
# Create empty list for candidate names
candidates = []

# Create for loop to find unique candidate names
for row in poll_data:
    # Define name variables for candidates
    # Use the index number of the candidate column so it knows where to look
    name = row[2]

    # Use if statement to check if a name is already in the candidate list
    # If not, then add to the candidates list
    if name not in candidates:
        candidates.append(name)

# Calculate total number of votes that each candidate won
# Create empty list to store number of votes for each candidate
candidate_votes = {}

# Initialize count for total votes casted
total_candidate_votes = 0

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

# Calculate percentage each candidate won
# Use .3f to round the percentage to three decimal places
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes)*100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

# Determine election winner based on popular vote (highest total number)
winner = max(candidate_votes, key= candidate_votes.get)

# Print summary of results
print("Election Results")
print('-------------------------------------------')       
print(f'Total votes: {total_votes}')
print('-------------------------------------------') 
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes)*100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print('-------------------------------------------') 
print(f'Winner: {winner} ')

# Export to a text file and save to analysis folder
pypoll_results = "analysis/pypoll_results.text"

with open(pypoll_results, "w") as file:
    # Write in the results summary
    file.write(f"Election Results\n")
    file.write('-------------------------------------------\n')
    file.write(f"Total votes: {total_votes}\n")
    file.write('-------------------------------------------\n')
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes)*100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write('-------------------------------------------\n')
    file.write(f"Winner: {winner}\n")
print(f"The PyPoll results have been exported to a text file.")