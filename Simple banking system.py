Balance=1000
AccountNumber=457896
import random
class Bank:
    def account(self):
        fn=int(input("Enter Account No."))
        if fn==AccountNumber:
            o.OTP()
        else:
            print("User not founnd")  
    def choice(self):
        l=int(input("Enter your choice:"))
        if l==1:
             print("Current Balance:",Balance)
        elif l==2:
             o.Deposit()
        elif l==3:
             o.Withdrawl()
        elif l==4:
             o.saving()
        elif l==5:
             o.recurring()
        elif l==6:
             o.fixed()
        elif l==7:
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
        s=Balance*5/100
        Newbalance=Balance+s
        print("Saving Acc :",Newbalance)
    def recurring(self):
        r=Balance*7/100 
        Newbalance=Balance+r 
        print("Recurring Deposit :",Newbalance)
    def fixed(self):
        print("For 6 months:")
        f=Balance*4/100
        Newbalance=Balance+f
        print("Fixed Deposit :",Newbalance)
        print("For 12 months")  
        d=Balance*8/100
        NewBalance=Balance+d
        print("Fixed Deposit :",NewBalance) 
    def details(self):
        print("Current Balance:",Balance)  
        o.saving()
        o.recurring() 
        o.fixed() 
        
    def OTP(self):
     for i in range(2,-1,-1):
          OTP1=random.randint(1000,10000)
          print(OTP1)
          OTP2=int(input("Enter OTP\n"))
          if OTP1==OTP2:
             print("1:Balance \n 2:Deposit \n 3:Withdrawl \n 4:Saving.A \n 5:Recurring.D \n 6:Fixed.D \n 7:Details") 
             o.choice()
             exit(0)  
          else : 
            if i==0:
                print("Your account has been locked for 24 hrs\n Please contact Customer Care for more details")
            else:
                print("INCORRECT, Attempts left:",i)           
o=Bank()
o.account()