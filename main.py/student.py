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
   writer.writerow({"1": "Elle R. Woods", 
                    "2": "2022-1465", 
                    "3": "2nd", 
                    "4": "f", 
                    "5": "BSCS"})
   
   writer.writerow({"1": "Regina T. George", 
                    "2": "2021-0456", 
                    "3": "3rd", 
                    "4": "f", 
                    "5": "BSCS"})
   
   writer.writerow({"1": "Marc M. Jacobs", 
                    "2": "2021-0009", 
                    "3": "3rd", 
                    "4": "m", 
                    "5": "BSIT"})
   
   writer.writerow({"1": "Ian B. Bart", 
                    "2": "2022-0652", 
                    "3": "2nd", 
                    "4": "m", 
                    "5": "BSCS"})
   
   writer.writerow({"1": "Lou Grace R. Yanong", 
                    "2": "2023-1327", 
                    "3": "1st", 
                    "4": "f", 
                    "5": "BSN"})
   
   writer.writerow({"1": "Welma C. Reyes", 
                    "2": "2022-1478", 
                    "3": "2nd", 
                    "4": "f", 
                    "5": "BSCE"})
   
   writer.writerow({"1": "Karen G. Smith",
                    "2": "2021-3133", 
                    "3": "2nd", 
                    "4": "f", 
                    "5": "BSCE"})
   
   writer.writerow({"1": "Merlia P. Summers", 
                    "2": "2021-5737", 
                    "3": "2nd", 
                    "4": "f", 
                    "5": "BSCE"})
   
   writer.writerow({"1": "Kevin D. Mcdonald", 
                    "2": "2023-2133", 
                    "3": "2nd", 
                    "4": "m", 
                    "5": "BSEE"})
   
   writer.writerow({"1": "Brad F. Evans",
                    "2": "2023-4279", 
                    "3": "1st", 
                    "4": "m", 
                    "5": "BSEE"})
   
   writer.writerow({"1": "Lance T. Elliot", 
                    "2": "2023-2133", 
                    "3": "1st", 
                    "4": "m", 
                    "5": "BSEE"})
   
   writer.writerow({"1": "Eli Y. Jang", 
                    "2": "2023-9090", 
                    "3": "1st", 
                    "4": "m", 
                    "5": "BSCS"})
   
   writer.writerow({"1": "Sabrina Y. Yap", 
                    "2": "2021-7879", 
                    "3": "3rd", 
                    "4": "f", 
                    "5": "BSCA"})
   
   writer.writerow({"1": "Selena Marie A. Gomez", 
                    "2": "2020-1211", 
                    "3": "4th", 
                    "4": "f", 
                    "5": "BSCA"})
   
   writer.writerow({"1": "Katy Lorde L. Perry", 
                    "2": "2020-0012", 
                    "3": "4th", 
                    "4": "f", 
                    "5": "BSCA"})
   
   writer.writerow({"1": "Elijah M. West", 
                    "2": "2022-2312", 
                    "3": "2nd", 
                    "4": "m", 
                    "5": "BSME"})
   
   writer.writerow({"1": "John Lloyd K. Ardiente", 
                    "2": "2022-3434", 
                    "3": "2nd", 
                    "4": "m", 
                    "5": "BSME"})
   
   writer.writerow({"1": "Johana Jane L. Dunne", 
                    "2": "2022-9090", 
                    "3": "1st", 
                    "4": "f", 
                    "5": "BSPsych"})
   
   writer.writerow({"1": "Anna T. Wintour",                
                    "2": "2021-7672", 
                    "3": "3rd", 
                    "4": "f", 
                    "5": "BSPsych"})
   
   writer.writerow({"1": "Gretel N. Reid", 
                    "2": "2023-1234", 
                    "3": "1st", 
                    "4": "f", 
                    "5": "BSIT"})
   
   writer.writerow({"1": "Hansel Mark P. Houston", 
                    "2": "2023-3892", 
                    "3": "1st", 
                    "4": "m", 
                    "5": "BSIT"})
   
   writer.writerow({"1": "Bryan L. May", 
                    "2": "2023-0090", 
                    "3": "1st", 
                    "4": "m", 
                    "5": "BSIT"})
   
   writer.writerow({"1": "Krisha Joy B. Gucci", 
                    "2": "2021-2714", 
                    "3": "3rd", 
                    "4": "f", 
                    "5": "BSH"})
   
   writer.writerow({"1": "Yohan K. Jung", 
                    "2": "2022-3423", 
                    "3": "2nd", 
                    "4": "m", 
                    "5": "BSH"})
   
   writer.writerow({"1": "Krystal K. Jung", 
                    "2": "2022-2041", 
                    "3": "2nd", 
                    "4": "f", 
                    "5": "BSH"})
   
