import getpass
import random
import math
import time
from os import system
import mysql.connector as c
db = c.connect(
                                host="localhost",
                                user="root",
                                password="root",
                                database="gringots")
mycursor = db.cursor()
j=0
def x():
    system('cls')
def clear():
    q = input("Enter anything to continue: ")
    system('cls')
def sym():
    print(" "*75,"_____$$_____")
    print(" "*75,"____$$$$____")
    print(" "*75,"___$$$$$$___")
    print(" "*75,"___$$__$$___")
    print(" "*75,"___$$$______")
    print(" "*75,"____$$$$____")
    print(" "*75,"______$$$___")
    print(" "*75,"___$$__$$___")
    print(" "*75,"___$$$$$$___")
    print(" "*75,"____$$$$____")
    print(" "*75,"_____$$_____")
def intro():
    print("\t\t\t\tWelcome to GRINGOTS")
    num1=random.randint(900,99999)
    print("\t\t\t\tUsers online:",num1)
def calc():
    x()
    print('''
        Enter 1 for simple intrest
        Enter 2 for compound intrest''')
    aa=int(input("Enter: "))
    if aa==1:
        x()
        P = float(input("Enter the principal amount : "))
        N = float(input("Enter the number of years : "))
        Rate = float(input("Enter the rate of interest : "))
        SI = (P * N * Rate)/100.
        print("Simple interest : ",SI)
        clear()
    elif aa==2:
        x()
        pamt=float(input("Enter the principal amount : "))
        rate = float(input("Enter the rate of interest : "))
        time = float(input("Enter the number of years : "))
        CI = pamt * (pow((1 + rate / 100), time)) 
        print("Compound interest is", CI)
        clear()
def stock():
    global j
    stock=random.randint(123,789)
    j=stock
    return j
def terms():
    x()
    terms=open("FILEE\\terms.txt","r")
    file=terms.read()
    print("The following are the Term and Conditions The bank adheres to:")
    print(file)
    terms.close()
    clear()
def signin():
    x()
    mycursor.execute("select Acc_No from data")
    acc=mycursor.fetchall()
    mycursor.execute("select Passcode from data")
    key=mycursor.fetchall()
    for i in range(len(acc)):
        acc[i]=str(acc[i])
        key[i]=str(key[i])
    for i in range(len(acc)):
        acc[i]=acc[i][1:-2]
        key[i]=key[i][2:-3]
    print(acc,key)
    sayhello()
    print("Please enter your login details:")
    an=int(input("Account no. :"))
    t=str(an)
    if t in acc:
        I=acc.index(t)
        p=str(input("Enter passcode:"))
        if key[I]==p:
                c1="select Acc_Holder from data where acc_no= (%s)"
                c="select Balance from data where Acc_No = (%s) "
                k=acc[I]
                val=[k]
                mycursor.execute(c1,val)
                ju=mycursor.fetchone()
                j2=str(ju)
                j=j2[2:-3]
                mycursor.execute(c,val)
                p1=mycursor.fetchone()
                p=str(p1)
                timelapse()
                print('Welcome,',j,"you have succesfully logged in!" )
                print("Your current balance is",p[2:-3],"INR.")
                x()
                RUN(an)
        else:
            x()
            print("Incorrect password! Please try agin!")
            clear()
    else:
        x()
        print("Account cannot be found!")
        clear()
