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
                        q="Insert into users values(%s,%s,%s,%s,%s,%s,%s,%s)"
                        cur.execute(q,(d["id"],d["f_n"],d["m_n"],d["l_n"],d["gender"],d["dob"],d["per_id"],d["emailID"]))
                        con.commit()
                        print("Success")
                except Exception as er:
                    print("Error is ",er)
            elif inp==3:
                try:
                        d={}
                        key=input("Enter id to modify ")
                        q="Select * from users where id=%s" %(key);
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
                    q="Select * from permission where id=%s" ;
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
                    tel_no=int(input("Enter number"))
                    q="Insert into tel_no_users values(%s,%s)" 
                    cur.execute(q,(d["users_id"],tel_no))
                    con.commit()
                    print("Success")
                except Exception as er:
                    print("Error is ",er)
            elif inp==3:
                try:
                    d={}
                    key=input("Enter id  to modify ")
                    num =int(input("Enter number to modify"))
                    q="Select * from tel_no_users where users_id=%s and tel_no=%s" 
                    cur.execute(q,(key,num))
                    ans=cur.fetchone()
                    print("If you don't want to modify the column,press ENTER")
                    d["users_id"]=input("Enter users id")
                    if d["users_id"]=="":
                        d["users_id"]=ans["users_id"]
                    d["tel_no"]=int(input("Enter number"))
                    if d["tel_no"]=="":
                        d["tel_no"]=ans["tel_no"]
                    q="Update tel_no_users set users_id=%s,tel_no=%s where users_id=%s and tel_no=%s" 
                    cur.execute(q,(d["users_id"],d["tel_no"],key,num))
                    con.commit()
                    print("Success")
                except Exception as er:
                    print("Error is ",er)
            elif inp==4:
                try:
                    d={}
                    key=input("Enter per_id to modify ")
                    num =int(input("Enter number to delete"))
                    q="Delete from tel_no_users where users_id=%s and tel_no=%s" 
                    cur.execute(q,(key,num))
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
                    d["address"]=(input("Enter address"))
                    q="Insert into address_users values(%s,%s)" 
                    cur.execute(q,(d["users_id"],d["address"]))
                    con.commit()
                    print("Success")
                except Exception as er:
                    print("Error is ",er)
            elif inp==3:
                try:
                    d={}
                    key=input("Enter id to modify ")
                    add=input("Enter address to modify")
                    q="Select * from address_users where users_id=%s and address=%s" 
                    cur.execute(q,(key,add))
                    ans=cur.fetchone()
                    print("If you don't want to modify the column,press ENTER")
                    d["users_id"]=input("Enter users id")
                    if d["users_id"]=="":
                        d["users_id"]=ans["users_id"]
                    d["address"]=(input("Enter address"))
                    if d["address"]=="":
                        d["address"]=ans["address"]
                    q="Update address_users set users_id=%s,address=%s where users_id=%s and address=%s" 
                    cur.execute(q,(d["users_id"],d["address"],key,add))
                    con.commit()
                    print("Success")
                except Exception as er:
                    print("Error is ",er)
            elif inp==4:
                try:
                    d={}
                    key=input("Enter id to modify ")
                    add=input("Enter address to modify")
                    q="Delete from address_users where users_id=%s and address=%s" 
                    cur.execute(q,(key,add))
                    con.commit()
                    print("Success")
                except Exception as er:
                    print("Error is ",er)
            elif inp==5:
                return 1
            else :
                print("Enter correct input")

