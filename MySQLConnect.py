import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Salman@0097"
)
mycursor = mydb.cursor()

mycursor.execute("USE SalmanDB")
# mycursor.execute("CREATE TABLE Persons (PersonID int,LastName varchar(255),FirstName varchar(255),Address varchar(255),City varchar(255))")
mycursor.execute("SHOW TABLES")
# mycursor.execute("INSERT INTO Persons VALUES (2,'Setia','Simran','Ramanujan Block','Ropar')")
# mycursor.execute("SELECT * FROM Persons")
#mycursor.execute("DROP TABLE customers_details")

for x in mycursor:
  print(x)
