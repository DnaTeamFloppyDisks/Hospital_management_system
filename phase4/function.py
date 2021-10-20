import datetime
def admin(con,cur):
    while(True):
        print("Press 1 to see all data")
        print("Press 2 to insert new tuple")
        print("Press 3 to update a tuple")
        print("Press 4 to Delete")
        print("Press 5 to Go back")
        inp=int(input("Enter query:-"))
        if inp==1:
            try:
                    cur.execute("Select * from admin;")
                    answer = cur.fetchall()
                    for i in answer:
                        print(i)
            except Exception as er:
                print("Error is ",er)
        elif inp==2:
            try:
                d={}
                d["id"]=input("Enter id ")
                d["f_n"]=input("Enter first name ")
                d["m_n"]=input("Enter middle name, write NULL if empty ")
                
                d["l_n"]=input("enter last name ")
                d["l"]=input("Enter login ")
                d["pass"]=input("Enter password ")
                q="Insert into admin values(%s,%s,%s,%s,%s,%s)" %(d["id"],d["f_n"],d["m_n"],d["l_n"],d["l"],d["pass"]);
             
                cur.execute(q)
                con.commit()
                print("Success")
            except Exception as er:
                print("Error is ",er)
        elif inp==3:
            try:
                d={}
                key=input("Enter id to modify ")
                q="Select * from admin where id=%s" %(key);
                cur.execute(q)
                ans=cur.fetchone()
                print("If you don't want to modify the column,press ENTER")
                d["id"]=input("Enter id ")
                if(d["id"]==""):
                    d["id"]=ans["id"]
                d["f_n"]=input("Enter first name ")
                if(d["f_n"]==""):
                    d["f_n"]=ans["first_name"]
                d["m_n"]=input("Enter middle name, write NULL if empty ")
                if d["m_n"]=="":
                    d["m_n"]=ans["middle_name"]
                d["l_n"]=input("enter last name ")
                if d["l_n"]=="":
                    d["l_n"]=ans["last_name"]
                d["l"]=input("Enter login ")
                if d["l"]=="":
                    d["l"]=ans["login"]
                d["pass"]=input("Enter password ")
                if d["pass"]=="":
                    d["pass"]=ans["password"]
                
                q="UPDATE admin set id=%s,first_name=%s,middle_name=%s,last_name=%s,login=%s,password=%s" %(d["id"],d["f_n"],d["m_n"],d["l_n"],d["l"],d["pass"]);
             
                cur.execute(q)
                con.commit()
                print("Success")
            except Exception as er:
                print("Error is ",er)
        elif inp==4:
            
            try:
                    key=input("Enter id to delete ")
                    q="Delete from admin where ID=%s" %(key);
                    cur.execute(q)
                    con.commit()
                    print("Success")
            except Exception as er:
                print("Error is ",er)
        elif inp==5:
            return 1
        
        else :
            print("Enter correct input")