def treatment(con,cur):
    while(True):
            print("Press 1 to see all data")
            print("Press 2 to insert new tuple")
            print("Press 3 to update a tuple")
            print("Press 4 to Delete")
            print("Press 5 to Go back")
            inp=int(input("Enter query:-"))
            if inp==1:
                try:
                        cur.execute("Select * from treatment;")
                        answer = cur.fetchall()
                        for i in answer:
                            print(i)
                except Exception as er:
                    print("Error is ",er)
            elif inp==2:
                try:
                    d={}
                    d["users_id"]=input("Enter treatment id ")
                    d["treatment"]=(input("Enter treatment name "))
                    q="Insert into treatment values(%s,%s)" 
                    cur.execute(q,(d["users_id"],d["treatment"]))
                    con.commit()
                    print("Success")
                except Exception as er:
                    print("Error is ",er)
            elif inp==3:
                try:
                    d={}
                    key=input("Enter t_id to modify ")
                    q="Select * from treatment where t_id=%s" 
                    cur.execute(q,(key))
                    ans=cur.fetchone()
                    print("If you don't want to modify the column,press ENTER")
                    d["t_id"]=input("Enter t_id ")
                    if d["t_id"]=="":
                        d["t_id"]=ans["t_id"]
                    d["t_name"]=(input("Enter t_name "))
                    if d["t_name"]=="":
                        d["t_name"]=ans["t_name"]
                    q="Update treatment set t_id=%s,t_name=%s where t_id=%s" 
                    cur.execute(q,(d["t_id"],d["t_name"],key))
                    con.commit()
                    print("Success") 
                except Exception as er:
                    print("Error is ",er)
            elif inp==4:
                try:
                    d={}
                    key=input("Enter id to modify ")
                    q="Delete from treatment where t_id=%s" 
                    cur.execute(q,(key))
                    con.commit()
                    print("Success")
                except Exception as er:
                    print("Error is ",er)
            elif inp==5:
                return 1
            else :
                print("Enter correct input")
def patient(con,cur):
    while(True):
            print("Press 1 to see all data")
            print("Press 2 to insert new tuple")
            print("Press 3 to update a tuple")
            print("Press 4 to Delete")
            print("Press 5 to search first name starting with a string")
            print("Press 6 to search address with a string in between")
            print("Press 7 to search for patients after a specific date")
            print("Press 8 to Go back")
            inp=int(input("Enter query:-"))
            if inp==1:
                try:
                        cur.execute("Select * from patient;")
                        answer = cur.fetchall()
                        for i in answer:
                            print(i)
                except Exception as er:
                    print("Error is ",er)
            elif inp==2:
                try:
                    d={}
                    d["p_id"]=input("Enter patient id ")
                    d["adm_date"]=(input("Enter date"))
                    d["complaints"]=(input("Enter complaints"))
                    q="Insert into patient values(%s,%s,%s)" 
                    cur.execute(q,(d["p_id"],d["adm_date"],d["complaints"]))
                    con.commit()
                    print("Success")
                except Exception as er:
                    print("Error is ",er)
            elif inp==3:
                try:
                    d={}
                    key=input("Enter id to modify ")
                    q="Select * from patient where p_id=%s" %(key);
                    cur.execute(q)
                    ans=cur.fetchone()
                    print("If you don't want to modify the column,press ENTER")
                    d["p_id"]=input("Enter id ")
                    if(d["p_id"]==""):
                        d["p_id"]=ans["p_id"]
                    d["adm_date"]=input("Enter adm_date ")
                    if(d["adm_date"]==""):
                        d["adm_date"]=ans["adm_date"]

                    d["complaints"]=input("Enter complains ")
                    if(d["complaints"]==""):
                        d["complaints"]=ans["complaints"]
                    
                    q="UPDATE patient set p_id=%s,adm_date=%s,complaints=%s where p_id=%s" 
                
                    cur.execute(q,(d["p_id"],d["adm_date"],d["complaints"],key))
                    con.commit()
                    print("Success")
                except Exception as er:
                    print("Error is ",er)
            elif inp==4:
                try:
                    d={}
                    key=input("Enter id to modify ")
                    q="Delete from patient where p_id=%s" 
                    cur.execute(q,(key))
                    con.commit()
                    print("Success")
                except Exception as er:
                    print("Error is ",er)
            
            elif inp==5:
                try:
                    key=input("Enter key to search")
                    q= "Select DISTINCT(first_name)  FROM ((Select * from users  ) as A INNER JOIN (Select * from patient ) as B ON A.id=B.p_id) where first_name like '%s%%' "  % (key)
                    cur.execute(q)
                    answer = cur.fetchall()
                    for i in answer:
                            print(i)
                except Exception as er:
                    print("Error is ",er)
            elif inp==6:
                try:
                    key=input("Enter key to search")
                    q= "Select id,address  FROM ((Select * from address_users )as C INNER JOIN(Select * from users  ) as A INNER JOIN (Select * from patient ) as B ON A.id=B.p_id ON A.id=C.users_id) where address like '%%%s%%'  " %(key)
                    cur.execute(q)
                    answer = cur.fetchall()
                    for i in answer:
                            print(i)
                except Exception as er:
                    print("Error is ",er)
            elif inp==7:
                try:
                    key=input("Enter adm_date to search in YYYY/MM/DD format")
                    q= "Select * from patient where adm_date>=%s"
                    cur.execute(q,(key))
                    answer = cur.fetchall()
                    for i in answer:
                            print(i)
                except Exception as er:
                    print("Error is ",er)
            elif inp==8:
                return 1
            else :
                print("Enter correct input")
