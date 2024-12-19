"""PyBank Script - Analyzes financial records"""
 
# Import necessary modules
import csv  # For reading CSV files
import os   # For handling file paths
 
# Define file paths using raw strings to avoid escape character issues
# Input path points to the CSV file containing budget data
file_to_load = r"C:\\Users\\aloux\bootcamp\\instructor_gitlab\\02-Homework\\03-Python\Starter_Code\\PyBank\\Resources\budget_data.csv"
# Output path specifies where the analysis results will be saved
file_to_output = r"C:\\Users\\aloux\\bootcamp\\instructor_gitlab\\02-Homework\\03-Python\\Starter_Code\\PyBank\\analysis\budget_analysis.txt"
 
# Initialize variables to store our financial analysis data
total_months = 0      # Will count the total number of months in dataset
total_net = 0        # Will sum all profit/losses
net_change_list = [] # Will store month-to-month changes
date_list = []       # Will store dates corresponding to changes
previous_net = None  # Will store previous month's profit/loss for change calculation
 
try:  # Use try-except to handle potential file errors
    # Open and read the CSV file
    with open(file_to_load) as financial_data:
        # Create CSV reader object
        reader = csv.reader(financial_data)
 
        # Skip the header row but store it for reference
        header = next(reader)  # Header should be ["Date", "Profit/Losses"]
 
        # Process first row separately to establish baseline
        first_row = next(reader)
        total_months = 1  # Count first month
        total_net = int(first_row[1])  # Add first profit/loss to total
        previous_net = int(first_row[1])  # Set baseline for change calculation
 
        # Loop through remaining rows in the dataset
        for row in reader:
            # Count each month
            total_months += 1
 
            # Convert profit/loss string to integer and add to total
            current_net = int(row[1])
            total_net += current_net
 
            # Calculate change from previous month
            net_change = current_net - previous_net
 
            # Store the date and change in their respective lists
            date_list.append(row[0])
            net_change_list.append(net_change)
 
            # Update previous_net for next iteration
            previous_net = current_net
 
    # Calculate financial metrics
    # Average change is sum of changes divided by number of changes
    average_change = sum(net_change_list) / len(net_change_list)
 
    # Find greatest increase and decrease
    greatest_increase = max(net_change_list)
    greatest_decrease = min(net_change_list)
 
    # Find dates corresponding to greatest changes
    # Add 1 to index because changes list is one shorter than dates list
    increase_date = date_list[net_change_list.index(greatest_increase)]
    decrease_date = date_list[net_change_list.index(greatest_decrease)]
 
    # Create formatted output string
    output = (
        "\nFinancial Analysis\n"
        "-------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_net:,}\n"
        f"Average Change: ${average_change:,.2f}\n"
        f"Greatest Increase in Profits: {increase_date} (${greatest_increase:,})\n"
        f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease:,})\n"
    )
 
    # Print results to terminal
    print(output)
 
    # Write results to text file
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)
 
    print(f"\nResults have been written to: {file_to_output}")
 
except FileNotFoundError:
    # Handle case where input file isn't found
    print(f"Error: Could not find the file at {file_to_load}")
    print("Please check if:")
    print("1. The path is correct")
    print("2. The Resources folder exists")
    print("3. The budget_data.csv file is in the Resources folder")
except Exception as e:
    # Handle any other unexpected errors
    print(f"An error occurred: {str(e)}")