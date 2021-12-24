import pyodbc 
import numpy as np
from datetime import datetime
import sys



server = 'LAPTOP-2J9AEQ6E'
database = 'PasswordCreatorDB'

try:

    connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};" #connect to db
                              "Server=" + server + ";"
                              "Database=" + database + ";"
                              "Trusted_Connection=yes;")
except: 
    print("There is no connection to the database or a problem with the connection string")
    sys.exit(1) #remeber to add the exit from the program, so it will not continue and create unhandled problems
else:

    try:
        conn = pyodbc.connect = (connection)
        cursor = conn.cursor() 
        
    except:
        print("There was a problem connecting to the database ")
        sys.exit(1)
    else:
        for n in range(4):
            idn = str(np.random.randint(1, 60453))
            try:
                cursor.execute("exec sp_choose_words " + idn ) #execute the stored procedure
            except:
                print("There was a problem with retriving the data")
                sys.exit(1)
            else:
  

                for row in cursor: #transform the cursor in a normal string and delete the characters not needed
                    word = str(row) 
                    sc  ="(',) [\]^_`{|}~'()*+, -./:;<>"
                    for s in sc:
                        word = word.replace(s, "").capitalize() 
                        print (idn)
                words = word + word + str(np.random.randint(1,9))
    

            print(words)

