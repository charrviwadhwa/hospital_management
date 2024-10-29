
import mysql.connector
from tabulate import tabulate
l=[]



def myconnection():
    con=mysql.connector.connect(host ='localhost', database='hs', user='root', passwd='dav')
    return con
    

con=myconnection()
cur=con.cursor()
cur.execute("select pid from hospi")
q=cur.fetchall()
q1=list(q)
for i in q1:
    l.append(i[0])




def selectAll():
    cur=con.cursor()
    cur.execute("select * from hospi")
    r=cur.fetchall()
    if(r==[]):
        print("\nNo Record in Table to display")
    else:
        print(tabulate(r,headers=['PID','PNAME','GENDER','FEE','AGE','WARD','DISEASE']))
        
        
    cur.close()
    con.close()

def selectSpecfic():
    cur=con.cursor()
    print("Select Searching Options ")
    print("1.for ID")
    print("2.for NAME")
    print("3.for FEE Range")
    print("4.for AGE Range")
    print("5.for WARD")
    print("6.for DISEASE")
    op=int(input("Enter Your from Above Menu "))
    if(op==1):
        eno=int(input("Enter Id whose record you want to see "))
        query ="select * from hospi where pid = '%d'"
        ag=(eno)        
        cur.execute(query % ag)
        r=cur.fetchall()
        
        if(r==[]):
            print("\nNo ID Matched")
        else:
            print(tabulate(r,headers=['PID','PNAME','GENDER','FEE','AGE','WARD','DISEASE']))
            
    elif(op==2):
        en=input("Enter Name whose record you want to see ")
        query ="select * from hospi where Pname = '%s'"
        ag=(en.lower())        
        cur.execute(query % ag)
        r=cur.fetchall()
            
        if(r==[]):
            print("\nNo Name Matched")
        else:
            print(tabulate(r,headers=['PID','PNAME','GENDER','FEE','AGE','WARD','DISEASE']))
            
    elif(op==3):
        x=int(input("Enter Lower Limit of Fees "))
        y=int(input("Enter Upper Limit of Fees "))
        query ="select * from hospi where fee >='%d' and fee <= '%d'"
        ag=(x,y)        
        cur.execute(query % ag)
        r=cur.fetchall()

        if(r==[]):
            print("\nNo fee Range Matched")
        else:
            print(tabulate(r,headers=['PID','PNAME','GENDER','FEE','AGE','WARD','DISEASE']))
            
    elif(op==4):
        x=int(input("Enter Lower Limit of AGE "))
        y=int(input("Enter Upper Limit of AGE "))
        query ="select * from hospi where age >='%d' and age <= '%d'"
        ag=(x,y)        
        cur.execute(query % ag)
        r=cur.fetchall()

        if(r==[]):
            print("\nNo AGE Range Matched")
        else:
           print(tabulate(r,headers=['PID','PNAME','GENDER','FEE','AGE','WARD','DISEASE']))
          

    elif(op==5):
        en=input("Enter WARD whose record you want to see ")
        query ="select * from hospi where ward = '%s'"
        ag=(en.lower())        
        cur.execute(query % ag)
        r=cur.fetchall()
            
        if(r==[]):
            print("\nNo ward name Matched")
        else:
           print(tabulate(r,headers=['PID','PNAME','GENDER','FEE','AGE','WARD','DISEASE']))
           
    elif(op==6):
        en=input("Enter DISEASE Name whose record you want to see ")
        query ="select * from hospi where disease = '%s'"
        ag=(en.lower())        
        cur.execute(query % ag)
        r=cur.fetchall()
            
        if(r==[]):
            print("\nNo Disease name Matched")
        else:
           print(tabulate(r,headers=['PID','PNAME','GENDER','FEE','AGE','WARD','DISEASE']))
           


    else:
        print("Invalid  Option Selected ")           
    cur.close()
    con.close()