def doctor(con,cur):
    while(True):
        print("Press 1 to see all data")
        print("Press 2 to insert new tuple")
        print("Press 3 to update a tuple")
        print("Press 4 to delete")
        print("Press 5 to max salary from doctors")
        print("Press 6 to go back")
        inp=int(input("Enter query:-"))
        if inp==1:
            try:
                    cur.execute("Select * from doctor;")
                    answer = cur.fetchall()
                    for i in answer:
                        print(i)
            except Exception as er:
                print("Error is ",er)
        elif inp==2:
            try:
                d={}
                d["doc_id"]=input("Enter doctor id ")
                d["doc_ssn"]=input("Enter doctor ssn ")
                d["dep_id"]=input("Enter department id ")
                d["salary"]=input("Enter salary ")
                q="Insert into doctor values(%s,%s,%s,%s)" 
             
                cur.execute(q,(d["doc_id"],d["doc_ssn"],d["dep_id"],d["salary"]))
                con.commit()
                print("Success")
            except Exception as er:
                print("Error is ",er)
        elif inp==3:
            try:
                d={}
                key=input("Enter doctor id to modify ")
                q="Select * from doctor where doc_id=%s" %(key)
                cur.execute(q)
                ans=cur.fetchone()
                print("If you don't want to modify the column,press ENTER")
                d["doc_id"]=input("Enter doctor id ")
                if(d["doc_id"]==""):
                    d["doc_id"]=ans["doc_id"]
                d["doc_ssn"]=input("Enter doctor's ssn ")
                if(d["doc_ssn"]==""):
                    d["doc_ssn"]=ans["doc_ssn"]
                d["dep_id"]=input("Enter department id of doctor ")
                if d["dep_id"]=="":
                    d["dep_id"]=ans["dep_id"]
                d["salary"]=input("salary ")
                if d["salary"]=="":
                    d["salary"]=ans["salary"]
                
                q="UPDATE doctor set doc_id=%s,doc_ssn=%s,dep_id=%s,salary=%s where doc_id=%s" 
             
                cur.execute(q,(d["doc_id"],d["doc_ssn"],d["dep_id"],d["salary"],key))
                con.commit()
                print("Success")
            except Exception as er:
                print("Error is ",er)
        elif inp==4:
            
            try:
                    key=input("Enter doctor id to delete ")
                    q="Delete from doctor where doc_id=%s" 
                    cur.execute(q,(key))
                    con.commit()
                    print("Success")
            except Exception as er:
                print("Error is ",er)
        elif inp==5:
            try:
                print("Return MAX salary from doctor")
                q="Select MAX(salary) from doctor"
                cur.execute(q)
                
            except Exception as er:
                print("Error is ",er)
        elif inp==6:
            return 1
        else :
            print("Enter correct input")
