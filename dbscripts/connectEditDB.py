#!/usr/bin/python
import MySQLdb

# Open database connection
# connect(<endpoint of RDS>, <dbusername>,<password>,<dbname>)
db = MySQLdb.connect("zekeinstance.cra1n4auudcc.ap-southeast-1.rds.amazonaws.com","test","epsilon123","zekelabs")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Create table as per requirement
#sql = """CREATE TABLE EMPLOYEE_Ashish(
#         FIRST_NAME  CHAR(20) NOT NULL,
#         LAST_NAME  CHAR(20),
#         AGE INT,  
#         SEX CHAR(1),
#         INCOME FLOAT )"""
#cursor.execute(sql)
#
# execute SQL query using execute() method.
fname = ["a","b","c","d"]
salary = [1000,2000,3000,4000]

for i in range(len(fname)):
	print("a " + str(salary[i]))
	sql = "INSERT INTO EMPLOYEE_Ashish(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('" + fname[i ] + "', 'M', 25, 'M'," + str(salary[i]) + " )"
	cursor.execute(sql)
	db.commit()

#sql = """ DELETE FROM EMPLOYEE1 WHERE FIRST_NAME = "Prithvi" """
#cursor.execute(sql)
#db.commit()


sql = "SELECT * FROM EMPLOYEE_Ashish"
#sql = "SELECT * FROM EMPLOYEE \
#       WHERE INCOME > '%d'" % (1000)
#sql = getquery()

try:
	cursor.execute(sql)
	results = cursor.fetchall()
	print(results)	
	outputfile = open("outfile.txt",'w')
	for i in results:
		print (i)
		#print("firstname = ", i[0], "lastname = ", i[1])
		outputfile.write(str(i[0])+ "," + str(i[4]) + "\n") 
	outputfile.close()
	db.commit()
except:
	db.rollback()
	print "Error: unable to fecth data"

db.close()
#sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#         LAST_NAME, AGE, SEX, INCOME)
#         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
# Fetch a single row using fetchone() method.
#data = cursor.fetchone()
#data = cursor.()
#print "Database version : %s " % data

# disconnect from server
#db.close()
