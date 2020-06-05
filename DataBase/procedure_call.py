import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="mysql", database="telusko")
myCursor = conn.cursor()

myCursor.callproc('GetAllEmployees')

# results = [r.fetchall() for r in myCursor.stored_results()]

data = []
for i in myCursor.stored_results():
    for result in i:
        print("Id = ", result[0])
        print("Name = ", result[1])
        print("Salary = ", result[2])
        print("Designation = ", result[3])