def medicine(con,cur):
    while(True):
        print("Press 1 to see all data")
        print("Press 2 to insert new tuple")
        print("Press 3 to update a tuple")
        print("Press 4 to Delete")
        print("Press 5 to Go back")
        inp=int(input("Enter query:-"))
        if inp==1:
            try:
                    cur.execute("Select * from medicine")
                    answer = cur.fetchall()
                    for i in answer:
                        print(i)
            except Exception as er:
                print("Error is ",er)
        elif inp==2:
            try:
                d={}
                d["m_id"]=input("Enter medicine id ")
                d["m_name"]=input("Enter medicine name ")
                d["mrp"]=float(input("Enter MRP of Medicine "))
                d["discount"]=float(input("Enter discount(if applicable) "))
                q="Insert into medicine values(%s,%s,%s,%s)" 
             
                cur.execute(q,(d["m_id"],d["m_name"],float(d["mrp"]),float(d["discount"])))
                con.commit()
                print("Success")
            except Exception as er:
                print("Error is ",er)
        elif inp==3:
            try:
                d={}
                key=input("Enter medicine id to modify ")
                q="Select * from medicine where m_id=%s" 
                cur.execute(q,(key))
                ans=cur.fetchone()
                print("If you don't want to modify the column,press ENTER")
                d["m_id"]=input("Enter medicine id ")
                if(d["m_id"]==""):
                    d["m_id"]=ans["m_id"]
                d["m_name"]=input("Enter medicine name ")
                if(d["m_name"]==""):
                    d["m_name"]=ans["m_name"]
                mrp=(input("Enter MRP of  medicine "))
                if mrp=="":
                    d["mrp"]=ans["mrp"]
                else :
                    d["mrp"]=float(mrp)
                if d["mrp"]=="":
                    d["mrp"]=ans["mrp"]
                discount=(input("Enter discount "))
                if discount=="":
                    d["discount"]=float(ans["discount"])
                else :
                    d["discount"]=float(discount)
                q="UPDATE medicine set m_id=%s,m_name=%s,mrp=%s,discount=%s where m_id=%s" 
             
                cur.execute(q,(d["m_id"],d["m_name"],d["mrp"],d["discount"],key))
                con.commit()
                print("Success")
            except Exception as er:
                print("Error is ",er)
        elif inp==4:
            
            try:
                    key=input("Enter medicine id to delete ")
                    q="Delete from medicine where m_id=%s" 
                    cur.execute(q,(key))
                    con.commit()
                    print("Success")
            except Exception as er:
                print("Error is ",er)
        elif inp==5:
            return 1
        else :
            print("Enter correct input")
def other_workers(con,cur):
    while(True):
            print("Press 1 to see all data")
            print("Press 2 to insert new tuple")
            print("Press 3 to update a tuple")
            print("Press 4 to Delete")
            print("Press 5 to Go back")
            inp=int(input("Enter query:-"))
            if inp==1:
                try:
                        cur.execute("Select * from other_workers;")
                        answer = cur.fetchall()
                        for i in answer:
                            print(i)
                except Exception as er:
                    print("Error is ",er)
            elif inp==2:
                try:
                    d={}
                    d["w_id"]=input("Enter worker id")
                    d["job"]=(input("Enter job"))
                    d["salary"]=float(input("Enter salary"))
                    q="Insert into other_workers values(%s,%s,%s)" 
                    cur.execute(q,(d["w_id"],d["job"],d["salary"]))
                    con.commit()
                    print("Success")
                except Exception as er:
                    print("Error is ",er)
            elif inp==3:
                try:
                    d={}
                    key=input("Enter id to modify ")
                    q="Select * from other_workers where w_id=%s" 
                    cur.execute(q,(key))
                    ans=cur.fetchone()
                    print("If you don't want to modify the column,press ENTER")
                    d["w_id"]=input("Enter worker id")
                    if d["w_id"]=="":
                        d["w_id"]=ans["w_id"]
                    d["job"]=(input("Enter job"))
                    if d["job"]=="":
                        d["job"]=ans["job"]
                    
                    sal=(input("Enter salary"))
                    if sal=="":
                        d["salary"]=ans["salary"]
                    else :
                        d["salary"]=float(sal)
                    q="Update other_workers set w_id=%s,job=%s,salary=%s where w_id=%s" 
                    cur.execute(q,(d["w_id"],d["job"],d["salary"],key))
                    con.commit()
                    print("Success")
                except Exception as er:
                    print("Error is ",er)
            elif inp==4:
                try:
                    d={}
                    key=input("Enter id to modify ")
                    q="Delete from other_workers where w_id=%s" 
                    cur.execute(q,(key))
                    con.commit()
                    print("Success")
                except Exception as er:
                    print("Error is ",er)
            elif inp==5:
                return 1
            else :
                print("Enter correct input")

