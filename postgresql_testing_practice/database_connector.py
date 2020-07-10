import psycopg2

conn = psycopg2.connect(database="test", user="postgres", password="123", host="127.0.0.1", port="5432")
print("Opened the database successfully")
