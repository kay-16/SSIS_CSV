import tkinter as tk                 
from tkinter import ttk, filedialog  
import csv                           # //import the csv module
import tkinter.messagebox as mb      


class SSISApp:                 
    def __init__(self, root):  
        self.root = root        
        self.root.title("Simple Student Information System") 
        root.geometry("950x650")                             
        root.resizable(width=True, height=True)     # //allows root resizing of the root window

        self.file_path = ""    # //initialise file_path attribute
        self.data = []         # //initialise data attribute

        self.create_Widgets()  # //call create_Widgets() method to create elements in GUI
        self.open_csv()        # //open_csv() opens and displays CSV file data

     

# define method to create GUI widgets
    def create_Widgets(self):  

    # frame for buttons
        button_frame = tk.Frame(self.root, highlightbackground="light gray", highlightthickness=2, bg="light gray") # //creates a frame for buttons called button_frame
        button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=20) 
        

        # //Saves edited data to student.csv
        Save2_Button = tk.Button(button_frame, text="Save Edited Data", command=self.saveEditedData, 
                                 font=("Arial", 10, "bold"), bg="orange")
        Save2_Button.pack(side=tk.RIGHT, padx=5, pady=5)        

        # //Edits data in student.csv
        EditButton = tk.Button(button_frame, text="Edit Data", command=self.editStudentData, font=("Arial", 10, "bold"),
                               bg="yellow")
        EditButton.pack(side=tk.RIGHT, padx=5, pady=5)        

        # //Return to view student.csv data in the table
        BackButton = tk.Button(button_frame, text="back", command=self.open_csv, font=("Arial", 10, "bold"),
                               bg="black", fg="white")
        BackButton.pack(side=tk.LEFT, padx=5, pady=5)               

        # //Deletes a data in student.csv after a row of data has been selected in the table
        DeleteButton = tk.Button(button_frame, text="Delete Data", command=self.deleteStudentData, font=("Arial", 10, "bold"),
                                 bg="red", fg="white")
        DeleteButton.pack(side=tk.LEFT, padx=5, pady=5)             
        
        # //Saves data to student.csv after inputting
        SaveButton = tk.Button(button_frame, text="Save Data", command=self.save_csv, font=("Arial", 10,"bold"),
                                bg="green", fg="white")
        SaveButton.pack(side=tk.LEFT, padx=5, pady=5)      # //place SaveButton in button_frame



    # exclusive frame for 'Search'
        s_frame = tk.Frame (self.root, highlightbackground="light gray", highlightthickness=1, bg="light gray")
        s_frame.pack(side=tk.TOP, fill=tk.X, padx=20, pady=20)


        tk.Label(s_frame, text="Search by ID no.:", bg="light gray").grid(row=0, column=0)
        self.searchStudentText = tk.Entry(s_frame, width=40)
        self.searchStudentText.grid(row=0, column=1, padx=5, pady=5)


        # //Search or filter students based on ID no.
        SearchButton = tk.Button(s_frame, text="Search", command=self.searchStudent, font=("Arial", 10, "bold"),
                                 bg="white")
        SearchButton.grid(row=0, column=2, padx=5, pady=5)         
        


    # frame for the table, text entry & user label
        tt_frame = tk.Frame(self.root, bg="light gray") # //creates a frame called tt_frame
        tt_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=20, pady=20) # //layout of tt_frame using pack() method

         

    # to dynamically resize rows and columns
        for x in range(7):
            tt_frame.grid_rowconfigure(x, weight=1)

        for y in range(3):
            tt_frame.grid_columnconfigure(y, weight=1)

     

    # labels
        studentNameLabel = tk.Label(tt_frame, text = "Enter Full Name :", bg="light gray") # //label for Student Name input
        studentNameLabel.grid(row=2, column=0, padx=5, pady=5)            # //place label in tt_frame

        studentIDnoLabel = tk.Label(tt_frame, text = "Enter ID no. :", bg="light gray")    # //label for ID no. input
        studentIDnoLabel.grid(row=3, column=0, padx=5, pady=5)          

        studentYrLevelLabel = tk.Label(tt_frame, text = "Enter Year Level :", bg="light gray") # //label for Year Level input
        studentYrLevelLabel.grid(row=4, column=0, padx=5, pady=5)            

        studentGenderLabel = tk.Label(tt_frame, text = "Enter Gender :", bg="light gray")      # //label for Gender input
        studentGenderLabel.grid(row=5, column=0, padx=5, pady=5)             

        studentCourseCodeLabel = tk.Label(tt_frame, text = "Enter Course Code :", bg="light gray")   # //label for Course Code input 
        studentCourseCodeLabel.grid(row=6, column=0, padx=5, pady=5)



    # table 
        self.tree = ttk.Treeview(tt_frame, columns=("Col1","Col2","Col3","Col4","Col5")) # //create Treeview widget within tt_frame
        self.tree.heading("Col1", text="Student Name", anchor="center") 
        self.tree.heading("Col2", text="ID No.", anchor="center")       
        self.tree.heading("Col3", text="Year Level", anchor="center")   
        self.tree.heading("Col4", text="Gender", anchor="center")       
        self.tree.heading("Col5", text="Course Code", anchor="center")  
        self.tree.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")   
        
        self.tree.heading("#0", text="#") # table row starts at index 0
        self.tree.column("#0", width=3, anchor="w")

        for col in ("Col1","Col2","Col3","Col4","Col5"): 
         self.tree.column(col, anchor="w", width=200)

        

    # text entry
        self.nameText = tk.Text(tt_frame, height=1.4, width=38, wrap=tk.NONE) # //student name input
        self.nameText.grid(row=2, column=0, columnspan=3, padx=5, pady=6)   # //layout of each text entry using grid()
        self.nameText.bind("<Tab>", lambda event: self.next_entry_widget_is(event))  
        """when 'tab' key is pressed, it will call function 'next_entry_widget_is' then it will proceed to the next text entry"""

        self.idText = tk.Text(tt_frame, height=1.4, width=38, wrap=tk.NONE) # //ID no. input
        self.idText.grid(row=3, column=0, columnspan=3, padx=5, pady=6)
        self.idText.bind("<Tab>", lambda event: self.next_entry_widget_is(event))

        self.yearlvlText = tk.Text(tt_frame, height=1.4, width=38, wrap=tk.NONE) # //year level input
        self.yearlvlText.grid(row=4, column=0, columnspan=3, padx=5, pady=6)
        self.yearlvlText.bind("<Tab>", lambda event: self.next_entry_widget_is(event))

        self.genderText = tk.Text(tt_frame, height=1.4, width=38, wrap=tk.NONE) # //gender input
        self.genderText.grid(row=5, column=0, columnspan=3, padx=5, pady=6)
        self.genderText.bind("<Tab>", lambda event: self.next_entry_widget_is(event))

        self.courseCodeText = tk.Text(tt_frame, height=1.4, width=38, wrap=tk.NONE) # //course code input
        self.courseCodeText.grid(row=6, column=0, columnspan=3, padx=5, pady=6)
        self.courseCodeText.bind("<Tab>", lambda event: self.next_entry_widget_is(event))


        # //Used when all texts in text entry widget needs to be cleared after being inputted
        ClearButton = tk.Button(tt_frame, text="Clear All Text", 
                                command=self.clearInputData, font=("Arial",10, "bold", "italic"))
        ClearButton.grid(row=6, column=2, columnspan=2, padx=5, pady=5)

        

    # combobox for Course Code
        ttk.Label(tt_frame)
        self.courseChoice = ttk.Combobox(tt_frame, height=10, width=49, state="readonly")
        self.courseChoice.bind ("<<ComboboxSelected>>", lambda event: self.loadStudentData(event)) 
        self.courseChoice.grid(row=7, column=0, columnspan=3, padx=9, pady=9,)
       
        courses = self.loadCourseCSV()
        if courses:
            self.courseChoice["values"] = [f"{code} - {name}" for code, name in courses]
            self.courseChoice.current(0)
        else:
            mb.showerror("Error!", "Failed to load course data.")

   
        

   

        """--------Functions--------""" 
            
