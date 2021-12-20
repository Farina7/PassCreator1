import pyodbc 
import random as r

server = 'LAPTOP-2J9AEQ6E'
database = 'PasswordCreatorDB'

ix = r.randint(1, 60453)
idn = str(ix)
connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=" + server + ";"
                      "Database=" + database + ";"
                      "Trusted_Connection=yes;")
conn = pyodbc.connect = (connection)

cursor = conn.cursor()
cursor.execute("exec sp_choose_words " + idn )
for i in cursor:
    print(i)