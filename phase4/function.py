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
                q="Insert into admin values(%s,%s,%s,%s,%s,%s)" 
             
                cur.execute(q,(d["id"],d["f_n"],d["m_n"],d["l_n"],d["l"],d["pass"]))
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
                
                q="UPDATE admin set id=%s,first_name=%s,middle_name=%s,last_name=%s,login=%s,password=%s where id=%s" 
             
                cur.execute(q,(d["id"],d["f_n"],d["m_n"],d["l_n"],d["l"],d["pass"],key))
                con.commit()
                print("Success")
            except Exception as er:
                print("Error is ",er)
        elif inp==4:
            
            try:
                    key=input("Enter id to delete ")
                    q="Delete from admin where id=%s" 
                    cur.execute(q,(key))
                    con.commit()
                    print("Success")
            except Exception as er:
                print("Error is ",er)
        elif inp==5:
            return 1
        else :
            print("Enter correct input")
def users(con,cur):
    while(True):
            print("Press 1 to see all data")
            print("Press 2 to insert new tuple")
            print("Press 3 to update a tuple")
            print("Press 4 to Delete")
            print("Press 5 to Go back")
            inp=int(input("Enter query:-"))
            if inp==1:
                try:
                        cur.execute("Select * from users;")
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
                        
                        d["l_n"]=input("enter last name  ")
                        d["gender"]=input("Enter gender(M/F/T) ")
                        d["dob"]=input("Enter dob ")
                        d["per_id"]=input("Enter permission id ")
                        d["emailID"]=input("Enter Email id ")
                        q="Insert into users values(%s,%s,%s,%s,'%s',%s,%s,%s)"
                        cur.execute(q,(d["id"],d["f_n"],d["m_n"],d["l_n"],d["gender"],d["dob"],d["per_id"],d["emailID"]))
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
                        if[d["id"]==""]:
                            d["id"]=ans["id"]
                        d["f_n"]=input("Enter first name ")
                        if(d["f_n"]==""):
                            d["f_n"]=ans["first_name"]
                        d["m_n"]=input("Enter middle name, write NULL if empty ")
                        if(d["m_n"]==""):
                            d["m_n"]=ans["middle_name"]
                        d["l_n"]=input("enter last name ")
                        if(d["l_n"]==""):
                            d["l_n"]=ans["last_name"]
                        d["gender"]=input("Enter gender(M/F/T) ")
                        if(d["gender"]==""):
                            d["gender"]= ans["gender"]
                        d["dob"]=input("dob ")
                        if d["dob"]=="":
                            d["dob"]=ans["dob"]
                        d["per_id"]=input("Enter permission id ")
                        if(d["per_id"]==""):
                            d["per_id"]=ans["per_id"]
                        d["emailID"]=input("Enter Email id ")
                        if(d["emailID"]==""):
                            d["emailID"]=ans["emailID"]
                        q="UPDATE users SET id=%s,first_name=%s,middle_name=%s,last_name=%s,gender=%s,dob=%s,per_id=%s,emailID=%s where id=%s" 
                        cur.execute(q,(d["id"],d["f_n"],d["m_n"],d["l_n"],d["gender"],d["dob"],d["per_id"],d["emailID"],key))
                        con.commit()
                        print("Success")
                except Exception as er:
                    print("Error is ",er)
            
            elif inp==4:
                try:
                        key=input("Enter id to delete ")
                        q="Delete from users where id=%s" 
                        cur.execute(q,(key))
                        con.commit()
                        print("Success")
                except Exception as er:
                    print("Error is ",er)
            elif inp==5:
                return 1
            else :
                print("Enter correct input")
def permission(con,cur):
    while(True):
            print("Press 1 to see all data")
            print("Press 2 to insert new tuple")
            print("Press 3 to update a tuple")
            print("Press 4 to Delete")
            print("Press 5 to Go back")
            inp=int(input("Enter query:-"))
            if inp==1:
                try:
                        cur.execute("Select * from permission;")
                        answer = cur.fetchall()
                        for i in answer:
                            print(i)
                except Exception as er:
                    print("Error is ",er)
            elif inp==2:
                try:
                    d={}
                    d["per_id"]=input("Enter permission id ")
                    d["per_name"]=input("Enter permission name ")
                    q="Insert into permission values(%s,%s)" 
                    cur.execute(q,(d["per_id"],d["per_name"]))
                    con.commit()
                    print("Success")
                except Exception as er:
                    print("Error is ",er)
            elif inp==3:
                try:
                    d={}
                    key=input("Enter per_id to modify ")
                    q="Select * from admin where id=%s" ;
                    cur.execute(q,(key))
                    ans=cur.fetchone()
                    print("If you don't want to modify the column,press ENTER")
                    d["per_id"]=input("Enter permission id")
                    if(d["per_id"]==""):
                        d["per_id"]=ans["per_id"]
                    d["per_name"]=input("Enter permission name")
                    if(d["per_name"]==""):
                        d["per_name"]=ans["per_name"]
                    q="UPDATE permission SET per_id=%s,per_name=%s where per_id=%s"
                    cur.execute(q,(d["per_id"],d["per_name"],key))
                    con.commit()
                    print("Success")
                except Exception as er:
                    print("Error is ",er)
            elif inp==4:
                try:
                        key=input("Enter per_id to delete ")
                        q="Delete from permission where per_id=%s" 
                        cur.execute(q,(key))
                        con.commit()
                        print("Success")
                except Exception as er:
                    print("Error is ",er)
            elif inp==5:
                return 1
            else :
                print("Enter correct input")