# focuses on the next entry widget as "tab" key is pressed
    def next_entry_widget_is(self,event):
        event.widget.tk_focusNext().focus()
        return 'break'
    


# executes in editing a selected student data 
    def editStudentData(self):

        # //this checks if row is selected
        a_selected_item = self.tree.selection()
        if not a_selected_item:
            mb.showerror("Error!", "Please select a row (item) to edit.")
            return

        # //stores the selected index and original data
        self.data_to_be_edited = a_selected_item[0]
        self.orig_data = self.tree.item(a_selected_item)["values"]

        # //populates each text entries with the original data
        self.nameText.delete("1.0", tk.END)
        self.nameText.insert("1.0", self.orig_data[0])

        self.idText.delete("1.0", tk.END)
        self.idText.insert("1.0", self.orig_data[1])

        self.yearlvlText.delete("1.0", tk.END)
        self.yearlvlText.insert("1.0", self.orig_data[2])

        self.genderText.delete("1.0", tk.END)
        self.genderText.insert("1.0", self.orig_data[3])

        self.courseCodeText.delete("1.0", tk.END)
        self.courseCodeText.insert("1.0", self.orig_data[4])

        # //this sets combobox value to the original course code of the selected data
        self.courseChoice.set(self.orig_data[4])



# saves the edited data and updates it to student.csv
    def saveEditedData(self):

        # //checks if there is data to edit
        if self.data_to_be_edited is None: 
            mb.showerror("Error!", "Please select a row (data) to edit.")
            return
        

        # //get the edited data from each text entries 
        studentName_input = self.nameText.get("1.0" ,tk.END).strip()
        IDno_input = self.idText.get("1.0" ,tk.END).strip()
        yearlvl_input = self.yearlvlText.get("1.0" ,tk.END).strip()
        gender_input = self.genderText.get("1.0" ,tk.END).strip()
        courseCode_input = self.courseCodeText.get("1.0" ,tk.END).strip()


        # //checks if the inputed course code is valid/exists in the existing list of courses in course.csv
        courses = self.loadCourseCSV()
        course_code_entered = [code for code, _ in courses ]

        if courseCode_input not in course_code_entered:
            courseCode_input = "N/A"
            print(course_code_entered)

        else:               # //checks if course code text field is empty 
            if not courseCode_input.strip():
                courseCode_input = "Not Enrolled"

        
        # //makes sure each text entries are filled except for 'course code'
        if not all([studentName_input, IDno_input, yearlvl_input, gender_input]):
            mb.showerror("Error!", "Please fill in all entries before saving it.")
            return
        

        # //updates data in treeview
        self.tree.item(self.data_to_be_edited, values=(studentName_input, IDno_input, 
                                                    yearlvl_input, gender_input, courseCode_input))
        
        # //save the newly edited data to student.csv
        updatedData = []
        with open("student.csv", "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row == self.orig_data:
                    row = (studentName_input, IDno_input, yearlvl_input, gender_input, courseCode_input)
                updatedData.append(row)

        with open("student.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(updatedData)
               
        mb.showinfo("Successfully Edited", "Item edited and saved.")

        # //resets selected index and original data
        self.data_to_be_edited = None
        self.orig_data = None

        # //function called as "Clear All Text" button is clicked
        self.clearInputData()



# called when search button is clicked
    def searchStudent(self):
        # //get search entry from entry widget
        search_query = self.searchStudentText.get().strip().lower()

        # //clearing existing items in Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # //filter data based on ID no.
        data_filtered = [row for row in self.data if search_query in row[1].lower()]
        
        # //update Treeview with the filtered data
        for row in data_filtered:
            self.tree.insert("", "end", values=row)

        # //display message if no data is matched from search entry
        if not data_filtered:
            mb.showinfo("No Results", "No matching records found.")



# function called when input data needs to be cleared from all the text widgets
    def clearInputData(self):

        # //clear text(student data) in each text entry widget
        self.nameText.delete("1.0", tk.END)
        self.idText.delete("1.0", tk.END)
        self.yearlvlText.delete("1.0", tk.END)
        self.genderText.delete("1.0", tk.END)
        self.courseCodeText.delete("1.0", tk.END)



# loads the student data within the selected course
    def loadStudentData(self, event=None):
        selectedCourse = self.getSelectedCourse()

        if not selectedCourse:
            return             # //if no course is selected, do nothing 
        
        for item in self.tree.get_children(): # //clear existing data in Treeview
            self.tree.delete(item)

        # //reads all student data from CSV file into memory
        with open("student.csv", "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            student_data = [row for row in reader]

        # //filter data based on selected course
        filteredData = [row for row in student_data if row[4] == selectedCourse]

        # //update Treeview with filtered data
        for row in filteredData:
            self.tree.insert("", "end", values=row)

        # //update the 'self.data attribute if needed
        self.data = filteredData

        # //display filtered data in Treeview
        self.display_csv_data()

        print("Selected course data:", filteredData)
        


# returns the selected value (course code) from the combobox
    def getSelectedCourse(self):
        selectedCourse = self.courseChoice.get().split(" - ")[0] # //extract course code from selected values
        return selectedCourse



# load course data from course.csv
    def loadCourseCSV(self):
        try:
            with open("course.csv", "r", newline="", encoding="utf=8") as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                courses = [(row[0], row[1]) for row in reader]
                return courses
                
        except FileNotFoundError:
            mb.showerror("File Not Found", "course.csv not found.")
            return []
        
        except Exception as e:
            mb.showerror("Error", f"An error has occurred: {e}")



# to open CSV file
    def open_csv(self):
        filePath = "student.csv" 
        self.filePath = filePath # //set function filePath to the value of filePath

        if filePath:
            self.filePath = filePath
            with open(filePath, newline="") as csvfile:
                csv_reader = csv.reader(csvfile)
                self.data = list(csv_reader)
                self.display_csv_data()             # //displays the data
                self.tree.column("#0", width=3)



# to save the existing data
    def save_csv(self):
        if self.filePath:
            with open(self.filePath, 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)

        # //get data from each text entries
                student_name_input = self.nameText.get('1.0', tk.END).strip()
                student_IDno_input = self.idText.get('1.0', tk.END).strip()
                student_yearlvl_input = self.yearlvlText.get('1.0', tk.END).strip()
                student_gender_input = self.genderText.get('1.0', tk.END).strip()
                student_coursecode_input = self.courseCodeText.get('1.0', tk.END).strip()

        # //checks if the inputted course code is valid/exists in the existing list of courses in course.csv
                courses = self.loadCourseCSV()
                course_code_entered_2 = [code for code, _ in courses ]

                if student_coursecode_input not in course_code_entered_2:
                        student_coursecode_input = "N/A"
                        print(course_code_entered_2)

                 # //if no course code is inputted
                else:
                    if student_coursecode_input.strip() is course_code_entered_2:
                        student_coursecode_input = "Not Enrolled"

        # //checks if any text entry is empty, except for course code entry
                if not all([student_name_input, student_IDno_input, 
                            student_yearlvl_input, student_gender_input]):
                    mb.showerror("Error!", "Please fill in all text entries before saving.")
                    return
                
        # //writes data to student.csv
                csv_writer.writerow([student_name_input, student_IDno_input, student_yearlvl_input, 
                                     student_gender_input, student_coursecode_input])


        # //reload data from student.csv
        self.open_csv()

        mb.showinfo("Saved Data", "Data has been saved successfully.")



# confirms deletion
    def deleteStudentData(self):
        select_a_row = self.tree.selection()
        if select_a_row:
        # //confirmation delete message
            confirmation = mb.askyesno("You're about to delete a data", 
                                       "Are you sure you want to delete this student's data?") 
            
            """prompt message that asks user, if they want to delete the data"""                                                                           

            if confirmation: # //if 'yes', executeDeleteData function will be called
                self.executeDeleteData()
                
        else:       # //otherwise, if a row isn't selected, a prompt message will ask user to select a row
            mb.showerror("Error!", "Please select a row to delete.")



# actually removes the selected row of data from student.csv
    def executeDeleteData(self):
        select_a_row = self.tree.selection()    # //selects a row from the table
        if select_a_row:                        # //if a row is selected
            select_an_item = self.tree.item(select_a_row) # //
            studentData = select_an_item["values"]
            s_identifier = studentData[1]

            with open("student.csv", "r", newline="") as csvfile:
                reader = csv.reader(csvfile)
                data = [row for row in reader]

            updatedDataNow = [row for row in data if row[1] != s_identifier]

            with open("student.csv", "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(updatedDataNow)

            self.open_csv()
            mb.showinfo("Data Successfully Deleted", f"Row with ID {s_identifier} was removed from student.csv file.")

        else: 
            mb.showerror("Error!", "Please select a row to delete.")



# displays existing data in the table
    def display_csv_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        widthColumn = []
        if self.data:                           # //checks if data is not empty 
            for k in range(len(self.data[0])):  # //use the length of first row to determine no. of columns
                columnsData =  [row[k] for row in self.data if k < len(row)]   # //checks 'k' for all the length of rows
                widthMaxx = max(len(str(k)) for k in columnsData)
                widthColumn.append(widthMaxx)

        # //insert data into the table 
        for k, row in enumerate(self.data, start=0):
            self.tree.insert("", "end", text=str(k), values=row)

        # //adjusts column width dynamically
            for l, item in enumerate(row):
                self.tree.column(l, width=max(130, 10 + 7 * widthColumn[l])) 

        else:
            print("No data to display")

    

if __name__ == "__main__":
    root = tk.Tk()
    app = SSISApp(root)
    root.mainloop()
    
    
