import csv
import os

source_file = os.path.join("Resources", "budget_data.csv")
analysis_folder = "analysis"
if not os.path.exists(analysis_folder):
    os.mkdir(analysis_folder)

with open(source_file,'r', newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader, None)
    data = list(reader)
    
months = []
profit = 0.0
avgchange = []
grt_inc_ind = 0
grt_dec_ind = 0
grt_inc_amt = min([float(x[1]) for x in data])
grt_dec_amt = max([float(x[1]) for x in data])

for i in range(len(data)):
    if data[i][0] not in months:
        months.append(data[i][0])
    profit += float(data[i][1])
    if i < len(data) - 1:
        change = float(data[i+1][1])-float(data[i][1])
        avgchange.append(change)
        if change > grt_inc_amt:
            grt_inc_amt = change
            grt_inc_ind = i+1
        if change < grt_dec_amt:
            grt_dec_amt = change
            grt_dec_ind = i+1
report = "Financial Analysis\n"
report += "--------------------------\n"
report += f"Total months:\t\t\t{len(months)}\n"
report += f"Total profit/loss:\t\t${profit:0.2f}\n"
report += f"Average changes:\t\t${sum(avgchange) / len(avgchange) :0.2f}\n"
report += f"Greatest increase in profit:\t{data[grt_inc_ind][0]} (${grt_inc_amt:0.2f})\n"
report += f"Greatest decrease in profit:\t{data[grt_dec_ind][0]} (${grt_dec_amt:0.2f})"
print(report)


analysis_file = os.path.join("analysis", "report.txt")
out_file = open(analysis_file, "w", encoding="utf-8")
out_file.writelines(report)
out_file.close()