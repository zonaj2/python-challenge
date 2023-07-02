import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

# Empty lists to store candidate info
candidate_names = []
total_votes = []
vote_percentages = []

# Read data from CSV file
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header row

    # Create dictionary to store vote counts for each candidate
    candidates = {}

    # Count votes for each candidate
    for row in csvreader:
        candidate = row[2]

        # If candidate is not in the dictionary, add them with initial vote count of 1
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1

    # Calculate total votes
    total_vote_count = sum(candidates.values())
    print(f'\n')
    print(f'Election Results\n')
    print(f'-------------------------\n')
    print(f'Total Votes: {total_vote_count}\n')
    print(f'-------------------------\n')

    # Calculate candidate information
    for candidate, vote_count in candidates.items():
        vote_percentage = round(((vote_count / total_vote_count) * 100), 3)

        # Append candidate information to the lists
        candidate_names.append(candidate)
        total_votes.append(vote_count)
        vote_percentages.append(vote_percentage)

# Display the candidate information
for i in range(len(candidate_names)):
    print(f'{candidate_names[i]}: {vote_percentages[i]}% ({total_votes[i]})\n')
    
# Find the candidate with the most votes
winner = max(candidates, key=candidates.get)

# Print the name of the candidate with the most votes
print(f'-------------------------\n')
print(f"Winner: {winner}\n")
print(f'-------------------------')

# Prepare output 
output = (f'Election Results\n'
          f'-------------------------\n'
          f'Total Votes: {total_vote_count}\n'
          f'-------------------------\n')

# Append candidate information to the output 
for i in range(len(candidate_names)):
    output += f'{candidate_names[i]}: {vote_percentages[i]}% ({total_votes[i]})\n'

output += (f'-------------------------\n'
           f'Winner: {winner}\n'
           f'-------------------------\n')

# Set variable for output file
output_file = os.path.join("analysis", "election.txt")

# Open the output file
with open(output_file, "w") as txt_file:
    txt_file.write(output)
