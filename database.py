import pymysql
from tkinter import messagebox

# establish connection
def connect_database():
    global mycursor, conn # make the variables global so that they can be accessed in all the functions
    try:
        conn = pymysql.connect(host='localhost',user='root',password='181818')
        mycursor = conn.cursor()
    except:
        messagebox.showerror('Error','Something went wrong')
        return

    mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
    mycursor.execute('USE employee_data')
    # Fixed: Added closing parenthesis for the CREATE TABLE query
    mycursor.execute('CREATE TABLE IF NOT EXISTS data(id VARCHAR(20), name VARCHAR(30), phone VARCHAR(10), role VARCHAR(50), gender VARCHAR(10), salary DECIMAL(10,2))')


def insert(id, name, phone, role, gender, salary):
    # print(id, name, role, phone, gender, salary)
    mycursor.execute('insert into data values(%s,%s,%s,%s,%s,%s)',(id, name ,phone, role, gender, salary))
    conn.commit() # commit the changes

def id_exists(id):
    mycursor.execute('select count(*) from data where id=%s', id)
    result = mycursor.fetchone()
    # print(result) # we will get a  tuple as result
    return result[0]>0 # we will return first element of the tuple

def fetch_employee():
    mycursor.execute('select * from data')
    result = mycursor.fetchall()
    return result;

def update(id, new_name, new_phone, new_role, new_gender, new_salary):
    mycursor.execute('update data set name=%s, phone=%s, role=%s, gender=%s, salary=%s where id=%s', (new_name, new_phone, new_role, new_gender, new_salary, id))
    conn.commit() # commit the changes

def delete(id):
    mycursor.execute('delete from data where id=%s', id)
    conn.commit()

def search(label, value):
    mycursor.execute(f'select * from data where {label}=%s', value)
    result=mycursor.fetchall()
    return result

def delete_all_records():
    mycursor.execute('truncate table data')
    conn.commit()


connect_database()
