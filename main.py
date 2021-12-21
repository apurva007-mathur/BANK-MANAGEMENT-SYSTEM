import pymysql
import time
a=pymysql.connect(host='localhost',user='root',password='123456',db='project_bank')
def Open_Account():
    name=input("Account holder's name: ")
    fname=input("Father's name: ")
    dob=input("Date of birth: ")
    cn=int(input("Mobile number: "))
    gd=input("Gender: ")
    ad=input("Address: ")
    adn=int(input("Aadhar number: "))
    pcn=input("Pan number: ")
    oc=input("Occupation: ")
    act=input("Account type: ")
    ob=int(input("Opening balance: "))
    acno=int(input("Account Number: "))
    debit="Not issued"
    email=input("Email id: ")
    data=(name,fname,dob,gd,cn,ad,email,pcn,adn,oc,act,ob,acno,debit)
    data1=(acno,name,act,ob)
    sql='insert into customer_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    sql1 = 'insert into customer_balance values(%s,%s,%s,%s)'
    x=a.cursor()
    x.execute(sql,data)
    x.execute(sql1, data1)
    a.commit()
    print("Account opened successfully")
def Deposit():
    name = (input("Enter name:"))
    account_number = int(input("Enter Account number:"))
    amount = int(input("Enter Amount:"))
    date = input("Enter date:")
    x = a.cursor()
    bank_statement = ('insert into bank_statement (name,account_number,date,credit_amount) values (%s,%s,%s,%s)')
    data1 = (name, account_number, date, amount)
    x.execute(bank_statement, data1)
    b = "select bank_balance from customer_balance where account_number=%s "
    data = (account_number,)
    x.execute(b, data)
    result = x.fetchone()
    total_amount = result[0] + amount
    sql = "update customer_balance set bank_balance=%s where account_number=%s"
    d = (total_amount, account_number)
    x.execute(sql, d)
    a.commit()
    print("executed")
def withdraw():
    name = input("Enter name:")
    account_number = input("Enter Account number:")
    amount = int(input("Enter Amount:"))
    date = input("Enter date:")
    b = "select bank_balance from customer_balance where account_number=%s "
    data = (account_number,)
    x = a.cursor()
    bank_statement = ('insert into bank_statement (name,account_number,date,debit_amount) values (%s,%s,%s,%s)')
    data1 = (name, account_number, date, amount)
    x.execute(bank_statement, data1)
    x.execute(b, data)
    result = x.fetchone()
    total_amount = result[0] - amount
    sql = "update customer_balance set bank_balance=%s where account_number=%s"
    d = (total_amount, account_number)
    x.execute(sql, d)
    a.commit()
    print("executed")
def showbalance():
    account_number = input("Enter Account number:")
    b = "select bank_balance from customer_balance where account_number=%s "
    an = (account_number,)
    x = a.cursor()
    c = x.execute(b, an)
    c = x.fetchone()
    print(c[0])
    a.commit()
def Apply_For_ChequeBook():
    acc = int(input("Enter Account Number: "))
    name = input("Enter name: ")
    mobile = input("Enter Mobile Number: ")
    actype = input("Enter Account Type: ")
    cb = input("Enter number of cheque books: 1/2/3 ")
    cp = input("Enter number of cheque pages:25/50 ")
    data = (acc, name, mobile, actype, cb, cp)
    sql = 'insert into cheque_book_applicants values(%s,%s,%s,%s,%s,%s)'
    x = a.cursor()
    x.execute(sql, data)
    a.commit()
    print("You have succesfully applied for chequebook")
def cheque_payment():
    ch = input("enter checque number:")
    date = input("enter date")
    amount = int(input("enter amount"))
    rn = input("recivers name")
    account_number = int(input("enter recivers account number"))
    hacno = int(input("account holder account number"))
    b = "select bank_balance from customer_balance where account_number=%s "
    data = (account_number,)
    x = a.cursor()
    x.execute(b, data)
    result = x.fetchone()
    total_amount = result[0] + amount
    sql = "update customer_balance set bank_balance=%s where account_number=%s"
    d = (total_amount, account_number)
    x.execute(sql, d)
    data1 = (ch, date, amount, rn, account_number, hacno)
    sql = 'insert into cheque_payment values(%s,%s,%s,%s,%s,%s)'
    x.execute(sql, data1)
    a.commit()
    print("executed")
def Apply_for_Debit():
    name = input("Enter name:")
    acc = int(input("Enter account number"))
    actype = input("Enter account type")
    phone = int(input("Enter Phone Number"))
    email = input("Enter email")
    address = input("Enter address")
    debit_type = input("Enter Debit type:-VISA or RUPAY")
    data = (name, acc, actype, phone, email, address, debit_type)
    sql = 'insert into debit_applicants values(%s,%s,%s,%s,%s,%s,%s)'
    sql1 = 'update customer_details set debit_card=%s where account_number=%s'
    data1 = "Issued"
    tup = (data1, acc)
    x = a.cursor()
    x.execute(sql, data)
    x.execute(sql1, tup)
    a.commit()
    print("you have Succesfully applied for debit card")