# For derived attrbutes
def costForMedicine(con,cur):
    while(True):
        print("Press 1 to check cost")
        print("Press 2 to return")

        inp=input("Enter command ")
        if(inp=='1'):
            try:
                key=input("Enter medicine id for which to check cost ")
                q="select m_name as 'Name',mrp*(100-discount)/100 as 'Cost' from medicine where m_id=%s"
                cur.execute(q,(key))
                ans=cur.fetchone()
                print(ans)
            except Exception as er:
                            print("Error is ",er)     
        elif inp=='2':
            return 1
        else:
            print("Enter correct input")

def findAge(con,cur):
     while(True):
        print("Press 1 to check age")
        print("Press 2 to return")

        inp=input("Enter command ")
        if(inp=='1'):
            try:
                key=input("Enter user id for which to check age in years ")
                q="SELECT first_name,last_name,TIMESTAMPDIFF(YEAR, dob, CURDATE()) AS age from users where id=%s"
                cur.execute(q,(key))
                ans=cur.fetchone()
                print(ans)
            except Exception as er:
                            print("Error is ",er)     
        elif inp=='2':
            return 1
        else:
            print("Enter correct input")
# Report analysis:-
def report1(con,cur):
    print("This is Report 1 which finds total medicine cost used by each patient along with patients details using JOIN technique")
    while(True):
        print("Press 1 to check Report")
        print("Press 2 to return")
        inp=input("Enter command ")
        if inp=='1':   
            key=input("Enter Patient id to generate report for ")
            try:
                q1="Select SUM(Cost) FROM (Select p_id from patient where p_id=%s) as A INNER JOIN (Select * from medicalRecord) as B INNER JOIN (Select m_id,m_name,mrp*(100-discount)/100 as 'Cost' from medicine) as C ON B.m_id=C.m_id ON A.p_id=B.p_id"
                q2="Select first_name,last_name from users where id=%s"
                cur.execute(q1,(key))
                ans1=cur.fetchone()
                cur.execute(q2,(key))
                ans2=cur.fetchone()
                print(ans2,ans1)
            except Exception as er:                
                print("Error is ",er)     
        elif inp=='2':
            return 1
        else:
            print("Enter correct input")
def report2(con,cur):
    print("This report generates the patient names under a specific doctor")
    while(True):
        print("Press 1 to check Report")
        print("Press 2 to return")
        inp=input("Enter command ")
        if inp=='1':   
            key=input("Enter Doc id to generate report for ")
            try:
                q1="Select DISTINCT(p_id),first_name as 'patient_first_name',last_name as 'patient_last_name',doc_id,complaints,adm_date FROM ( (Select doc_id,p_id as 'ap_id' from medicalRecord where doc_id=%s ) as A INNER JOIN (Select * from patient ) as B ON A.ap_id=B.p_id INNER JOIN (SELECT * from users ) as C ON C.id=B.p_id );"
                cur.execute(q1,(key))
                ans1=cur.fetchall()
                for i in ans1:
                        print(i)
            except Exception as er:                
                print("Error is ",er)     
        elif inp=='2':
            return 1
        else:
            print("Enter correct input")
def report3(con,cur):
    print("This report generates  the average expenses born by people suffering from a disease.")
    while(True):
        print("Press 1 to check Report")
        print("Press 2 to return")
        inp=input("Enter command ")
        if inp=='1':   
            try:
                q1="Select AVG(mrp*(100-discount)/100) as 'Average Cost',disease from (( Select m_id as am_id,disease from medicalRecord) as A  INNER JOIN (Select * from medicine) as B ON A.am_id=B.m_id ) GROUP BY (disease);"
                cur.execute(q1)
                ans1=cur.fetchall()
                for i in ans1:
                        print(i)
            except Exception as er:                
                print("Error is ",er)     
        elif inp=='2':
            return 1
        else:
            print("Enter correct input")
