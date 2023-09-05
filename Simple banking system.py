Balance=1000
AccountNumber=457896
class Bank:
    def account(self):
        fn=int(input("Enter Account No."))
        if fn==AccountNumber:
            print("1:Balance \n 2:Deposit \n 3:Withdrawl \n 4:Saving.A \n 5:Current.A \n 6:Recurring.D \n 7:Fixed.D \n 8:Details")
            o.choice()
        else:
            print("User not founnd")  
    def choice(self):
        l=int(input("Enter your choice:"))
        if l==1:
             print("Balance:",Balance)
        elif l==2:
             o.Deposit()
        elif l==3:
             o.Withdrawl()
        elif l==4:
             o.saving()
        elif l==5: 
             o.current()
        elif l==6:
             o.recurring()
        elif l==7:
             o.fixed()
        elif l==8:
             o.details()     
        else:
             print("wrong choice!!")     
    def Deposit(self):
        self.n=int(input("Enter the amount of money you want to add:"))
        self.NewBalance=Balance+self.n
        print("Balance",self.NewBalance)   
    def Withdrawl(self):
        self.m=int(input("Enter the amount of money you want to Withdrawl:"))
        self.Newbalance=Balance-self.m
        if self.m>Balance:
           print("Insufficient balance")
        elif self.m==Balance:
           print("Balance=0")
        else:     
           print("Balance",self.Newbalance)
    def saving(self):
        s=Balance*3/100
        Newbalance=Balance+s
        print("Saving Acc :",Newbalance)
    def current(self):
        c=Balance*2/100
        Newbalance=Balance+c
        print("Current Acc :",Newbalance)
    def recurring(self):
        r=Balance*6/100 
        Newbalance=Balance+r 
        print("Recurring Deposit :",Newbalance)
    def fixed(self):
        print("For 6 months:")
        f=Balance*3/100
        Newbalance=Balance+f
        print("Fixed Deposit :",Newbalance)
        print("For 12 months")  
        d=Balance*7/100
        NewBalance=Balance+d
        print("Fixed Deposit :",NewBalance) 
    def details(self):
        print("Balance:",Balance)  
        o.saving()
        o.current()
        o.recurring() 
        o.fixed() 
o=Bank()
o.account()