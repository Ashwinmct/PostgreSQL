import psycopg2


connection_object = psycopg2.connect(database="test", user="postgres", password="123", host="127.0.0.1", port="5432")
cursor_object = connection_object.cursor()
cursor_object.execute("CREATE TABLE employee (id INTEGER PRIMARY KEY,name TEXT NOT NULL,job TEXT NOT NULL);")
connection_object.commit()
with open('C:\\Users\VIGNESH\\PycharmProjects\\PostgreSQL\\postgresql_testing_practice\\resourse\\employee.csv', 'r+') as file:
    next(file)
    cursor_object.copy_from(file, 'employee', sep=',')

cursor_object.execute("SELECT * FROM employee;")
table_rows = cursor_object.fetchall()
print("\nID\tNAME\tEMPLOYEE")
for row in table_rows:
	print("\n{0}\t{1}\t{2}".format(row[0], row[1], row[2]))


