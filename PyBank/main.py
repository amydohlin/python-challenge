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

# Calculate changes in "Profits/Losses" over entire period
# Create empty list for changes
changes = []

# Initialize greatest_increase, greatest_decrease, greatest_increase_date, greatest_decrease_date
greatest_increase = 0
greatest_decrease = 0
greatest_increase_date = ""
greatest_decrease_date = ""

# Find greatest increase and decrease in profits (date and amount) over entire period

# Create a loop to read through each row of data to calculate day-to-day changes
for i in range(1, len(bank_data)):

        # Define variables for the current profit and previous profit
        # Reference 'i' to read the current row, define it as an integer
        # Reference 'i-1' to read the previous row, define it as an integer
    current_profit = int(bank_data[i][1])
    previous_profit = int(bank_data[i-1][1])

        # Define variable for change in profit
        # Store the value of (current_profit - previous_profit) in 'change'
        # Append every calculation of change to the 'changes' list
    change = int(current_profit - previous_profit)
    changes.append(change)

        # Greatest Increase and Date
    if change > greatest_increase:
        greatest_increase = change
        greatest_increase_date = bank_data[i][0]

        # Greatest Decrease and Date
    if change < greatest_decrease:
        greatest_decrease = change
        greatest_decrease_date = bank_data[i][0]

        # Calculate the average of the changes
        avg_change = sum(changes) / len(changes)
    
# Print summary of results
print(f"PyBank Analysis:")
print(f"Total Months: {total_months}")
print(f"Net Total: ${total_profits_losses}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase: ${greatest_increase}, {greatest_increase_date}")
print(f"Greatest Decrease: ${greatest_decrease}, {greatest_decrease_date}")

# Export to a text file and save to analysis folder
pybank_results = "analysis/pybank_results.text"

with open(pybank_results, "w") as file:
    # Write in the results summary
    file.write(f"PyBank Analysis:\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Net Total: ${total_profits_losses}\n")
    file.write(f"Average Change: ${avg_change:.2f}\n")
    file.write(f"Greatest Increase: ${greatest_increase}, {greatest_increase_date}\n")
    file.write(f"Greatest Decrease: ${greatest_decrease}, {greatest_decrease_date}\n")
print(f"The PyBank results have been exported to a text file.")
