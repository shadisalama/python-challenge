
import csv, os

file_to_open = os.path.join("Resources", "budget_data.csv")
file_to_export = os.path.join("Exported", "budget_analysis.txt")

total_months = 0
total_net = 0

month_of_change = []
net_change_list = []

greatest_decrease = ["", 10000000000000000]
greatest_increase = ["", 0]

with open(file_to_open) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)
    first_row = next(reader)

    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        total_months = total_months + 1
        total_net = total_net + int(row[1])

        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

net_monthly_avg = sum(net_change_list) / len(net_change_list)

output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(output)

with open(file_to_export, "w") as txt_file:
    txt_file.write(output)
