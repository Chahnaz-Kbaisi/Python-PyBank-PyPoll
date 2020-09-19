# Importing Modules/Dependencies
import os
import csv

# creating the path
csvpath = os.path.join('Resources', 'election_data.csv')

# open & read in csvfile
def voter_func(filepath):
    with open(csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        csv_header = next(csvfile)

        Voter_ID = []
        County = []
        Candidate = []
        Results = []
        Percentage = []

# using dictionary function to set vote_totals       
        Vote_totals = {}

        Votes = 0

# running conditionals

        for rows in csvreader:
            Voter_ID.append(rows[0])
            Current_Candidate = rows[2]
            if Current_Candidate not in Candidate:
                Candidate.append(Current_Candidate)
                Vote_totals[Current_Candidate] = 1
            else:
                Vote_totals[Current_Candidate] += 1

        TotalNumberVoters = len(Voter_ID)
        TotalCandidates = len(Candidate)
        Winner = sorted(Vote_totals)

# Print statements

        print("'''text")
    print("Election Results")
    print("----------------------------------------")
    print("Total Votes: " + str(TotalNumberVoters))
    print("----------------------------------------")
    for C in Candidate:
        print(f"{C}: {round(Vote_totals[C] * 100 / (TotalNumberVoters), 3)}% ({Vote_totals[C]})")
    print("----------------------------------------")
    print("Winner: " + str(Winner[1]))
    print("----------------------------------------")
    print("'''")

# Setting the file to write to outputs

    output_file = os.path.join("Analysis","Output_election.csv")
# opening the file using write mode    
    with open(output_file, "w") as datafile:
# Initializing csv writer         
        writer = csv.writer(datafile)

        writer.writerow(["'''text"])
        writer.writerow(["Election Results"])
        writer.writerow(["----------------------------------------"])
        writer.writerow(["Total Votes: " + str(TotalNumberVoters)])
        writer.writerow(["----------------------------------------"])
        for C in Candidate:
            writer.writerow([f"{C}: {round(Vote_totals[C] * 100 / (TotalNumberVoters), 3)}% ({Vote_totals[C]})"])

        writer.writerow(["----------------------------------------"])
        writer.writerow(["Winner: " + str(Winner[1])])
        writer.writerow(["----------------------------------------"])
        writer.writerow(["'''"])
    return ""


voter_func(csvpath)
