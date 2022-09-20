import mysql.connector
import xlrd

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Salman@0097'
)

mycursor = mydb.cursor()

# Create Database
mycursor.execute("CREATE DATABASE AmazonProducts")

# Use Database
mycursor.execute("USE AmazonProducts")

# Create table
mycursor.execute(
    "CREATE TABLE Amazon_Products (Product_Id int, Product_Name varchar(255), Brand varchar(255), Category varchar(255), Price float)")

l = []

loc = ("E:\\Data Science\\Amazon Products.xls")

wb = xlrd.open_workbook(loc)

sheet = wb.sheet_by_index(0)

sheet.cell_value(0, 0)

for i in range(1, 11):
    l.append(tuple(sheet.row_values(i)))
# insert
q = "insert into Amazon_Products(Product_Id,Product_Name,Brand,Category,Price)values(%s,%s,%s,%s,%s)"

mycursor.executemany(q, l)

mydb.commit()

mydb.close()
