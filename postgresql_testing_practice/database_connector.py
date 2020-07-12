import psycopg2


def print_table_details(cursor_object):
	table_rows = cursor_object.fetchall()
	print("\nID\tNAME\tDEPARTMENT")
	for row in table_rows:
		print("\n{0}\t{1}\t{2}".format(row[0], row[1], row[2]))


connection_object = psycopg2.connect(database="test", user="postgres", password="123", host="127.0.0.1", port="5432")
print("Opened the database successfully")
cursor_object = connection_object.cursor()
cursor_object.execute("SELECT EMPLOYEE_ID, NAME, DEPARTMENT FROM COMPANY FULL OUTER JOIN DEPARTMENTS ON COMPANY.ID = DEPARTMENTS.EMPLOYEE_ID;")
print_table_details(cursor_object)
connection_object.close()