def tel_no_users(con,cur):
    while(True):
            print("Press 1 to see all data")
            print("Press 2 to insert new tuple")
            print("Press 3 to update a tuple")
            print("Press 4 to Delete")
            print("Press 5 to Go back")
            inp=int(input("Enter query:-"))
            if inp==1:
                try:
                        cur.execute("Select * from tel_no_users;")
                        answer = cur.fetchall()
                        for i in answer:
                            print(i)
                except Exception as er:
                    print("Error is ",er)
            elif inp==2:
                try:
                    d={}
                    d["users_id"]=input("Enter users id")
                    d["tel_no"]=int(input("Enter number"))
                    q="Insert into tel_no_users values(%s,%d)" 
                    cur.execute(q,(d["users_id"],d["tel_no"]))
                    con.commit()
                    print("Success")
                except Exception as er:
                    print("Error is ",er)
            elif inp==3:
                try:
                    d={}
                    key=input("Enter per_id to modify ")
                    q="Select * from admin where id=%s" 
                    cur.execute(q,(key))
                    ans=cur.fetchone()
                    print("If you don't want to modify the column,press ENTER")
                    d["users_id"]=input("Enter users id")
                    if d["users_id"]=="":
                        d["users_id"]=ans["users_id"]
                    d["tel_no"]=int(input("Enter number"))
                    if d["tel_no"]=="":
                        d["tel_no"]=ans["tel_no"]
                    q="Update tel_no_users set users_id=%s,tel_no=%d where users_id=%s" 
                    cur.execute(q,(d["users_id"],d["tel_no"],key))
                    con.commit()
                    print("Success")
                except Exception as er:
                    print("Error is ",er)
            elif inp==4:
                try:
                    d={}
                    key=input("Enter per_id to modify ")
                    q="Delete from tel_no_users where users_if=%s" 
                    cur.execute(q,(key))
                    con.commit()
                    print("Success")
                except Exception as er:
                    print("Error is ",er)
            elif inp==5:
                return 1
            else :
                print("Enter correct input")
 
def address_users(con,cur):
    while(True):
            print("Press 1 to see all data")
            print("Press 2 to insert new tuple")
            print("Press 3 to update a tuple")
            print("Press 4 to Delete")
            print("Press 5 to Go back")
            inp=int(input("Enter query:-"))
            if inp==1:
                try:
                        cur.execute("Select * from address_users;")
                        answer = cur.fetchall()
                        for i in answer:
                            print(i)
                except Exception as er:
                    print("Error is ",er)
            elif inp==2:
                try:
                    d={}
                    d["users_id"]=input("Enter users id")
                    d["address"]=(input("Enter number"))
                    q="Insert into tel_no_users values(%s,%s)" 
                    cur.execute(q,(d["users_id"],d["address"]))
                    con.commit()
                    print("Success")
                except Exception as er:
                    print("Error is ",er)
            elif inp==3:
                try:
                    d={}
                    key=input("Enter per_id to modify ")
                    q="Select * from admin where id=%s" 
                    cur.execute(q,(key))
                    ans=cur.fetchone()
                    print("If you don't want to modify the column,press ENTER")
                    d["users_id"]=input("Enter users id")
                    if d["users_id"]=="":
                        d["users_id"]=ans["users_id"]
                    d["address"]=(input("Enter address"))
                    if d["address"]=="":
                        d["address"]=ans["address"]
                    q="Update tel_no_users set users_id=%s,address=%s where users_id=%s" 
                    cur.execute(q,(d["users_id"],d["address"],key))
                    con.commit()
                    print("Success")
                except Exception as er:
                    print("Error is ",er)
            elif inp==4:
                try:
                    d={}
                    key=input("Enter id to modify ")
                    q="Delete from address_users where users_id=%s" 
                    cur.execute(q,(key))
                    con.commit()
                    print("Success")
                except Exception as er:
                    print("Error is ",er)
            elif inp==5:
                return 1
            else :
                print("Enter correct input")
def controls(con,cur):
    pass
