"""PyPoll Script - Analyzes election results"""
 
# Import required modules
import csv   # For reading CSV files
import os    # For handling file paths
 
# Define file paths using raw strings to avoid escape character issues
# Input path points to the CSV file containing election data
file_to_load = r"C:\\Users\\aloux\bootcamp\\instructor_gitlab\\02-Homework\\03-Python\Starter_Code\\PyPoll\\Resources\\election_data.csv"
# Output path specifies where the analysis results will be saved
file_to_output = r"C:\\Users\\aloux\bootcamp\\instructor_gitlab\\02-Homework\\03-Python\Starter_Code\\PyPoll\\analysis\\election_analysis.txt"
 
# Initialize variables to track election data
total_votes = 0          # Counter for total number of votes cast
candidates = {}          # Dictionary to store candidate names (key) and their vote counts (value)
winner = ""             # Will store the winning candidate's name
winning_votes = 0       # Will store the winning vote count
 
try:  # Use try-except to handle potential file errors
    print("Starting vote count...")
 
    # Open and read the CSV file
    with open(file_to_load) as election_data:
        # Create CSV reader object
        reader = csv.reader(election_data)
 
        # Skip the header row but store it for reference
        header = next(reader)  # Header should be ["Ballot ID", "County", "Candidate"]
 
        # Process each vote in the dataset
        for row in reader:
            # Count total votes
            total_votes += 1
 
            # Extract candidate name from the current row (third column)
            candidate = row[2]
 
            # If this is the first vote for this candidate, add them to the dictionary
            if candidate not in candidates:
                candidates[candidate] = 0
 
            # Add a vote to this candidate's count
            candidates[candidate] += 1
 
    # Print total votes processed for verification
    print(f"\nProcessed {total_votes:,} votes.\n")
 
    # Create the output summary string, starting with the header
    output = (
        "Election Results\n"
        "-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        "-------------------------\n"
    )
 
    # Process results for each candidate
    for candidate in candidates:
        # Calculate vote count and percentage for current candidate
        votes = candidates[candidate]
        vote_percentage = (votes / total_votes) * 100
 
        # Update winner information if this candidate has the most votes
        if votes > winning_votes:
            winning_votes = votes
            winner = candidate
 
        # Add this candidate's results to the output string
        output += f"{candidate}: {vote_percentage:.3f}% ({votes:,})\n"
 
    # Complete the output string with winner announcement
    output += (
        "-------------------------\n"
        f"Winner: {winner}\n"
        "-------------------------\n"
    )
 
    # Print complete results to terminal
    print(output)
 
    # Write results to text file
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)
 
    print(f"Results have been written to: {file_to_output}")
 
except FileNotFoundError:
    # Handle case where input file isn't found
    print(f"Error: Could not find the file at {file_to_load}")
    print("Please check if:")
    print("1. The path is correct")
    print("2. The Resources folder exists")
    print("3. The election_data.csv file is in the Resources folder")
except Exception as e:
    # Handle any other unexpected errors
    print(f"An error occurred: {str(e)}")