def Acreate():
    x()
    mycursor.execute("select Acc_No from data")
    acc=mycursor.fetchall()
    for i in range(len(acc)):
        acc[i]=str(acc[i])
        acc[i]=acc[i][1:-2]
        acc[i]=int(acc[i])
    acc.sort()
    accnoo=acc[-1]
    accno=int(accnoo)+1
    num1=random.randint(900,99999)
    print("Please enter the following deatils:")
    N=input("Name of account holder: ")
    P=int(input("Phone No.(10 digits): "))
    k=str(P)
    if len(k)==10:
        SL=["Cansas","Connecticut","Delhi","Goa","Lousiana","Texas","Bengaluru","Hyderabad"]
        print("Currently we are operating in the following places.",SL)
        S1=input("Please enter one of them here: ")
        S2=S1.lower()
        S=S2.capitalize ()
        if S in SL:
            Ad=input("Address: ")
            balance=0
            print("Please enter the below given caption to verify you are not a bot.")
            print(num1)
            int1=int(input("Enter the above number here: "))
            if num1!=int1:
                print("We are sorry to inform you that account cannot be created!")
                clear()
            else:
                password=input("Please enter a password: ")
                x()
                terms()
                print('''
1. Yes, I have read the terms and conditions and agree to abide by them.
2. No, I disagree.''')
                i=input("Please choose one of the following NUMBER:")
                if i=="1":
                    x()
                    c= "insert into data values (%s,%s,%s,%s,%s,%s,%s,%s)"
                    val=(accno,N,P,S,Ad,password,0,0)
                    mycursor.execute(c, val)
                    db.commit()
                    timelapse()
                    print("Congratulations! Your account has been successfully created.")
                    print("Your Account Number is: ",accno,"please do remember it!")
                    print("Do you want to login to your account?")
                    i1=input("Please type 1 to login or 2 to not continue with the signing in..")
                    if i1=="1":
                        x()
                        RUN(accno)
                    else:
                        x()
                        print("Signing in terminated!")
                        clear()
                else:
                    x()
                    print("Terms have to be agreed to.")
                    clear()
        else:
            x()
            print("There is an error in the input.")
            clear()
    else:
        x()
        print("The no of digits in the phone no is not correct!")
        clear()        
def sayhello():
    w=["Bonjour!","Hola!","Namastey!","Hello!","Konnichiwa!","Salve!"]
    print(random.choice(w))
def timelapse():
        print("Initialising procedure...")
        time.sleep(5)
        print("Procedure successful!")
def FAQs():
     x()
     faq=open("FILEE\\faq.txt","r")
     file=faq.read()
     print(file)
     faq.close()
     clear()
def feed(accno):
    x()
    c1="select Acc_Holder from data where acc_no= (%s)"
    val=[accno]
    mycursor.execute(c1,val)
    ju=mycursor.fetchone()
    j2=str(ju)
    j=j2[2:-3]
    fout=open("FILEE\\feedback.txt","a")
    feed=str(input("Please submit your feedback here: "))
    f='"'+feed+'" -'+j+'\n'
    fout.write(f)
    fout.close()
    print("Thankyou for your feedback!")
    clear()
def abt():
    x()
    faq=open("FILEE\\Aboutus.txt","r")
    file=faq.read()
    print(file)
    faq.close()
    clear()
def transact(accno):
    x()
    t=1
    c = "select Balance from data where Acc_No = (%s)"
    val=[accno]
    mycursor.execute(c,val)
    C1=mycursor.fetchone()
    balance=str(C1)
    Ci=balance[2:-3]
    C=int(Ci)
    m=C
    while t<100:
        print('''Do you want to transact further?''')
        A=str(input("enter yes or no."))
        if A=='yes':
            x()
            print("Enter 1 to deposit cash and 2 to withdraw:")
            a=int(input("d/w: "))
            if a==1:
                x()
                c=int(input("Please enter the cash amt. to be deposited: "))
                m=int(C)+c
                print("Your account balance is",m,"INR")
                C=m
                t+=1
                clear()
            elif a==2:
                x()
                c=int(input("Please enter cash to be widrawed"))
                if c<int(C):
                    m=int(C)-c
                    print("Your account balance is",m,"INR")
                    C=m
                    t+=1
                    clear()
                elif c>int(C):
                    x()
                    print("Acc. bal insufficient.")
                    t+=1
                    clear()
            else:
                x()
                print("You entered a wrong value!!!")
                clear()
        elif A=='no':
            x()
            C=m
            c="update data set Balance=%s where Acc_No=%s"
            val=(m,accno)
            mycursor.execute(c,val)
            db.commit()
            print("Your account balance is",m,"INR")
            print("Happy transactions!")
            clear()
            break
        else:
            print("Wrong input!")
            clear()
def choice(accno):
    x()
    print(''' PLEASE CHOOSE ONE OF THE DETAILS TO BE UPDATED:
1. Name
2. Address
3. Phone Number
4. Reset passcode
5. Change State''')
    a3=int(input("Please enter your choice here: "))
    l=[0,"Acc_Holder","Address","Contact_No","Passcode"]
    l1a="select "
    l1b=" from data where Acc_No=%s"
    l2a="update data set "
    l2b="=%s where Acc_No=%s"
    if a3 in [1,2,3,4]:
        updater(accno,a3)
    elif a3==5:
        x()
        print('''This may take a little time.
Please wait while we initialise your request.
Meanwhile, please go through the below provided list for state change.
Thank you.''')
        SL=["Cansas","Connecticut","Delhi","Goa","Lousiana","Texas","Bengaluru","Hyderabad"]      
        print(SL)
        time.sleep(10)
        n=input("Enter the new state here: ")
        c = "update data set State=%s where Acc_no=%s"
        val=(n,accno)
        mycursor.execute(c,val)
        timelapse()
        clear()
    else:
        x()
        print("Wrong entry!")
        clear()
        
    
