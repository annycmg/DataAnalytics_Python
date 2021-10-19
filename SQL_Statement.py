####### DATABASE AND PYTHON ########
# Connect to SQL Server database using pyodbc
import pyodbc 

server = 'tcp:myserver.database.windows.net' 
database = 'mydb' 
username = 'myusername' 
password = 'mypassword' 
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()

query = cursor.execute('SELECT * FROM table01')

query2 = cursor.execute("INSERT INTO table01 (Name, Age, StandardCost, ListPrice, SellStartDate) \
                        VALUES ('?',?,?,?,?)", 'Anny', 26, 3175, 3, '2021-10-19')
conn.commit()
conn.close()

# Connect to SQL Server database using pymssql
import pymssql  

conn2 = pymssql.connect(server='yourserver.database.windows.net', user='yourusername@yourserver', password='yourpassword', database='AdventureWorks')  
cursor = conn2.cursor()  

query3 = cursor.execute("INSERT INTO table01 (Name, Age, StandardCost, ListPrice, SellStartDate) \ 
                         VALUES ('Anny', 26, 3175, 3, '2021-10-19')")  
conn2.commit()
conn2.close()




