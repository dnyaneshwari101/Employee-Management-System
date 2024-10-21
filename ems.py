from customtkinter import *
from tkinter import ttk # for tree view
from tkinter import messagebox
import database

# Functions

def update_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error','select data to update')

    else:
        database.update(idEntry.get(), nameEntry.get(), phoneEntry.get(), roleBox.get(), genderBox.get(), salaryEntry.get())
        treeview_data() # displays updated data on the tree view
        clear() # clear the entry fields after updating
        messagebox.showinfo('Success','Data updated')

def add_employee(): #adding the employee to database and treeview
    id = idEntry.get()
    phone = phoneEntry.get()
    name = nameEntry.get()
    salary = salaryEntry.get()
    role = roleBox.get()
    gender = genderBox.get()

    if not id or not phone or not name or not salary:
        messagebox.showerror('Error','All fields are required')

    elif database.id_exists(idEntry.get()):
        messagebox.showerror('Error','ID already exists')

    elif not idEntry.get().startswith('EMP'):
        messagebox.showerror('Error','Invalid ID format')

    else:
        database.insert(id,name,phone,role,gender,salary)
        treeview_data()
        clear() # clears all the fields once the data is inserted
        messagebox.showinfo('Success','Employee added')

def delete_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select data to delete')

    else:
        database.delete(idEntry.get())
        treeview_data() # displays the updated data
        clear() # clears the selection
        messagebox.showinfo('Success','Data deleted')
def clear(value=False): # clears all the fields once the data is inserted
    if value:
        tree.selection_remove(tree.focus()) # when a new employee button is clicked, the selected row will be deselected
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    salaryEntry.delete(0, END)
    roleBox.set(role_options[0])
    genderBox.set('Male')
def treeview_data(): # displays the employee data on treeview after fetching from the database
    employees = database.fetch_employee()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('',END, values = employee)

# function so that the fields on left frame get filled automatically after selecting row in the treeview
def selection(event):
    selected_item = tree.selection()
    # print(selected_item)
    if selected_item :
        row = tree.item(selected_item)['values'] # values of selected row is stored in row tuple
        # print(row)
        clear() # clear existing values from the fields
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0,row[5])

# search button functionality
def search_employee():
    value = searchEntry.get()
    if not value:
        messagebox.showerror('Error','Enter value to search')
    elif searchBox.get() == 'Search By':
        messagebox.showerror('Error','Please select search by option')
    else:
        search_data=database.search(searchBox.get(), searchEntry.get())
        #print(search_data)
        # display only searched result
        tree.delete(*tree.get_children())
        for employee in search_data:
            tree.insert('',END, values=employee)

def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchBox.set('Search By')

def delete_all():
    result = messagebox.askyesno('Confirm','Are you sure you want to delete all the records?')
    if result:
        database.delete_all_records()
        treeview_data()

# GUI part
window = CTk()
window.geometry('1250x700+100+100') # window of size 1200x700 will be displayed on screen 100 distance from x and 100 distance from y axis
window.configure(fg_color='#2D347A')
window.resizable(0, 0)
window.title('Employee Management System')

leftFrame = CTkFrame(window, width=250, height=700, fg_color='#2D347A')
leftFrame.grid(row=0, column=0)

rightFrame = CTkFrame(window, width=950, height=700, fg_color='#7A8CB4')
rightFrame.grid(row=0, column=1, padx=40, pady=20)

# Corrected label to use fg_color instead of bg_color
idLabel = CTkLabel(leftFrame, text='ID', fg_color='#2D347A', font=('times new roman', 20, 'bold'), text_color='white')
idLabel.grid(row=0, column=0, padx=20, pady=20, sticky='w')

idEntry = CTkEntry(leftFrame, font=('times new roman', 15, 'bold'), width=180)
idEntry.grid(row=0, column=1, pady=20)

nameLabel = CTkLabel(leftFrame, text='Name', fg_color='#2D347A', font=('times new roman', 20, 'bold'), text_color='white')
nameLabel.grid(row=1, column=0, padx=20, pady=20, sticky='w')

nameEntry = CTkEntry(leftFrame, font=('times new roman', 15, 'bold'), width=180)
nameEntry.grid(row=1, column=1, pady=20)

phoneLabel = CTkLabel(leftFrame, text='Phone', fg_color='#2D347A', font=('times new roman', 20, 'bold'), text_color='white')
phoneLabel.grid(row=2, column=0, padx=20, pady=20, sticky='w')

phoneEntry = CTkEntry(leftFrame, font=('times new roman', 15, 'bold'), width=180)
phoneEntry.grid(row=2, column=1, pady=20)

# Role
roleLabel = CTkLabel(leftFrame, text='Role', fg_color='#2D347A', font=('times new roman', 20, 'bold'), text_color='white')
roleLabel.grid(row=3, column=0, padx=20, pady=10, sticky='w')

role_options = [
    "Application Developer",
    "Business Analyst",
    "Cloud Engineer",
    "Data Analyst",
    "Data Engineer",
    "Data Scientist",
    "Database Administrator",
    "DevOps Engineer",
    "Full Stack Developer",
    "Helpdesk Support",
    "Information Security Analyst",
    "Infrastructure Engineer",
    "IT Consultant",
    "Mobile Application Developer",
    "Network Engineer",
    "Project Manager",
    "QA Engineer",
    "Scrum Master",
    "Software Engineer",
    "Solution Architect",
    "Systems Analyst",
    "Technical Lead",
    "Technical Support Engineer",
    "Test Automation Engineer",
    "UI/UX Designer",
    "Web Developer"
]
roleBox=CTkComboBox(leftFrame, values=role_options, width=180,font=('times new roman', 15, 'bold'), state='readonly')
roleBox.grid(row=3,column=1)
roleBox.set(role_options[0]) # set default option