def Apply_for_credit():
    name = input("Enter name:")
    acc = int(input("Enter account number"))
    actype = input("Enter account type")
    phone = int(input("Enter Phone Number"))
    email = input("Enter email")
    address = input("Enter address")
    credit_balance = int(input("Enter Credit limit:-"))
    data = (name, acc, actype, phone, email, address, credit_balance)
    sql = 'insert into credit_applicants values(%s,%s,%s,%s,%s,%s,%s)'
    x = a.cursor()
    x.execute(sql, data)
    a.commit()
    print("you have Succesfully applied for credit card")
def Apply_for_loan():
    name = input("Enter name:")
    email = input("Enter email:")
    phone = int(input("Enter Phone Number:"))
    state = input("Enter state:")
    loan_type = input("Enter Loan type:- GOLD,PROPERTY,STUDY,BUSINESS,CAR,PERSONAL")
    data = (name, email, phone, state, loan_type)
    sql = 'insert into loan_applicants values(%s,%s,%s,%s,%s)'
    x = a.cursor()
    x.execute(sql, data)
    a.commit()
    print("you have Succesfully applied for Loan")
def bank_statement():
    account_number = int(input("Enter Account number:"))
    b = 'select * from bank_statement where account_number=%s'
    tup = (account_number,)
    x = a.cursor()
    x.execute(b, tup)
    a.commit()
    print("Holder's Name        |    \tAccount number         |\t  Date     | \tAmount(dr)   | \tAmount(cr)")
    print("------------------------------------------------------------------------------------------------")
    for i in x:
        z = str(i[1])
        z = z.replace(z[:6], 'XXXX')
        print(i[0], "             \t  \t", z, "          \t\t", i[2], "      \t", i[3], "       \t", i[4])
while(True):

    #-------------opening------------#
    print()
    print()
    print()
    print("Who are you?\t\t1] Admin\t 2] Customer\t 3] Exit")
    c = int(input("Enter: "))
    #----------------admin-------------------------#
    if c == 1:
        while(True):
            print()
            print("Login/signup to access all the services")
            print()
            print("What do you want?  1] Log-in\t2] Sign-up\t3] Exit")
            ch = int(input("Enter: "))
        #---------login-----------#
            if ch == 1:
                email = input("Enter email: ")
                password = input("Enter password: ")
                p = 'select password from customer_login where email=%s'
                data = (email,)
                x = a.cursor()
                x.execute(p, data)
                match = ""
                for i in x:
                    match = i[0]
                if password == match:
                    print("-----------------------------------------------------------------------------")
                    print("                           Login Sucessfully                                 ")
                    time.sleep(0.5)
                    print("-----------------------------------------------------------------------------")

                    Open_Account()
                else:
                    print("-----------------------------------------------------------------------------")
                    print("                           Incorrect email/password                          ")
                    print("-----------------------------------------------------------------------------")
                    continue


        #-----------signup-----------#
            elif ch == 2:
                email = input("Enter email: ")
                password = input("Enter password")
                x = a.cursor()
                data = (email, password)
                sql = 'insert into customer_login values (%s,%s)'
                x.execute(sql, data)
                a.commit()
            elif ch==3:
                print("Good bye")
                break

        #--------------customer------------------#

    elif c==2:
     while(True):
        print()
        print("Login/signup to access all the services")
        print()
        print("1] Log-in\t2] Sign-up\t3] Exit")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            #---------login-------------#

            email = input("Enter email: ")
            password = input("Enter password: ")
            p = 'select password from customer_login where email=%s'
            data = (email,)
            x = a.cursor()
            x.execute(p, data)
            match = ""
            for i in x:
                match = i[0]
            if password == match:
                print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                new = "[Successfully logged-in]"
                for i in new:
                    print(i,end="")
                    time.sleep(0.1)
                print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                while(True):
                    service=("1] Deposit","2] Withdraw","3] Apply for loan","4] Apply for debit card","5] Apply for credit card","6] Apply for cheque book","Request for bank statement","8] Check bank balance","9] Cheque payment"," 10] Exit")
                    for i in service:
                        print(i,end=" ")
                        time.sleep(0.4)
                    print()
                    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                    choice=int(input("Please select a service: "))
                    if choice==1:
                        Deposit()
                    elif choice==2:
                        withdraw()
                    elif choice==3:
                        Apply_for_loan()
                    elif choice==4:
                        Apply_for_Debit()
                    elif choice==5:
                        Apply_for_credit()
                    elif choice==6:
                        Apply_For_ChequeBook()
                    elif choice==7:
                        bank_statement()
                    elif choice==8:
                        showbalance()
                    elif choice==9:
                        cheque_payment()
                    elif choice==10:
                        print("Good Bye")
                        break
            else:
                print("-----------------------------------------------------------------------------")
                print("                           Incorrect email/password                          ")
                print("-----------------------------------------------------------------------------")
                continue
        elif ch == 2:
                email = input("Enter email: ")
                password = input("Enter password")
                x = a.cursor()
                data = (email, password)
                sql = 'insert into customer_login values (%s,%s)'
                x.execute(sql, data)
                a.commit()
        elif ch==3:
            print("Good bye...")
            break


    elif c==3:
        print("Good bye")
        break