def updater(accno,a3):
    x()
    l=[0,"Acc_Holder","Address","Contact_No","Passcode"]
    l1a="select "
    l1b=" from data where Acc_No=(%s)"
    l2a="update data set "
    l2b="=%s where Acc_No=(%s)"
    a4=int(a3)
    if a4 in [1,2,3,4]:
        c1=l1a+l[a4]+l1b
        c2=l2a+l[a4]+l2b
        val=[accno]
        mycursor.execute(c1,val)
        before=mycursor.fetchone()
        print("Data before updation is: ",before)
        a=input("Please enter the updated data here: ")
        val=(a,accno)
        mycursor.execute(c2,val)
        print("Do you wish to proceed furthur? Please  note this can't be undone.")
        b=input("Enter y to continue (Any other response will cancel the deletion procedure): ")
        if b=="y":
            db.commit()
            print("Updation successful!")
            print("Updated data input is: ",a)
            clear()
        else:
            print("Cancelling updation...")
    else:
        print("Wrong input entered")
        clear()
def delacc(accno):
    print("Do you wish to proceed furthur? Please  note this can't be undone.")
    time.sleep(3)
    a=input("Enter y to continue (Any other response will cancel the deletion procedure): ")
    if a=="y":
        x()
        cmnd = "delete from data where Acc_no= (%s)"
        val = [accno]
        mycursor.execute(cmnd, val)
        db.commit()
        timelapse()
        clear()
def stockportal(accno):
    x()
    c = "select Balance from data where Acc_No = (%s)"
    val=[accno]
    mycursor.execute(c,val)
    C1=mycursor.fetchone()
    balance=str(C1)
    Ci=balance[2:-3]
    C=int(Ci)
    c = "select stocks from data where Acc_No = (%s)"
    val=[accno]
    mycursor.execute(c,val)
    S1=mycursor.fetchone()
    sto=str(S1)
    Si=sto[1:-2]
    S=int(Si)
    print('''Welcome to the Stock Money Portal. What would you like to do?
1. Buy stocks
2. Sell stocks
3. Access the intrest calculator
Please note that value of the stock is subject to market risk. The bank will not be responsible for any losses, (if they occur)''')
    print("Your current balance is: ",C,"and withheld stock(s) are: ",S)
    n=int(input("Enter your choice here: "))
    if n==1:
        x()
        stock()
        print("The current stock value is",j,"INR")
        print("Max no. of shares that can be bought at once are 50.")
        print("Your current balance is: ",C,"and withheld stock(s) are: ",S)
        ns=int(input("How many stocks would you like to buy?: "))
        if ns>0 and ns<=50:
            k=ns*j
            print("The net amount about to be deducted from your bank account is",k,"INR.")
            na=input("Do you wish to continue? Enter y to carry out transaction (any other response will end in termination)")
            if  na=="y":
                print("Launching link procedure to your vault...")
                timelapse()
                st=S+ns
                ba=C-k
                if ba>=0:
                    c = "update data set Stocks=%s, balance=%s where Acc_no=%s"
                    val=(st,ba,accno)
                    mycursor.execute(c,val)
                    db.commit()
                    print("Transaction completed successfully!")
                    print("Your account balance is: ",ba,"INR")
                    print("No. of stocks held: ",st)
                    clear()
                else:
                    print("Insufficient balance!")
                    clear()
            else:
                print("No transaction was initiated")
                clear()
        else:
            print("No transaction was initiated")
            clear()
    elif n==2:
        x()
        stock()
        print("The current stock value is",j,"INR")
        print("Max no. of shares that can be sold at once are 50.")
        print("Your current balance is: ",C,"and withheld stock(s) are: ",S)
        ns=int(input("How many stocks would you like to sell?: "))
        if ns>0 and ns<=50 and ns<=S:
            k=ns*j
            print("The net amount about to be added to your bank account is",k,"INR.")
            na=input("Do you wish to continue? Enter y to carry out transaction (any other response will end in termination)")
            if  na=="y":
                print("Launching link procedure to your vault...")
                timelapse()
                st=S-ns
                ba=C+k
                c = "update data set Stocks=%s, balance=%s where Acc_no=%s"
                val=(st,ba,accno)
                mycursor.execute(c,val)
                db.commit()
                print("Transaction completed successfully!")
                print("Your account balance is: ",ba,"INR")
                print("No. of stocks held: ",st)
                clear()
            else:
                print("No transaction was initiated")
                clear()
        else:
            print("No transaction was initiated")
            clear()
    elif n==3:
            calc()
    else:
            print("An error occured!")
            clear()
