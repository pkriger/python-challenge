import os
import csv

current_directory=os.path.dirname(os.path.abspath(__file__))
poll_path= os.path.join(current_directory,"Resources","election_data.csv")

with open (poll_path, 'r') as poll_file:
    csvreader = csv.reader (poll_file, delimiter = ",")
    
    headerline = next(csvreader)
    # define variavles
    
    votes = 0
    khan_votes=0
    correy_votes=0
    li_votes=0
    otool_votes=0
    candidates= ["Khan","Correy","Li","O'Tooley"]
    

    for row in csvreader:
        votes += 1

        if row[2] == "Khan":
            khan_votes += 1
        elif row[2] == "Correy":
            correy_votes += 1
        elif row[2] == "Li":
            li_votes += 1
        elif row[2] == "O'Tooley":
            otool_votes += 1

    candidate_votes = [khan_votes, correy_votes, li_votes, otool_votes]
    
    #determine winner
    winner_inx = candidate_votes.index(max(candidate_votes))  
    winner = candidates[winner_inx]
        

    row1=(f"Election Results")
    row2=(f"-------------------------")
    row3=(f"Total Votes: {(votes)}")
    row4=(f"-------------------------")
    row5=(f"Khan: {round((khan_votes/votes*100),4)}% ({khan_votes})")
    row6=(f"Correy: {round((correy_votes/votes*100),4)}% ({correy_votes})")
    row7=(f"Li: {round((li_votes/votes*100),4)}% ({li_votes})")
    row8=(f"O'Tooley: {round((otool_votes/votes*100),4)}% ({otool_votes})")
    row9=(f"-------------------------")
    row10=(f"Winner: {winner}")
    row11=(f"-------------------------")

#write to txt        
analysispath= os.path.join(current_directory,"Analysis",'PyPoll Result.txt')
with open (analysispath, 'w') as poll_result:

    poll_result.write(row1 + '\n')
    poll_result.write(row2 + '\n')
    poll_result.write(row3 + '\n')
    poll_result.write(row4 + '\n')
    poll_result.write(row5 + '\n')
    poll_result.write(row6 + '\n')
    poll_result.write(row7 + '\n')
    poll_result.write(row8 + '\n')
    poll_result.write(row9 + '\n')
    poll_result.write(row10 + '\n')
    poll_result.write(row11 + '\n')

#print
with open (analysispath, 'r') as poll_result:   
    for lines in poll_result:
        print(lines)