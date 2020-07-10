import psycopg2

#to check data base opening
connection_object = psycopg2.connect(database="test", user="postgres", password="123", host="127.0.0.1", port="5432")
print("Opened the database successfully")

#to add records to table
cursor_object = connection_object.cursor()
cursor_object.execute("INSERT INTO COMPANY (ID,NAME,AGE,SALARY) VALUES (1, 'Ashwin B' , 23 , 50000.00);")
cursor_object.execute("INSERT INTO COMPANY (ID,NAME,AGE,SALARY) VALUES (2, 'Vicky G' , 28 , 90000.00);")
cursor_object.execute("INSERT INTO COMPANY (ID,NAME,AGE,SALARY) VALUES (3, 'Loki O' , 23 , 30000.00);")
connection_object.commit()
connection_object.close()
print("Table records created Successfully")