def medicalRecord(con,cur):
    while(True):
        print("Press 1 to see all data")
        print("Press 2 to insert new tuple")
        print("Press 3 to update a tuple")
        print("Press 4 to Delete")
        print("Press 5 to Go back")
        inp=int(input("Enter query:-"))
        if inp==1:
            try:
                    cur.execute("Select * from medicalRecord;")
                    answer = cur.fetchall()
                    for i in answer:
                        print(i)
            except Exception as er:
                print("Error is ",er)
        elif inp==2:
            try:
                d={}
                d["p_id"]=input("Enter patient id ")
                d["doc_id"]=input("Enter doctor id ")
                d["m_id"]=input("Enter medicine id ")
                d["t_id"]=input("Enter treatment id ")
                d["disease"]=input("Enter name of disease ")
                q="Insert into medicalRecord values(%s,%s,%s,%s,%s)" 
             
                cur.execute(q,(d["p_id"],d["doc_id"],d["m_id"],d["t_id"],d["disease"]))
                con.commit()
                print("Success")
            except Exception as er:
                print("Error is ",er)
        elif inp==3:
            try:
                d={}
                key1=input("Enter patient id of record to be modified ")
                key2=input("Enter doctor id of record to be modified ")
                key3=input("Enter medicine id of record to be modified ")
                key4=input("Enter treatment id of record to be modified ")
                q="Select * from medicalRecord where p_id=%s and doc_id=%s and m_id=%s and t_id=%s  " %(key1,key2,key3,key4)
                cur.execute(q)
                ans=cur.fetchone()
                print("If you don't want to modify the column,press ENTER")
                d["p_id"]=input("Enter patient id ")
                if(d["p_id"]==""):
                    d["p_id"]=ans["p_id"]
                d["doc_id"]=input("Enter doctor id ")
                if(d["doc_id"]==""):
                    d["doc_id"]=ans["doc_id"]
                d["m_id"]=input("Enter medicine id of doctor ")
                if d["m_id"]=="":
                    d["m_id"]=ans["m_id"]
                d["t_id"]=input("Enter t_id ")
                if d["t_id"]=="":
                    d["t_id"]=ans["t_id"]
                d["disease"]=input("Enter disease ")
                if d["disease"]=="":
                    d["disease"]=ans["disease"]
                
                q="UPDATE medicalRecord set p_id=%s,doc_id=%s,m_id=%s,t_id=%s,disease=%s where p_id=%s and doc_id=%s and m_id=%s and t_id=%s" 
             
                cur.execute(q,(d["p_id"],d["doc_id"],d["m_id"],d["t_id"],d["disease"],key1,key2,key3,key4))
                con.commit()
                print("Success")
            except Exception as er:
                print("Error is ",er)
        elif inp==4:
            
            try:
                    key1=input("Enter patient id of record to be modified ")
                    key2=input("Enter doctor id of record to be modified ")
                    key3=input("Enter medicine id of record to be modified ")
                    key4=input("Enter treatment id of record to be modified ")
                    q="Delete from medicalRecord where p_id=%s and doc_id=%s and m_id=%s and t_id=%s" 
                    cur.execute(q,(key1,key2,key3,key4))
                    con.commit()
                    print("Success")
            except Exception as er:
                print("Error is ",er)
        elif inp==5:
            return 1
        else :
            print("Enter correct input")

