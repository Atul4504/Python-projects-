import random
import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
class Bank:   
    def __init__(self):
        self.Balance = 1000
        self.AccountNumber = 457896
        self.window = root
        self.window.title("Banking Application")
        self.correct_OTP= None
        self.remaining_attempts=3

    def account(self):
        self.fn = int(self.entry_account.get())
        if self.fn == self.AccountNumber:
           tk.Button(text="Send OTP",command=self.OTP).pack()
        else:
            messagebox.showerror("Error", "User not found")

    def choice(self):
        l = int(self.entry_choice.get())
        if l == 1:
            messagebox.showinfo("Current Balance", f"Current Balance: {self.Balance}")
        elif l == 2:
            self.h()
        elif l == 3:
            self.k()
        elif l == 4:
            self.saving()
        elif l == 5:
            self.recurring()
        elif l == 6:
            self.fixed()
        elif l == 7:
            self.details()
        else:
            messagebox.showerror("Error", "Wrong choice!!")

    def Deposit(self):
        self.n = int(self.entry_deposit.get())
        self.NewBalance = self.Balance + self.n
        messagebox.showinfo("Deposit", f"New Balance: {self.NewBalance}")

    def Withdrawl(self):
        self.m = int(self.entry_withdraw.get())
        self.Newbalance = self.Balance - self.m
        if self.m > self.Balance:
            messagebox.showerror("Error", "Insufficient balance")
        elif self.m == self.Balance:
            messagebox.showinfo("Withdrawal", "Balance=0")
        else:
            messagebox.showinfo("Withdrawal", f"New Balance: {self.Newbalance}")

    def saving(self):
        s = self.Balance * 7 / 100
        Newbalance = self.Balance + s
        tk.Label(self.window, text=f"Saving Account Balance: {Newbalance}").pack()

    def recurring(self):
        r = self.Balance * 7 / 100
        Newbalance = self.Balance + r
        tk.Label(self.window, text=f"Recurring Deposit Balance: {Newbalance}").pack()

    def fixed(self):
        f = self.Balance * 4 / 100
        Newbalance = self.Balance + f
        tk.Label(self.window, text=f"Fixed Deposit (6 months) Balance: {Newbalance}").pack()

        d = self.Balance * 8 / 100
        NewBalance = self.Balance + d
        tk.Label(self.window, text=f"Fixed Deposit (12 months) Balance: {Newbalance}").pack()
        

    def details(self):
       tk.Label(self.window, text="Account Details").pack()
       tk.Label(self.window, text=f"Current Balance: {self.Balance}").pack()
       self.saving()
       self.recurring()
       self.fixed()

    def OTP(self): 
            self.correct_OTP=random.randint(1000,10000)
            messagebox.showinfo("OTP", f"Your OTP: {self.correct_OTP}")
            self.th()
            self.check_otp_button=tk.Button(text="Check OTP",command=self.gh)
            self.check_otp_button.pack()
          
    def gh(self):
         self.OTP2 = int(self.entry_OTP.get())
         if self.correct_OTP == self.OTP2:
                self.fh()
         else:
                self.remaining_attempts-=1
                if self.remaining_attempts == 0:
                    messagebox.showerror("Error", "Your account has been locked for 24 hrs.\n Please visit the bank for more details.")
                    self.window.destroy()
                else:
                    messagebox.showerror("Error", f"INCORRECT, Attempts left: {self.remaining_attempts}")
                    self.remove_widgets()
                
                    

    def run(self):
        tk.Label(self.window, text="Enter Account No.").pack()
        self.entry_account = tk.Entry(self.window)
        self.entry_account.pack()
        tk.Button(self.window, text="Login", command=self.account).pack()
   
    def th(self):
        self.otp_label=tk.Label(text="Enter OTP")
        self.otp_label.pack()
        self.entry_OTP = tk.Entry()
        self.entry_OTP.pack()
        

    def fh(self):
        tk.Label(self.window,text="Logged In,\n 1: Balance\n2: Deposit\n3: Withdrawl\n4: Saving.A\n5: Recurring.D\n6: Fixed.D\n7: Details").pack()
        tk.Label(self.window,text="Enter Choice:").pack()
        self.entry_choice = tk.Entry(self.window)
        self.entry_choice.pack()
        tk.Button(self.window,text="Details",command=self.choice).pack()  
    
    def h(self):
        tk.Label(text="Enter Amount to be deposited:").pack()
        self.entry_deposit = tk.Entry()
        self.entry_deposit.pack()
        tk.Button(text="Deposit",command=self.Deposit).pack()  

    def k(self):
        tk.Label(text="Enter Amount to be withdrawl:").pack()
        self.entry_withdraw = tk.Entry()
        self.entry_withdraw.pack()
        tk.Button(text="Withdrawl",command=self.Withdrawl).pack()  

    def remove_widgets(self):
        self.entry_OTP.pack_forget()
        self.otp_label.pack_forget()
        self.check_otp_button.pack_forget()
        self.OTP()
        

o=Bank()
o.run()


root.mainloop()