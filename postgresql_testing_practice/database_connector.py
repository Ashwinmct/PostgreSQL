import psycopg2

def print_table_details(cursor_object, message):
	print(message)
	cursor_object.execute("SELECT id, name, salary FROM COMPANY;")
	table_rows = cursor_object.fetchall()
	for row in table_rows:
		print("ID=", row[0])
		print("NAME=", row[1])
		print("SALARY=", row[2])

#to check data base opening
connection_object = psycopg2.connect(database="test", user="postgres", password="123", host="127.0.0.1", port="5432")
print("Opened the database successfully")

cursor_object = connection_object.cursor()
print_table_details(cursor_object, "table details before changing")

#to UPDATE table records
cursor_object.execute("UPDATE COMPANY set SALARY = 70000 WHERE ID = 3;")
connection_object.commit()

print_table_details(cursor_object, "table details after changing")
connection_object.close()
print("Table records updated and displayed Successfully")