import os, csv

total_months = 0
total_profitloss = 0
max_profitloss = 0
min_profitloss = 0

budget_path = os.path.join("..", "PyBank", "budget_data.csv")

with open(budget_path, newline='', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    for row in csv_reader:
        
        #Total number of months
        total_months += 1

        #Net total amount of Profits/Losses
        current_profitloss = int(row[1])
        total_profitloss += current_profitloss

        #Greatest increase in profits (date and amount)
        if int(row[1]) > max_profitloss:
            max_profitloss = int(row[1])
            max_month = row[0]
        else:
            max_profitloss = max_profitloss

        #Greatest decrease in profits (date and amount)
        if int(row[1]) < min_profitloss:
            min_profitloss = int(row[1])
            min_month = row[0]
        else:
            min_profitloss = min_profitloss

#Average of changes in Profits/Losses
avg_profitloss = int(total_profitloss / total_months)

#Create dictionay of summary
data_summary = {
    "total_months": total_months,
    "total_profitloss": total_profitloss,
    "avg_profitloss": avg_profitloss,
    "max_profitloss": max_profitloss,
    "min_profitloss": min_profitloss,
    "max_month": max_month,
    "min_month": min_month
}

#Creating string output for txt file
def financial_analysis(data_summary):
    summary_string = f"""Financial Analysis
----------------------------
Total Months: {data_summary['total_months']}
Total: ${data_summary['total_profitloss']}
Average Change: ${data_summary['avg_profitloss']}
Greatest Increase in Profits: {data_summary['max_month']} ${data_summary['max_profitloss']}
Greatest Decrease in Profits: {data_summary['min_month']} ${data_summary['min_profitloss']}"""
    return summary_string

#Print summary table to terminal
print(financial_analysis(data_summary))

#Output summary table to txt file
file = open('main_output.txt', 'w')
file.write(financial_analysis(data_summary))
file.close()