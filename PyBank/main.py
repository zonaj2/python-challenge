import os
import csv
budget_csv = os.path.join("Resources", "budget_data.csv")

Months =[]
Profit_loss = []
with open(budget_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        Months.append(row[0])
        Profit_loss.append(row[1])
    Profit_loss = [int(i) for i in Profit_loss]
    #print(Profit_loss)
Total_Months = len(Months)
Total_Profit = sum(Profit_loss)
Avg_Difference = round((Profit_loss[-1] - Profit_loss[0]) / ((Total_Months)- 1),2)

monthly_profit_change = []
for i in range(len(Profit_loss) - 1):
    monthly_profit_change.append(Profit_loss[i + 1] - Profit_loss[i])
    #print (monthly_profit_change)
max_increase_value = max(monthly_profit_change)
max_increase_index = monthly_profit_change.index(max_increase_value)
max_increase_month = Months[max_increase_index + 1]

max_decrease_value = min(monthly_profit_change)
max_decrease_index = monthly_profit_change.index(max_decrease_value)
max_decrease_month = Months[max_decrease_index + 1]

print(f'Financial Analysis')
print(f'-------------------------')
print(f'Total Months: {Total_Months}')
print(f'Total:  ${Total_Profit}')
print(f'Average Difference: {Avg_Difference}')
print(f"Greatest Increase in Profits: {max_increase_month} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {max_decrease_month} (${(str(max_decrease_value))})")

output = (
f'\n'
f'Financial Analysis\n'
f'-------------------------\n'
f'Total Months: {Total_Months}\n'
f'Total:  ${Total_Profit}\n'
f'Average Change: ${Avg_Difference}\n'
f"Greatest Increase in Profits: {max_increase_month} (${(str(max_increase_value))})\n"
f"Greatest Decrease in Profits: {max_decrease_month} (${(str(max_decrease_value))})\n")

# Set variable for output file
output_file = os.path.join("analysis","budget.txt")
#  Open the output file
with open(output_file, "w") as txt_file:
    txt_file.write(output)
