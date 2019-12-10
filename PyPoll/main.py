import os, csv

total_votes = 0

candidates = []

candidate_totals = {}
candidate_percents = {}

#Creating string output for txt file
def election_analysis(candidates, candidate_totals, candidate_percents):
    summary_string = f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------\n"""
    for candidate in candidates:
        summary_string += (f"{candidate}: {candidate_percents[candidate]}% ({candidate_totals[candidate]})\n")
    summary_string += f"""-------------------------
Winner: {winner}
-------------------------"""
    return summary_string

election_path = os.path.join("..", "PyPoll", "election_data.csv")

with open(election_path, newline='', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    for row in csv_reader:
        
        #Total number of votes cast
        total_votes += 1

        #List of candidates who received votes
        if row[2] not in candidates: 
            candidates.append(row[2])
            candidate_totals[row[2]] = 0
            candidate_percents[row[2]] = 0

        #Total number of votes each candidate won
        candidate_totals[row[2]] += 1

#Percentage of votes each candidate won
def find_percentage(value, total):
    return round(((value / total) * 100), 3)

for candidate in candidates:
    candidate_percents[candidate] = (find_percentage(candidate_totals[candidate], total_votes))

#Winner of the election based on popular vote
winner = max(candidate_totals, key=candidate_totals.get)

#Print summary table to terminal
print(election_analysis(candidates, candidate_totals, candidate_percents))

#Output summary table to txt file
file = open('main_output.txt', 'w')
file.write(election_analysis(candidates, candidate_totals, candidate_percents))
file.close()