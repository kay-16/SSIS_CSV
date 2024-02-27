import csv

# write csv file
with open('student.csv', mode='w', newline='', encoding='utf-8') as csvfile:
   fieldnames = ["1", "2", "3", "4", "5"]

# to append data in csv file
with open('student.csv', mode='a', newline='', encoding='utf-8') as csvfile:
   fieldnames = ["1", "2", "3", "4", "5"]
   
   
# creating a csv dict writer object
   writer = csv.DictWriter(csvfile,  fieldnames=fieldnames)

# writing headers (fieldnames)
   writer.writeheader()

# writing data rows
   writer.writerow({"1": "Elle Woods", 
                    "2": "2022-1465", 
                    "3": "2nd", 
                    "4": "f", 
                    "5": "BSCS"})
   
   writer.writerow({"1": "Regina George", 
                    "2": "2021-0456", 
                    "3": "3rd", 
                    "4": "f", 
                    "5": "BSCS"})
   
   writer.writerow({"1": "Marc Jacobs", 
                    "2": "2021-0456", 
                    "3": "3rd", 
                    "4": "m", 
                    "5": "BSIT"})
   
   writer.writerow({"1": "Ian Bart", 
                    "2": "2022-0652", 
                    "3": "2nd", 
                    "4": "m", 
                    "5": "BSCS"})
   
   writer.writerow({"1": "Lou Grace Yanong", 
                    "2": "2023-1327", 
                    "3": "1st", 
                    "4": "f", 
                    "5": "BSN"})
   
   writer.writerow({"1": "Elle Woods", 
                    "2": "2022-1465", 
                    "3": "2nd", 
                    "4": "f", 
                    "5": "BSCS"})
   
   writer.writerow({"1": "Elle Woods", 
                    "2": "2022-1465", 
                    "3": "2nd", 
                    "4": "f", 
                    "5": "BSCS"})
   
   writer.writerow({"1": "Elle Woods", 
                    "2": "2022-1465", 
                    "3": "2nd", 
                    "4": "f", 
                    "5": "BSCS"})
   
   writer.writerow({"1": "Elle Woods", 
                    "2": "2022-1465", 
                    "3": "2nd", 
                    "4": "f", 
                    "5": "BSCS"})
   
   writer.writerow({"1": "Elle Woods", 
                    "2": "2022-1465", 
                    "3": "2nd", 
                    "4": "f", 
                    "5": "BSCS"})