def RUN(accno):
    x()
    print('''
The following numbers correspond to the tasks. Please  select a number from the given options.
1. Carry out transactions
2. Enter the stock portal
3. Edit or view details
4. Leave us a feedback
5. View important document files
6. Logout
7. Delete this account''')
    i2=int(input("Please enter your choice here: "))
    if i2==1:
        transact(accno)
        RUN(accno)
    elif i2==2:
        timelapse()
        stockportal(accno)
        RUN(accno)
            
    elif i2==3:
        x()
        print(''' Please choose a number correspondig to your choice
1. View personal detail portfolio
2. To edit information''')
        n=int(input("Enter your choice here: "))
        if n==1:
            x()
            c="select * from data where Acc_no=(%s)"
            val=[accno]
            mycursor.execute(c,val)
            p=mycursor.fetchall()
            t1=list(p)
            t=list(t1[0])
            k=["Account  No: ","Name of account holder: ","Contact number: ","State: ","Address: ","Passcode: ","Current balance","Stocks withheld: "]
            for i in range(len(t)):
                print(k[i],t[i])
            clear()
        elif n==2:
            choice(accno)
        else:
            print("Wrong input entered!")
            clear()
        RUN(accno)
    elif i2==4:
        feed(accno)
        RUN(accno)
    elif i2==5:
        x()
        print('''Please choose a number correspondig to your choice
1. Read through FAQs
2. Access terms and conditions
3. Know more about us''')
        n=int(input("Enter your choice here: "))
        if n==1:
            FAQs()
        elif n==2:
            terms()
        elif n==3:
            abt()
        else:
            x()
            print("An error occured")
            clear()
        RUN(accno)
    elif i2==6:
        x()
        timelapse()
        print("Thankyou  for banking with us. See you soon!")
    elif i2==7:
        x()
        delacc(accno)
        print("Thankyou for banking with us.")
        clear()
    else:
        x()
        print("A wrong input might have been entered!")
        q = input("Enter anything to go back: ")
        system('cls')
        RUN(accno)
