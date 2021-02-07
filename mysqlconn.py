import mysql.connector# first install mysql connector 
mydb = mysql.connector.connect(
  host="localhost",   # mention your mysql user,host,password,and database
  user="mis_user",
  password="india#123",
  database="myadmin"

)

mycursor = mydb.cursor()
sql="insert into users (name ,address) values(%s,%s)"   #insert data into myadmin.users table
val=("rushi","highway")

mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
