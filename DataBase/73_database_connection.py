import mysql.connector

connection = mysql.connector.connect(host="localhost", user="root", passwd="mysql", database="telusko")
myCursor = connection.cursor()

query = "INSERT INTO employees VALUES(3,'Ayesha',12000,'Teacher')"

try:
    # myCursor.execute("insert into studen values('Yaser','iqra School');")
    myCursor.execute(query)
    connection.commit()
    print('Data Added Successfully..')
except Exception as e:
    print('There is an Error occurs :')
    print("Have an Exception {}".format(e))
    connection.rollback()
finally:
    connection.close()

# myCursor.execute("select * from student")


# result = myCursor.fetchall()

# for i in result:
#     print(i)
