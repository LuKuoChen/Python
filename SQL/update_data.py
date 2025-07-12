import mysql.connector

connection = mysql.connector.connect(host='localhost',port='3306',user='root',password='12151014',database='sql_tutorial')

cursor = connection.cursor()

cursor.execute("UPDATE 'branch' SET XXXXX")

cursor.close()
connection.commit()
connection.close()