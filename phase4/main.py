import pymysql
import datetime
import pymysql.cursors
from function import *
con = pymysql.connect(host='localhost',user='root',password='123',db='hospital',cursorclass=pymysql.cursors.DictCursor)
if(con.open):
    print("Hi,")
else:
    print("Connection Error")
cur=con.cursor()
while(True):
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
    print("18 to check cost for a medicine post discount")
    print("19 to check age for a user")
    print("20 to generate Report 1 which finds total medicine cost used by each patient along with patients names using JOIN technique")
    print("21 to generate the second report")
    print("22 to exit the user interface")
    command=int(input("Enter your preference:-"))
    print(command)
    if command==1:
        admin(con,cur)
    elif command==2:
        users(con,cur)
    elif command==3:
        pass
    elif command==4:
        tel_no_users(con,cur)
    elif command==5:
        address_users(con,cur)
    elif command==6:
        pass
    elif command==7:
        permission(con,cur)
    elif command==18:
        costForMedicine(con,cur)
    elif command==19:
        findAge(con,cur)
    elif command ==20: # For Report 1 generation
        report1(con,cur)
    elif command==22:
        print("Bye")
        exit()