def doctor(con,cur):
    while(True):
        print("Press 1 to see all data")
        print("Press 2 to insert new tuple")
        print("Press 3 to update a tuple")
        print("Press 4 to Delete")
        print("Press 5 to get Max salary")
        print("Press 6 to get doctors ordered via each department")
        print("Press 7 to Go back")
        inp=int(input("Enter query:-"))
        if inp==1:
            try:
                    cur.execute("Select * from doctor;")
                    answer = cur.fetchall()
                    for i in answer:
                        print(i)
            except Exception as er:
                print("Error is ",er)
        elif inp==2:
            try:
                d={}
                d["doc_id"]=input("Enter doctor id ")
                d["doc_ssn"]=input("Enter doctor ssn ")
                d["dep_id"]=input("Enter department id ")
                d["salary"]=input("Enter salary ")
                q="Insert into doctor values(%s,%s,%s,%s)" 
             
                cur.execute(q,(d["doc_id"],d["doc_ssn"],d["dep_id"],d["salary"]))
                con.commit()
                print("Success")
            except Exception as er:
                print("Error is ",er)
        elif inp==3:
            try:
                d={}
                key=input("Enter doctor id to modify ")
                q="Select * from doctor where doc_id=%s" %(key)
                cur.execute(q)
                ans=cur.fetchone()
                print("If you don't want to modify the column,press ENTER")
                d["doc_id"]=input("Enter doctor id ")
                if(d["doc_id"]==""):
                    d["doc_id"]=ans["doc_id"]
                d["doc_ssn"]=input("Enter doctor's ssn ")
                if(d["doc_ssn"]==""):
                    d["doc_ssn"]=ans["doc_ssn"]
                d["dep_id"]=input("Enter department id of doctor ")
                if d["dep_id"]=="":
                    d["dep_id"]=ans["dep_id"]
                d["salary"]=input("salary ")
                if d["salary"]=="":
                    d["salary"]=ans["salary"]
                
                q="UPDATE doctor set doc_id=%s,doc_ssn=%s,dep_id=%s,salary=%s where doc_id=%s" 
             
                cur.execute(q,(d["doc_id"],d["doc_ssn"],d["dep_id"],d["salary"],key))
                con.commit()
                print("Success")
            except Exception as er:
                print("Error is ",er)
        elif inp==4:
            
            try:
                    key=input("Enter doctor id to delete ")
                    q="Delete from doctor where doc_id=%s" 
                    cur.execute(q,(key))
                    con.commit()
                    print("Success")
            except Exception as er:
                print("Error is ",er)
        elif inp==5:
            try:
                q="select MAX(salary) from doctor"
                cur.execute(q)
                answer = cur.fetchall()
                for i in answer:
                        print(i)
            except Exception as er:
                print("Error is ",er)    
        elif inp==6:
            try:
                key=input("Enter department id ")
                q="Select doc_id,first_name,last_name,salary,doc_ssn,dep_id from ((Select * from doctor) AS A INNER JOIN (Select * from users) as B ON A.doc_id=B.id) where dep_id=%s;"
                cur.execute(q,(key))
                answer = cur.fetchall()
                for i in answer:
                        print(i)
            except Exception as er:
                print("Error is ",er)   
        elif inp==7:
            return 1
        else :
            print("Enter correct input")


def department(con,cur):
    while(True):
            print("Press 1 to see all data")
            print("Press 2 to insert new tuple")
            print("Press 3 to update a tuple")
            print("Press 4 to Delete")
            print("Press 5 to Go back")
            inp=int(input("Enter query:-"))
            if inp==1:
                try:
                        cur.execute("Select * from department;")
                        answer = cur.fetchall()
                        for i in answer:
                            print(i)
                except Exception as er:
                    print("Error is ",er)
            elif inp==2:
                try:
                    d={}
                    d["dep_id"]=input("Enter department id ")
                    d["dep_name"]=(input("Enter department name "))
                    q="Insert into department values(%s,%s)" 
                    cur.execute(q,(d["dep_id"],d["dep_name"]))
                    con.commit()
                    print("Success")
                except Exception as er:
                    print("Error is ",er)
            elif inp==3:
                try:
                    d={}
                    key=input("Enter dep_id to modify ")
                    q="Select * from department where dep_id=%s" 
                    cur.execute(q,(key))
                    ans=cur.fetchone()
                    print("If you don't want to modify the column,press ENTER")
                    d["dep_id"]=input("Enter dep_id ")
                    if d["dep_id"]=="":
                        d["dep_id"]=ans["dep_id"]
                    d["dep_name"]=(input("Enter dep_name "))
                    if d["dep_name"]=="":
                        d["dep_name"]=ans["dep_name"]
                    q="Update department set dep_id=%s,dep_name=%s where dep_id=%s" 
                    cur.execute(q,(d["dep_id"],d["dep_name"],key))
                    con.commit()
                    print("Success") 
                except Exception as er:
                    print("Error is ",er)
            elif inp==4:
                try:
                    d={}
                    key=input("Enter id to modify ")
                    q="Delete from department where dep_id=%s" 
                    cur.execute(q,(key))
                    con.commit()
                    print("Success")
                except Exception as er:
                    print("Error is ",er)
            elif inp==5:
                return 1
            else :
                print("Enter correct input")
