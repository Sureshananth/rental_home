import mysql.connector
from datetime import datetime
mydb=mysql.connector.connect(host="localhost",user="root",password="Suresh@123",database="rental_home")
mycursor=mydb.cursor()

def validate_login(user_name,password):
    mycursor.execute("select * from user_details where username like %s",(user_name,))
    data=mycursor.fetchall()
    print(data)
    if user_name==data[0][1] and password==data[0][2]:
        print("log in successfull")
        return 1
def rental(user_name,password):
    crg=int(input("how much feet"))
    mycursor.execute("select * from rental_house_details where housesqaurefeet like %s",(crg,))   
    data=mycursor.fetchall()
    print(data)
    count=0
    for i in data:
        count=count+1
        print("house id",i[0])
        print("HOUSE NUMBER",count)
        print("housetype",i[1])
        print("housesqaruefeet",i[2])
        print("houseownername",i[3])
        print("location",i[4])
        print("city",i[5])
        print("rent",i[6])
        print("-------------------------------------------")
    while True:
        needbook=input("do you want booking the rental home then type yes or no")
        if needbook=="yes":
            homeid=int(input("enter home id which you have to select"))
            mycursor.execute("select * from rental_house_details where rentalid like %s",(homeid,))
            data1=mycursor.fetchall()
            print(data1)
            rentalid=data1[0][0]
            mycursor.execute("select * from user_details where username like %s",(user_name,))
            data2=mycursor.fetchall()
            print(data2)
            user_id=data2[0][0]
            username=data2[0][1]  
            phoneno=data2[0][3]
            print(phoneno)
            print("ook")
            mycursor.execute("insert into booking_rent(bookid,user_id,username,rentalid,phoneno)values(null,%s,%s,%s,%s)",(user_id,username,rentalid,phoneno,))
            mydb.commit()
        elif needbook=="no":
            print("if the home available notification")
            break 
    return 1   
def publish(user_name,password):
    print("please enter the below details publish your house")
    mycursor.execute("select * from user_details where username like %s",(user_name,))
    data=mycursor.fetchall()
    userid=data[0][0]
    username=data[0][1]
    housetype=input("enter your house type like 2bhk or 3bhk or 4bhk")
    feet=int(input("enter your squarefeet"))
    ownername=input("enter your ownername")
    phoneno=int(input("enter your phoneno"))
    rent=int(input("enter your rent fees"))
    location=input("enter your location")
    mycursor.execute("insert into req_rental_home(req_id,user_id,home_type,feet,owner_name,phone_no,rent,location)values(null,%s,%s,%s,%s,%s,%s,%s)",(userid,housetype,feet,ownername,phoneno,rent,location,))
    mydb.commit()
    print("Laterally you will get notifications from our side")
    return 1
def admin_login(adminname,adminpassword):
    mycursor.execute("select * from admin where adminname like %s",(adminname,))
    data=mycursor.fetchall()
    print(data)
    if adminname==data[0][1] and adminpassword==data[0][2]:
        print("admin log in successfull")
        return 1

def admin_check(adminname,adminpassword):
    a=input("userdetails or renthomedetails or requesthomedetails or type here")
    if a=="userdetails":
        while True:
            user_id=int(input("enter your userid to check details"))
            mycursor.execute("select * from user_details where user_id like %s",(user_id,))
            data=mycursor.fetchall()
            for i in data:
                print("userid",i[0])
                print("username",i[1])
                print("email",i[4])
                print("phoneno",i[3])
                print("useraddress",i[5])
            break
    if  a=="rentalhomedetails":
        while True:
            rentalid=int(input("enter your userid to check details"))
            mycursor.execute("select * from rental_house_details where rentalid like %s",(rentalid,))
            data1=mycursor.fetchall()
            for i in data1:
                print("rentalid",i[0])
                print("housetype",i[1])
                print("housesqaurefeet",i[2])
                print("houseownername",i[3])
                print("location",i[4])
                print("city",i[5])
                print("rent",i[6])
            break
        if  a=="requesthomedetails":
            while True:
                req_id=int(input("enter your userid to check details"))
                mycursor.execute("select * from  requesthomedetails where req_id like %s",(req_id,))
                data2=mycursor.fetchall()
                for i in data2:
                    print("reqid",i[0])
                    print("userid",i[1])
                    print("hometype",i[2])
                    print("feet",i[3])
                    print("ownername",i[4])
                    print("phoneno",i[5])
                    print("rent",i[6])
                    print("location",i[7])
                break
        if  a=="bookingdetails":
            while True:
                book_id=int(input("enter your userid to check details"))
                mycursor.execute("select * from  bookid where book_id like %s",(book_id,))
                data3=mycursor.fetchall()
                for i in data3:
                    print("bookid",i[0])
                    print("userid",i[1])
                    print("username",i[2])
                    print("rentalid",i[3])
                    print("phoneno",i[4])
                break
    return 1        

s=input("enter your user or new_user or admin")
#s=s.lower()
if s=="user":
    user_name=input("enter your username")
    password=input("enter your password")
    youare=input("R you rental_publisher or customer type here")
    if youare=="customer":
        if validate_login(user_name,password):
            if rental(user_name,password):
               print("ok")
    elif youare=="rental_publisher":
        if publish(user_name,password):
            print("success")               
if s=="new_user":
    user_name=input("ENTER YOUR USER_NAME  :")
    password=input("ENTER YOUR PASSWORD  :")
    phoneno=int(input("ENTER YOUR MOBILE NO  :"))
    email=input("ENTER YOUR EMAIL ID  :")
    useraddress=input("ENTER YOUR ADDRESS:")
    mycursor.execute("insert into user_details(user_id,username,password,phoneno,email,useraddress)values(null,%s,%s,%s,%s,%s)",(user_name,password,phoneno,email,useraddress,))
    mydb.commit()
    print("resistration success, go to log in page")
    youare=input("R you rental_publisher or customer type here")
    if youare=="customer":
       if validate_login(user_name,password):
           if rental(user_name,password):
              print("success")
    elif youare=="rental_publisher":
        if publish(user_name,password):
            print("success")
if s=="admin":
    adminname=input("enter admin name")
    adminpassword=input("enter admin password")
    if admin_login(adminname,adminpassword):
        if admin_check(adminname,adminpassword):
            print("ok")