def AdminIn():
    x()
    print(''' The number correponds to the task:
1 To view or edit details
2 To create or delete an account
3 View feedback
4 Generate queries by accessing command client
5 To see the total amount of cash in bank
6 Shift back to normal bank mode''')
    mycursor.execute("select Acc_No from data")
    acclst=mycursor.fetchall()
    for i in range(len(acclst)):
        acclst[i]=str(acclst[i])
        acclst[i]=acclst[i][1:-2]
        acclst[i]=int(acclst[i])
    j=int(input("Enter your response here: "))
    if j==1:
        x()
        print('''
1. To see the list of Account Holders
2. To view full details of a particular Acc Holder 
3. To edit information of a particular Account''')
        j1=int(input("Select an option: "))
        if j1==1:
            x()
            mycursor.execute("select Acc_No, Acc_Holder, Balance,stocks from data")
            l=mycursor.fetchall()
            k=["Account  No: ","Name of account holder: ","Current balance","Stocks withheld: "]
            t1=list(l)
            for i in range(len(t1)):
                t=list(t1[i])
                print(k[0],t[0],"     ", k[1],t[1],"      ",k[2],t[2],"       ",k[3],t[3])
            clear()
        elif j1==2:
            x()
            print("Please ensure that the account no is in the following list, ",acclst)
            j2=int(input("Enter account no for which informaion has to be accessed: "))
            if j2 in acclst:
                c="select * from data where Acc_No = (%s)"
                val=[j2]
                mycursor.execute(c,val)
                l=mycursor.fetchall()
                t1=list(l)
                t=list(t1[0])
                k=["Account  No: ","Name of account holder: ","Contact number: ","State: ","Address: ","Passcode: ","Current balance: ","Stocks withheld: "]
                for i in range(len(k)):
                    print(k[i],t[i])
                clear()
            else:
                print("Account not found")
                clear()
        elif j1==3:
            system('cls')
            print("Please ensure that the account no is in the following list, ",acclst)
            j2=int(input("Enter account no for which informaion has to be accessed: "))
            if j2 in acclst:
                print('''Alter options:
    1. Acc_No
    2.Acc_Holder
    3.Contact_No
    4.State
    5.Address
    6.Passcode''')
                j3=int(input("Enter choice: "))
                jl=["Acc_No", "Acc_Holder", "Contact_No", "State", "Address", "Passcode"]
                adminupdate(j3)
                clear()
            else:
                print("Account not found")
                clear()
        else:
            print("Wrong input")
            clear()
        AdminIn()
    if j==2:
        system('cls')
        print('''Choose the task to be performed
1. Create an account
2. Delete an account''')
        n=int(input("Enter your choice here: "))
        if n==1:
            system('cls')
            SL=["Cansas","Connecticut","Delhi","Goa","Lousiana","Texas","New York","Bengaluru","Hyderabad"]
            a1=int(input("Acc_No: "))
            a2=input("Account_Holder: ")
            a3=int("Contact_No: ")
            print(SL)
            print("Enter one of the above mentioned states only.")
            a4=input("State: ")
            a5=input("Address: ")
            a6=input("Passcode: ")
            a7=int("Balance: ")
            a8=int("Stocks: ")
            if len(a3)==10 and a4 in SL:
                c="insert into data values(%s,%s,%s,%s,%s,%s,%s,%s)"
                val=(a1,a2,a3,a4,a5,a6,a7,a8)
                mycursor.execute(c,val)
                db.commit()
                timelapse()
                clear()
            else:
                print("There was an error,Admin")
                clear()
        elif n==2:
            system('cls')
            print("Please ensure that the account no is in the following list, ",acclst)
            j2=int(input("Enter account no of the account which has to be deleted: "))
            if j2 in acclst:
                delacc(j2)
            else:
                print("Account not found")
                clear()
        else:
            print("Wrong input entered!")
            clear()
        AdminIn()
    if j==3:
        system('cls')
        fout=open("FILEE\\feedback.txt","r")
        j1=fout.readlines()
        for i in range(len(j1)):
            print(j1[i])
        fout.close()
        clear()
        AdminIn()
    if j==4:
        system('cls')
        k=1
        ch="y"
        print("Linking with Command Client")
        time.sleep(5)
        print("Linked successfully!")
        while k==1 and ch!="n":
            c=input("SELECT type Command line: ")
            mycursor.execute(c)
            t2=mycursor.fetchall()
            t1=list(t2)
            for i in range(len(t1)):
                t=list(t1[i])
                print(t)
            ch=input("More queries? Enter n to break loop")
            system('cls')
        AdminIn()
    if j==5:
        system('cls')
        print("Initialising prepare to go through the cash vaults...")
        time.sleep(5)
        print("Fetching resources..")
        time.sleep(8)
        c="select sum(balance) from data"
        mycursor.execute(c)
        p1=mycursor.fetchall()
        p2=str(p1)
        print("Total cash as of now is, ",p2[2:-3],"INR")
        clear()
        AdminIn()
    if j==6:
        system('cls')
        print("Shifting to normalised bank mode..")
        timelapse()
        system('cls')
def adminupdate(j3):
    t1="update data set "
    t2="=%s where Acc_No=%s"
    p=int(j3)-1
    c1=t1+j[p]+t2
    j4=input("Enter new value: ")
    val=(j4,j1)
    mycursor.execute(c1,val)
    db.commit()
    print("Update successful!")
    
            
qq=1
I=0
sym()
intro()
while qq==1:
    print('''
    PRESS 1 TO SIGN IN
    PRESS 2 TO CREATE AN ACCOUNT
    PRESS 3 TO VIEW OUR CURRENT STOCK VALUE''')
    re=int(input("ENTER HERE: "))
    if re==1:
        system('cls')
        signin()
    elif re==2:
        system('cls')
        Acreate()
    elif re==3:
        stock()
        print("The current stock value is",j,"INR")
    elif re==2402:
        n=int(input("Wrong input please try again."))
        if n==2402:
            system('cls')
            print("Welcome Administrator")
            AdminIn()
    else:
        print("Wrong input please try again.")




