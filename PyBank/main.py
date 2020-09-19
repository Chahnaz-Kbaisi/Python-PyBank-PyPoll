# Importing Modules/Dependencies
import os
import csv

# creating the path
csvpath = os.path.join('Resources', 'budget_data.csv')

# open & read in csvfile
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

# creating variables for calcualtions
    Months = []
    Profit = []
    Losses = []
    
    Profit_changes = []
    Previous_profit = 0
    Profit_Sum = 0
    
# for loop through data
    for rows in csvreader:
        Current_profit = int(rows[1])
        Months.append(rows[0])
        Profit.append(int(rows[1]))
        Profit_Sum = Profit_Sum + int(rows[1])
        Profit_changes.append(Current_profit - Previous_profit)
        Previous_profit = Current_profit

        
    TotalNumberMonths = len(Months) 
    Profit_change_month = sum(Profit_changes[1:]) / (TotalNumberMonths - 1)
    Profit_month = Profit_Sum / TotalNumberMonths    
    Greatest_increase = max(Profit_changes)
    Greatest_month = Months[Profit_changes.index(Greatest_increase)]
    Greatest_decrease = min(Profit_changes)
    Greatest_dec_month = Months[Profit_changes.index(Greatest_decrease)]


# Print Statements:
    print("'''text")
    print("Finalcial Analysis")
    print("----------------------------------------")
    print("Total Months: " + str(TotalNumberMonths))  
    print("Total: " + "$" + str(Profit_Sum))
    print("Average Change: " + "$" + str(round(Profit_change_month, 2)))
    print("Greatest Increase in Profits: " + str(Greatest_month) + "($" + str(Greatest_increase) + ")" ) 
    print("Greatest Decrease in Profits: " + str(Greatest_dec_month) + "($" + str(Greatest_decrease) + ")" )
    print("'''")
      
# Setting the file to write to outputs

output_file = os.path.join("Analysis", "output.csv")


# opening the file using write mode
with open(output_file, "w") as datafile:
    
# Initializing csv writer    
    writer = csv.writer(datafile)

    writer.writerow(["'''text"])
    writer.writerow(["Financial Analysis"])
    writer.writerow(["-------------------------------------------------------------"])
    writer.writerow(["Total Months: " + str(TotalNumberMonths)])
    writer.writerow(["Totals: " + "$" + str(Profit_Sum)])
    writer.writerow(["Average Change: " + "$" + str(round(Profit_change_month, 2))])
    writer.writerow(["Greatest Increase in Profits: " + str(Greatest_month) + "($" + str(Greatest_increase) + ")"])
    writer.writerow(["Greatest Decrease in Profits: " + str(Greatest_dec_month) + "($" + str(Greatest_decrease) + ")"])
    writer.writerow(["'''"])   





    


    


        
       

   
     
  

    
    
