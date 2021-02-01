import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="mis_user",
  password="india#123",
  database="myadmin"

)

mycursor = mydb.cursor()
sql="insert into users (name ,address) values(%s,%s)"
val=("rushi","highway")

mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
