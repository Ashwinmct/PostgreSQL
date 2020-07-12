import psycopg2

def print_table_details(cursor_object, message):
	print(message)
	cursor_object.execute("SELECT id, name, salary FROM COMPANY;")
	table_rows = cursor_object.fetchall()
	print("\nID\tNAME\tSALARY")
	for row in table_rows:
		print("\n{0}\t{1}\t{2}".format(row[0], row[1], row[2]))



#to check data base opening
connection_object = psycopg2.connect(database="test", user="postgres", password="123", host="127.0.0.1", port="5432")
print("Opened the database successfully")
cursor_object = connection_object.cursor()
#to UPDATE table records
cursor_object.execute("CREATE TABLE DEPARTMENTS(id INTEGER PRIMARY KEY NOT NULL,department TEXT NOT NULL,employee_id INTEGER NOT NULL);")
connection_object.commit()
print("Table created successfully")
cursor_object.execute("INSERT INTO DEPARTMENTS (id, department, employee_id) VALUES (1, 'IT Billing', 1 ),(2, 'Engineering', 2 ),(3, 'Finance', 7 );")
connection_object.commit()
connection_object.close()
print("Table records updated and displayed Successfully")
