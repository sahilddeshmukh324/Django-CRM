import mysql.connector

database=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Deshmukh@1010'
)

cursorObject=database.cursor()


cursorObject.execute("CREATE DATABASE sahil")

print("All done !!")
