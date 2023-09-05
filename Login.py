import random
name="atul"
password="atul1234"
def OTP():
   OTP1=random.randint(1000,10000)
   print(OTP1)
   OTP2=int(input("Enter OTP"))
   if OTP1==OTP2:
      print("Name",name,"Password",password)
   else:
      OTP()   
def relogin(n,p):
    n=input("Enter your name:")
    p=input("Enter your password:")
    if n==name and p==password:
       print("Login Successfull")
    else :
       relogin(n,p)   
def login(): 
     n=input("Enter your name:")
     p=input("Enter your password:")
     if n==name and p==password:
       print("Login Successfull")      
     else:
       u=int(input("1:Relogin \n 2:Forget username and password"))
       if u==1:
          relogin(n,p)
       elif u==2:
          OTP()
login()       