# Gender
genderLabel = CTkLabel(leftFrame, text='Gender', fg_color='#2D347A', font=('times new roman', 20, 'bold'), text_color='white')
genderLabel.grid(row=4, column=0, padx=20, pady=10, sticky='w')
gender_options=['Male','Female','Other']
genderBox=CTkComboBox(leftFrame, values=gender_options, width=180,font=('times new roman', 15, 'bold'), state='readonly')
genderBox.grid(row=4,column=1)
genderBox.set('Male')

# salary
salaryLabel = CTkLabel(leftFrame, text='Salary', fg_color='#2D347A', font=('times new roman', 20, 'bold'), text_color='white')
salaryLabel.grid(row=5, column=0, padx=20, pady=10, sticky='w')

salaryEntry = CTkEntry(leftFrame, font=('times new roman', 15, 'bold'), width=180)
salaryEntry.grid(row=5, column=1, pady=10)

# Right Frame
#create a new frame
container=CTkFrame(rightFrame,fg_color='#7A8CB4')
container.grid(row=0, column=0, padx=20,pady=20)

#combo box for search options
search_options=['ID','Name','Phone','Role','Gender','Salary']
searchBox = CTkComboBox(container, values=search_options, state='readonly',font=('times new roman',20,'bold'),width=150,height=40)
searchBox.grid(row=0,column=0, pady=20)
searchBox.set('Search By')

#Entry box for searching
searchEntry=CTkEntry(container,font=('times new roman',20,'bold'),width=250,height=40)
searchEntry.grid(row=0,column=1)

#search button
searchButton=CTkButton(container, text='Search', width=100,height=40,fg_color='#D6B295',font=('times new roman',20,'bold'),text_color='black', command = search_employee)
searchButton.grid(row=0,column=2)

# button to show all the records
showAllButton=CTkButton(container, text='Show all', width=100, height=40, fg_color='#D6B295',font=('times new roman',20,'bold'),text_color='black', command = show_all)
showAllButton.grid(row=0, column=3)

# creating a trr view for displaying the records
tree=ttk.Treeview(container, height=10)
tree.grid(row=1,column=0, columnspan=4)

tree['columns']=('ID','Name','Phone','Role','Gender','Salary')
tree.heading('ID', text='ID')
tree.heading('Name', text='Name')
tree.heading('Phone', text='Phone')
tree.heading('Role', text='Role')
tree.heading('Gender', text='Gender')
tree.heading('Salary', text='Salary')

tree.config(show='headings') # remove default column
tree.column('ID',anchor=CENTER,width=150)
tree.column('Name',anchor=CENTER,width=250)
tree.column('Phone',anchor=CENTER,width=150)
tree.column('Role',anchor=CENTER,width=200)
tree.column('Gender',anchor=CENTER,width=100)
tree.column('Salary',anchor=CENTER,width=150)

style=ttk.Style()
style.configure('Treeview.Heading', font=('times new roman', 20, 'bold'))
style.configure("Treeview", font=('times new roman', 15, 'bold'), rowheight=40)

#  add sroll bar
scrollbar=ttk.Scrollbar(rightFrame, orient= VERTICAL, command=tree.yview)
scrollbar.grid(row=1, column=4, sticky='ns')
tree.config(yscrollcommand = scrollbar.set)
#scrollbar.config(command=tree.yview)

# button frame

buttonFrame = CTkFrame(window)
buttonFrame.configure(bg_color='#2D347A',fg_color='#2D347A')
buttonFrame.grid(row=2, column=0, columnspan=2)

newButton = CTkButton(buttonFrame, text='New employee',bg_color='#2D347A',fg_color='#D6B295',font=('times new roman',20,'bold'),text_color='black', height=40, command = lambda: clear(True))
newButton.grid(row=0,column=0, padx=20, pady=10)

addButton = CTkButton(buttonFrame, text='Add employee',bg_color='#2D347A',fg_color='#D6B295',font=('times new roman',20,'bold'),text_color='black', height=40, command=add_employee)
addButton.grid(row=0, column=1, padx=20, pady=10)

updateButton = CTkButton(buttonFrame, text='Update employee',bg_color='#2D347A',fg_color='#D6B295',font=('times new roman',20,'bold'),text_color='black', height=40, command = update_employee)
updateButton.grid(row=0, column=2, padx=20, pady=10)

deleteButton = CTkButton(buttonFrame, text='Delete employee',bg_color='#2D347A',fg_color='#D6B295',font=('times new roman',20,'bold'),text_color='black', height=40, command=delete_employee)
deleteButton.grid(row=0, column=3, padx=20, pady=10)

deleteAllButton = CTkButton(buttonFrame, text='Delete all',bg_color='#2D347A',fg_color='#D6B295',font=('times new roman',20,'bold'),text_color='black', height=40, command=delete_all)
deleteAllButton.grid(row=0, column=4, padx=20, pady=10)

treeview_data() # in order to see the existing employee data as we run the application
window.bind('<ButtonRelease>', selection)
window.mainloop()