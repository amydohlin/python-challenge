# Import dependencies
import os
import csv

# Read in the CSV file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV file
with open(csvpath) as csvfile:
    # Specify the delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read header row so it's skipped while reading the data
    csv_header = next(csvreader)

    # Assign variables to the columns in the csv
    # Define parameter for data
    def total(bank_data):
        # Initialize counters for months and profits/losses
        total_months = 0
        total_profits_losses = 0

        for row in bank_data:
            # Add to the totals as each row is counted
            total_months += 1

            # Profits/Losses is an integer and is the second column in the CSV
            # Declare it as an integer and tell it which column to read
            total_profits_losses += int(row[1])

        return total_months, total_profits_losses

    # Read in the data from the CSV file
    bank_data = list(csvreader)

# Call the total function
total_months, total_profits_losses = total(bank_data)

# Count total number of months in dataset
print(f'Total Months: {total_months}')

# Calculate net total of "Profits/Losses" over entire period
print(f'Net Total: ${total_profits_losses}')

# Calculate changes in "Profits/Losses" over entire period
#   Create empty list for changes
    changes = []

#   Calculate the average of the changes
    avg_change = average(total_profits_losses)


#   Find greatest increase in profits (date and amount) over entire period
    for i in bank_data:


# Find greatest decrease in profits (date and amount) over entire period
    

# Print summary of results
