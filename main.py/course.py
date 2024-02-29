import csv

# reading csv file
with open('course.csv', mode='w', newline='', encoding='utf-8') as csvfile:
   fieldnames = ["Course Code", "Course Name"]

with open('course.csv', mode='a', newline='', encoding='utf-8') as csvfile:
   fieldnames = ["Course Code", "Course Name"]

# creating a csv dict writer object
   writer = csv.DictWriter(csvfile,  fieldnames=fieldnames)

# writing headers (fieldnames)
   writer.writeheader()

# writing data rows
   writer.writerow({"Course Code": "BSCS", 
                    "Course Name": "Bachelor of Science in Computer Science"})
   
   writer.writerow({"Course Code": "BSIT", 
                    "Course Name": "Bachelor of Science in Information Technology"})
   
   writer.writerow({"Course Code": "BSN", 
                    "Course Name": "Bachelor of Science in Nursing"})
   
   writer.writerow({"Course Code": "BSCA", 
                    "Course Name": "Bachelor of Science in Computer Application"})
   
   writer.writerow({"Course Code": "BSCE", 
                    "Course Name": "Bachelor of Science in Computer Engineering"})
   
   writer.writerow({"Course Code": "BSEE", 
                    "Course Name": "Bachelor of Science in Electrical Engineering"})
   
   writer.writerow({"Course Code": "BSCE", 
                    "Course Name": "Bachelor of Science in Civil Engineering"})
   
   writer.writerow({"Course Code": "BSPsych", 
                    "Course Name": "Bachelor of Science in Pyschology"})
   
   writer.writerow({"Course Code": "BSIS", 
                    "Course Name": "Bachelor of Science in Information System"})
   
   writer.writerow({"Course Code": "BSME", 
                    "Course Name": "Bachelor of Science in Mechanical Engineering"})
   
   writer.writerow({"Course Code": "BAH", 
                    "Course Name": "Bachelor of Arts in History"})

   
