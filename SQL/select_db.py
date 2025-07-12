import mysql.connector

connection = mysql.connector.connect(host='localhost',port='3306',user='root',password='12151014',database='sql_tutorial')

cursor = connection.cursor()

cursor.execute("SELECT T2.name,T1.client_id,T1.total_sales FROM sql_tutorial.works_with AS T1 LEFT JOIN sql_tutorial.employee AS T2 ON T1.emp_id=T2.emp_id;")
records=cursor.fetchall()
for r in records:
    print(r)

cursor.close()
connection.close()