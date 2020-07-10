import psycopg2

#to check data base opening
connection_object = psycopg2.connect(database="test", user="postgres", password="123", host="127.0.0.1", port="5432")
print("Opened the database successfully")

#to check table creation
cursor_object = connection_object.cursor()
cursor_object.execute('''CREATE TABLE COMPANY
						(ID INT PRIMARY KEY  NOT NULL,
						NAME TEXT  NOT NULL,
						AGE INT  NOT NULL,
						SALARY REAL);''')
connection_object.commit()
connection_object.close()
print("Table Created Successfully")