def update():
    cur=con.cursor()
    print("What do u want to update. Enter your Option ")
    #print("1.for age")
    print("1.for disease")
    print("2.for fee")
    print("3.for ward")
    print("4.for disease , fee and ward")
    op=int(input("Enter Your from Above Menu "))
    if(op==1):
        eno=int(input("Enter Id whose record you want to UPDATE "))
        query1 ="select * from hospi where pid = '%d'"
        ag1=(eno)        
        cur.execute(query1 % ag1)
        r=cur.fetchall()
        
        if(r==[]):
            print("\nNo ID Matched")
        else:
            print("Current Record are........")
            print(r)
            name=input("Enter disease ")
            query2="update hospi set disease='%s'where pid= '%d'"
            ag2=(name,eno)
            cur.execute(query2 % ag2)
            con.commit()
            print("Updated  Successfully ")
            cur.execute(query1 % ag1)
            r=cur.fetchall()
            print("New Record are........")
            print(r)
    elif(op==2):
        eno=int(input("Enter Id whose record you want to UPDATE "))
        query1 ="select * from hospi where pid = '%d'"
        ag1=(eno)        
        cur.execute(query1 % ag1)
        r=cur.fetchall()
        
        if(r==[]):
            print("\nNo ID Matched")
        else:
            print("Current Record are........")
            print(r)
            sal=int(input("Enter New fees "))
            query2="update hospi set fee='%d'where pid= '%d'"
            ag2=(sal,eno)
            cur.execute(query2 % ag2)
            con.commit()
            print("Updated  Successfully ")
            cur.execute(query1 % ag1)
            r=cur.fetchall()
            print("New Record are........")
            print(r)
    elif(op==3):
        eno=int(input("Enter Id whose record you want to UPDATE "))
        query1 ="select * from hospi where pid = '%d'"
        ag1=(eno)        
        cur.execute(query1 % ag1)
        r=cur.fetchall()
        
        if(r==[]):
            print("\nNo ID Matched")
        else:
            print("Current Record are........")
            print(r)
            w=input("Enter New Ward Name ")
            query2="update hospi set ward= '%s'where pid= '%d'"
            ag2=(w,eno)
            cur.execute(query2 % ag2)
            con.commit()
            print("Updated  Successfully ")
            cur.execute(query1 % ag1)
            r=cur.fetchall()
            print("New Record are........")
            print(r)
    elif(op==4):
        eno=int(input("Enter Id whose record you want to UPDATE "))
        query1 ="select * from hospi where pid = '%d'"
        ag1=(eno)        
        cur.execute(query1 % ag1)
        r=cur.fetchall()
        
        if(r==[]):
             print("\nNo ID Matched")
        else:
            print("Current Record are........")
            print(r)
            name=input("Enter disease ")
            sal=int(input("Enter New fee "))
            w=input("Enter new ward ")
            query2="update hospi set disease= '%s', fee='%d',ward='%s' where pid= '%d'"
            ag2=(name,sal,w,eno)
            cur.execute(query2 % ag2)
            con.commit()
            print("Updated  Successfully ")
            cur.execute(query1 % ag1)
            r=cur.fetchall()
            print("New Record are........")
            print(r)                   
    else:
        print("Invalid  Option Selected ")           
    cur.close()
    con.close()

def delete():
    cur=con.cursor()
    eno=int(input("Enter Id whose record you want to DELETE "))
    
    query1 ="select * from hospi where pid = '%d'"
    ag1=(eno)        
    cur.execute(query1 % ag1)
    r=cur.fetchall()
    if(r==[]):
        print("\nNo ID Matched")
    else:
        print("Current Record are........")
        print(r)
        ch=input("Are u surewant to delete this record. ? ")
        if(ch=="y"):
            query2="delete from hospi where pid= '%d'"
            ag2=(eno)
            cur.execute(query2 % ag2)
            con.commit()
            print("Deleted Successfully ")
            l.remove(eno)
            
            
        
            
        else:
            print("Record Not Deleted ")
            
        cur.execute("select * from hospi")
        r=cur.fetchall()
       

    if(r==[]):
            print("No Record in Table ")
    else:
            print('remaining records are: ')
            for i in r:
                print(i)
   
def insert():
    cur=con.cursor()
    print("RECORDS:")
    cur.execute("select * from hospi")
    r=cur.fetchall()
    if(r==[]):
        print("\nNo Record in Table to display")
    else:
        print(tabulate(r,headers=['PID','PNAME','GENDER','FEE','AGE','WARD','DISEASE']))
        
    eid=int(input("Enter Id "))
    while eid in l:
        print("this id already exist")
        eid=int(input("Enter another Id "))
        
    ename=input("Enter Name ")
    gen=input('enter gender')
    salary=int(input("Enter Fee "))
    age=int(input("enter age"))
    ward=input("enter ward name ")
    dis=input("enter disease name")
        
    query= "insert into hospi(pid,pname,gender,fee,age,ward,disease)values('%d','%s','%s','%d','%d','%s','%s')"
    ag=(eid,ename,gen,salary,age,ward,dis)
    cur.execute(query % ag)
    con.commit()
    print(" Record Inserted")
    cur.close()
    con.close()
        

                  

def menu():
    print("1.View All Patient Record")
    print("2.View Particular Patient Record ")
    print("3.Update Patient Record")
    print("4.Delete Patient Record ")
    print("5.Insert Patient Record ")
    print("6.Exit")
   


choice="y"
print("\t\t\t\t+ CHARISH HOSPITAL +")
print("\t\t\tDeveloped by :ISHITA SHRIVASTAVA")
while(choice=="y" or "Y"):
    con=myconnection()
    menu()
    op=int(input("Enter Your Options from above Menu "))
    if(op==1):
        selectAll()
    elif(op==2):
        selectSpecfic()
    elif(op==3):
        update()
    elif(op==4):
        delete()
    elif(op==5):
        insert()
    elif(op==6):
        print("thank you :)")
        break
   
    else:
        print("Invalid Option Opted Please ReEnter Your Option ")
    choice=input("\nDo you want to continue ? (y/n) : ")
    if (choice=="n"):
            print("thank you :)")
            break
      
