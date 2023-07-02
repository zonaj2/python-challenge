import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

# Create empty lists to store candidate information
candidate_names = []
total_votes = []
vote_percentages = []

# Read data from CSV file
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header row

    # Process each row in the CSV file
    for row in csvreader:
        candidate = row[2]

        # Append candidate name to the list if it's not already present
        if candidate not in candidate_names:
            candidate_names.append(candidate)
            total_votes.append(1)  # Initialize vote count as 1
        else:
            # If candidate is already in the list, increment their vote count
            candidate_index = candidate_names.index(candidate)
            total_votes[candidate_index] += 1

    # Calculate total votes
    total_vote_count = sum(total_votes)
    print(total_vote_count)

    # Calculate vote percentages
    for vote_count in total_votes:
        vote_percentage = round(((vote_count / total_vote_count) * 100), 3)
        vote_percentages.append(vote_percentage)

# Display candidate information
for i in range(len(candidate_names)):
    print(f'{candidate_names[i]}: {vote_percentages[i]}% ({total_votes[i]})')

# Find the candidate with the most votes
max_votes = max(total_votes)
max_index = total_votes.index(max_votes)
winner = candidate_names[max_index]

# Print the name of the candidate with the most votes
print(f"Winner: {winner}")
