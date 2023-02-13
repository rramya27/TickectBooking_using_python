from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017")
import calendar
import random
import re
from datetime import date
print("------------FLIGHT TICKETS--------------")
print("Welcome to Flying bird air lines")
class ticket:
    def __init__(self):
        self.person=20
        self.phnno=str(input("Enter the mobile number:"))
        self.password=str(input("Enter the password:"))
        self.cost=0
        self.details=0
        self.Amt=0
    def paymentmethod(self):
        print("1.Bank tranfer\n 2.Google pay")
        choice=int(input("Enter the choice:"))
        if(choice==1):
            bt=str(input("Enter yor 15 digit account number:"))
            if(len(bt)==15):
                num=input("Enter the mobile number:")
                r=re.fullmatch('[6-9][0-9]{9}',num)
                if r!=None:
                    print("valid")
                    pin=str(input("Enter the 4 digit pin number:"))
                    if(len(pin)==4):
                        print("Your payment has been done successfully")
                        tickectno=random.randint(0,1000)
                        Date=date.today()
                        date=str(Date)
                        a=client["TicketBooking"]
                        Number=self.phnno
                        b=a[Number]
                        b.insert_one({"TicketNumber":tickectno,"Date":date,"Mobile number":self.phnno,"Adult":self.details,"Total cost":self.Amt})
                        print(f"Total no of person:{self.details}\n Total cost:{self.Amt}\n Your's ticket has been booked successfully @ {date} \n Have a safe and happy journey :)")                        
                    else:
                        print("please,Enter the valid pin")
                else:
                    print("Invalid")
            else:
                print("please,enter the correct account number")
        elif(choice==2):
            num=input("Enter the mobile number:")
            r=re.fullmatch('[6-9][0-9]{9}',num)
            if r!=None:
                print("valid")
                passcode=str(input("Enter the 6 digit passcode:"))
                if(len(passcode)==6):
                    print("Your payment has been done successfully")
                    tickectno=random.randint(0,1000)
                    Date=date.today()
                    a=client["TicketBooking"]
                    Number=self.phnno
                    b=a[Number]
                    b.insert_one({"TicketNumber":tickectno,"Date":date,"Mobile number":self.phnno,"Adult":self.details,"Total cost":self.Amt})
                    print("--------------------------------------------")
                    print(f"Total no of person:{self.details}\n Total cost:{self.Amt}\n Your's ticket has been booked successfully @ {date} \n Have a safe and happy journey :)")
                    print("--------------------------------------------")
                else:
                    print("please,Enter the valid pin")
            else:
                print("Invalid /n please enter the correct number")
        else:
            print("None to the choice.please,Enter the correct choice")            
    def persondetails(self):
        self.details=int(input("Enter the number of person:"))
        if(self.details<=self.person):
            i=0
            while(i<self.details):
                i=i+1
                print("------------------------------------")
                name=str(input("Enter the name:"))
                age=int(input("Enter the age:"))
                location=str(input("Enter the current location:"))
                a=client["TicketBooking"]
                Number=self.phnno
                b=a[Number]
                b.insert_one({"Name":name,"Age":age,"Location":location})
        else:
            return("please,Enter less members")
        phn1=input("Enter your register mobile number:")
        if(phn1==self.phnno):
            print("---Verified---")
            password1=input("Enter the password:")
            if(password1==self.password):
                print("---Verified----")
                print("otp has been send to your register mobile number",self.phnno)
                otp1=random.randint(1111,9999)
                print("otp number==>",otp1)
                otp=int(input("Enter the opt number:"))
                if(otp==otp1):
                    print("verified otp")
                    self.Amt=self.cost*self.details
                    print(f"Total==>{self.Amt}")
                    t1.paymentmethod()
                else:
                    print("Please,Enter the valid otp")                
            else:
                print("please,Enter the correct password")
        else:
            print("please,Enter the correct number")    
class availableticket(ticket):
    def available(self):
        print(" ")
        print("1.Chennai-bangalore    --- Air india @ 10Am \n 2.Chennai-coimbatore  --- Air india @ 10Am\n 3.Chennai-Delhi        --- Ingico air lines @ 4pm")
        print(" ")
        for choice in range(0,2):
            destination=int(input("Enter the destination:"))
            if(destination==1):
                print("1.Chennai-bangalore \n Air india @ 10Am")
                print("----Rs:3000/per person----")
                self.cost=3000
                t1.persondetails()                
            elif(destination==2):
                print("2.Chennai-coimbatore \n Air india @ 10Am")
                print("----Rs.4500/per person----")
                self.cost=4500
                t1.persondetails()   
            elif(destination==3):
                print("3.Chennai-Delhi \n Ingico air lines @ 4pm")
                print("----Rs:4800/per person----")
                self.cost=4800
                t1.persondetails()
            else:
                print("Please,Enter the correct option")
        else:
            View=str(input("Did you need to view your ticket yes/no:"))
            if(View=="yes"):
                a=client["TicketBooking"]
                Number=str(input("Enter your registed phn number"))
                b=a[Number]
                for i in b.find({},{"_id":0,"TicketNumber":1,"Date":1,"Mobile number":1,"Adult":1,"Total cost":1}):
                    print(i)
            elif(View=="no"):
                print("Thank u visting this visiting")
            
class logindetails(availableticket):
    def phn(self):
        number=self.phnno
        r=re.fullmatch('[6-9][0-9]{9}',number)
        if r!=None:
            print("valid mob number")
            user=self.password
            length=len(user)
            if(length>=8):
                print("valid password")
                return(t1.available())
            else:
                print("invalid password-please enter more than 8 character")
        else:
            print("Please,Enter the correct mobile number")        
t1=logindetails()
t1.phn()

