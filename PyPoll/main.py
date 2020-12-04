import os
import csv

source_file = os.path.join("Resources", "election_data.csv")
analysis_path = "analysis"

if not os.path.exists(analysis_path):
    os.mkdir(analysis_path)

with open(source_file, "r", encoding="utf-8") as datafile:
    reader = csv.reader(datafile)
    next(reader, None)
    data = list(reader)

total_votes = len(data)
candidates = []
[candidates.append(i[2]) for i in data if i[2] not in candidates]
candidate_votes_list = []
for cand in candidates:
    candidate_votes = {}
    candidate_votes["name"] = cand
    votes = len([x for x in data if x[2] == cand])
    candidate_votes["votes"] = votes
    candidate_votes["percentage"] = votes/total_votes
    candidate_votes_list.append(candidate_votes)

winner = ""
winner_vote = 0
result = "Election Results\n"
result += "--------------------------\n"
result += f"Total Votes:\t{total_votes}\n"
result += "--------------------------\n"
for cand in candidate_votes_list:
    if len(cand["name"]) < 8:
        result += f"{cand['name']}:\t\t{cand['percentage']*100:0.3f}%\t({cand['votes']})\n"
    else:
        result += f"{cand['name']}:\t{cand['percentage']*100:0.3f}%\t({cand['votes']})\n"
    if cand["votes"] > winner_vote:
        winner = cand["name"]
        winner_vote = cand["votes"]
result += "--------------------------\n"
result += f"Winner: {winner}\n"
result += "--------------------------"
print(result)
# print("Election Results")
# print("----------------------")
# print(f"Total Votes:\t{total_votes}")
# print("----------------------")
# for cand in candidate_votes_list:
#     print(f"{cand['name']}:\t{cand['percentage']*100:0.3f}%\t({cand['votes']})")
# print("----------------------")

analysis_file = os.path.join(analysis_path, "analysis.txt")
analysis = open(analysis_file, "w", encoding="utf-8")
analysis.writelines(result)
analysis.close()