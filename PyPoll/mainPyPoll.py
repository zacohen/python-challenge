import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    TotalVotes = 0
    Candidates = []
    TotalCandidateVotes = []
    

    for row in csvreader:

        TotalVotes = TotalVotes + 1
        CandidateName = (row[2])

        if CandidateName in Candidates:
            candidate_index = Candidates.index(CandidateName)
            TotalCandidateVotes[candidate_index] = TotalCandidateVotes[candidate_index] + 1
        else:
            #going through and adding candidates and votes
            Candidates.append(CandidateName)
            TotalCandidateVotes.append(1)
        


pct = []
max_votes = TotalCandidateVotes[0]
max_index = 0

for x in range(len(Candidates)):
    #calculation to get the percentage
    vote_pct = round(TotalCandidateVotes[x]/TotalVotes*100, 2)
    pct.append(vote_pct)
    
    if TotalCandidateVotes[x] > max_votes:
        max_votes = TotalCandidateVotes[x]
        max_index = x

election_winner = Candidates[max_index] 









print("Election Results")
print("--------------------------")
print("Total Votes:", TotalVotes)
for x in range(len(Candidates)):
    print(f'{Candidates[x]} : {pct[x]}% ({TotalCandidateVotes[x]})')
print('----------------------------------------------------------------')
print(f'winner: {election_winner}')
print('-----------------------------------------------------------------')

filename = "analysis.txt"
f = open("Analysis/Analysis.txt", "w" )
f.write("Election Results")
f.write('\n')
f.write("---------------------------------")
f.write('\n')
f.write("Total Votes:" + str(TotalVotes))
f.write('\n')
#honestly can't figure out why its exporting differently but i kept playing with it and messing it up more 
for x in range(len(Candidates)):
    f.write(f'{Candidates[x]} : {pct[x]}% ({TotalCandidateVotes[x]})')
f.write('\n')
f.write('--------------------------------------------------------------------')
f.write('\n')
f.write(f"winner:" + (election_winner))
f.write('\n')







