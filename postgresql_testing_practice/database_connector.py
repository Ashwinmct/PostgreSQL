import psycopg2

#to check data base opening
connection_object = psycopg2.connect(database="test", user="postgres", password="123", host="127.0.0.1", port="5432")
print("Opened the database successfully")

#to display table records
cursor_object = connection_object.cursor()
cursor_object.execute("SELECT id, name, salary FROM COMPANY;")
table_rows = cursor_object.fetchall()
for row in table_rows:
	print("ID=",row[0])
	print("NAME=", row[1])
	print("SALARY=", row[2])
connection_object.commit()
connection_object.close()
print("Table records displayed Successfully")