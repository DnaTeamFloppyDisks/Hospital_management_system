import pymysql
import datetime
import pymysql.cursors
from function import *
# Please enter your own password as a string and user afaik will be root only dont change rest of the stuff ig
con = pymysql.connect(host='localhost',user='root',password=password,db='hospital',cursorclass=pymysql.cursors.DictCursor)
if(con.open):
    print("Connected")
else:
    print("Connection Error")
cur=con.cursor()
print("Which table do you want to work on:-")
print("1 for admin")
print("2 for users")
print("3 for controls")
print("4 for tel_no_users")
print("5 for address_users")
print("6 for doctor")
print("7 for permission")
print("8 for patient")
print("9 for other_workers")
print("10 for grade_1")
print("11 for grade_2")
print("12 for department")
print("13 for maintenenceSchedule")
print("14 for medicine")
print("15 for treatment")
print("16 for medicalRecord")
print("17 for dosage")
print("18 to exit")
command=int(input("Enter your preference:-"))
print(command)
if command==1:
    admin(con,cur)