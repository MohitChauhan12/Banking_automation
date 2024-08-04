#!/usr/bin/env python
# coding: utf-8

# In[5]:


from tkinter import *
import sqlite3
import time
from tkinter.ttk import Combobox
from tkinter import messagebox
import re
import random
import gmail
from tkinter.ttk import Style,Treeview,Scrollbar


try:
    conobj=sqlite3.connect(database="bank.sqlite")
    curobj=conobj.cursor()
    curobj.execute("create table acn(acn_no integer primary key autoincrement,acn_name text,acn_pass text,acn_email text,acn_mob text,acn_bal float,acn_opendate text,acn_gender text,acn_type text)")
    curobj.execute("create table txn(acn int,txn_amt float,txn_type float,txn_date text,update_bal float)")
    conobj.close()
    print("table created")
except:
    print("Table exists")
    
win=Tk()
win.state('zoomed')
win.configure(bg='light green')
win.resizable(width=False,height=False)

title=Label(win,text="Banking Automation (Admin)",font=('arial',50,'bold','underline'),bg='light green')
title.pack()
dt=time.strftime("%d %B %Y,%A")
date=Label(win,text=f"{dt}",font=('arial',17,'bold'),bg='light green',fg='blue')
date.place(relx=.80,rely=.11)

lal_info=Label(win,text="Developed By: Mohit Chauhan",font=('arial',17,'bold'),bg='light green')
lal_info.place(relx=.01,rely=.85)

lal_info=Label(win,text="Email ID: mohitchauhan639821@gmail.com",font=('arial',17,'bold'),bg='light green')
lal_info.place(relx=.01,rely=.90)

lal_info=Label(win,text="For testing purpose, use Account number '1' and Password '123456'",font=('arial',17,'bold'),bg='light green',fg='red')
lal_info.place(relx=.01,rely=.95)

def main_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.16,relwidth=1,relheight=.68)
       
    def admin():
        frm.destroy()
        admin_screen()

    def forgotpass():
        frm.destroy()
        forgotpass_screen()

    def newuser():
        frm.destroy()
        newuser_screen()

    def login():
        global gacn
        gacn=e_acn.get()
        pwd=e_pass.get()
        if len(gacn)==0 or len(pwd)==0:
            messagebox.showwarning("Validation","Empty fields are not allowed")
            return
        else:
            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select * from acn where acn_no=? and acn_pass=?",(gacn,pwd))
            tup=curobj.fetchone()
            conobj.close()
            if tup==None:
                messagebox.showerror("Error","Invalid ACN/PASS")
            else:
                frm.destroy()
                welcome_screen()

    def clear():
        e_acn.delete(0,"end")
        e_pass.delete(0,"end")
        
    lbl_acn=Label(frm,text="Account number",font=('arial',20,'bold'),bg='powder blue')
    lbl_acn.place(relx=.2,rely=.1)

    e_acn=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_acn.place(relx=.4,rely=.1)
    e_acn.focus()

    lbl_pass=Label(frm,text="Password",font=('arial',20,'bold'),bg='powder blue')
    lbl_pass.place(relx=.2,rely=.25)

    e_pass=Entry(frm,font=('arial',20,'bold'),bd=5,show='*')
    e_pass.place(relx=.4,rely=.25)

    btn_login=Button(frm,text="Login",font=('arial',20,'bold'),bd=5,command=login)
    btn_login.place(relx=.42,rely=.4)

    btn_clear=Button(frm,text="Reset",font=('arial',20,'bold'),bd=5,command=clear)
    btn_clear.place(relx=.52,rely=.4)

    btn_fp=Button(frm,command=forgotpass,width=16,text="Forgot password",font=('arial',20,'bold'),bd=5)
    btn_fp.place(relx=.4,rely=.55)

    btn_new=Button(frm,command=newuser,width=18,text="Open new account",font=('arial',20,'bold'),bd=5)
    btn_new.place(relx=.39,rely=.7)
    
    btn_ad=Button(frm,text="Super Admin",font=('arial',10,'bold'),bd=5,command=admin)
    btn_ad.place(relx=0.9,rely=.01)
    
def admin_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    def back():
        frm.destroy()
        main_screen()
        
    def clear():
        e_id.delete(0,"end")
        e_key.delete(0,"end")
        
    def login():
        id=e_id.get()
        key=e_key.get()
        if len(id)==0 or len(key)==0:
            messagebox.showerror("Error","Fill both field")
        elif id=="101" and key=="india":
            frm.destroy()
            admin_welcome_screen()
        else:
            messagebox.showerror("Error","Wrong Id/Key or Empty field")
        
    btn_back=Button(frm,text="Back",font=('arial',20,'bold'),bd=5,command=back)
    btn_back.place(relx=0,rely=0)
        
    lbl_id=Label(frm,text="ID number",font=('arial',20,'bold'),bg='powder blue')
    lbl_id.place(relx=.25,rely=.1)

    e_id=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_id.place(relx=.4,rely=.1)
    e_id.focus()

    lbl_key=Label(frm,text="Pass key",font=('arial',20,'bold'),bg='powder blue')
    lbl_key.place(relx=.25,rely=.2)

    e_key=Entry(frm,font=('arial',20,'bold'),bd=5,show='*')
    e_key.place(relx=.4,rely=.2)

    btn_login=Button(frm,text="Login",font=('arial',20,'bold'),bd=5,command=login)
    btn_login.place(relx=.42,rely=.3)

    btn_clear=Button(frm,text="Reset",font=('arial',20,'bold'),bd=5,command=clear)
    btn_clear.place(relx=.52,rely=.3)

def forgotpass_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)

    def back():
        frm.destroy()
        main_screen()

    def forgotpass_db():
        acn=e_acn.get()
        email=e_email.get()
        
        conobj=sqlite3.connect(database="bank.sqlite")
        curobj=conobj.cursor()
        curobj.execute("select acn_email,acn_pass from acn where acn_no=?",(acn,))
        row=curobj.fetchone()
        if(row==None):
            messagebox.showerror("Password Recovery","ACN does not exist or empty field")
        else:
            if(row[0]==email):
                otp=random.randint(1000,9999)
                try:
                    con=gmail.GMail("mohitg12rana@gmail.com","kgwi gfih nopy laog")
                    msg=gmail.Message(to=email,subject="OTP verification",text=f"You OTP is :{otp}")
                    con.send(msg)
                    messagebox.showinfo("Password Recovery","OTP sent, Check your email")
                except:
                    messagebox.showerror("Password Recovery","Connect to the internet")
                    return
                ifrm=Frame(frm)
                ifrm.configure(bg='powder blue')
                ifrm.place(relx=0,rely=.1,relwidth=1,relheight=.8)
                
                lbl_otp=Label(ifrm,text="Fill OTP",font=('arial',20,'bold'),bg='powder blue')
                lbl_otp.place(relx=.2,rely=.1)
    
                entry_otp=Entry(ifrm,font=('arial',20,'bold'),bd=5)
                entry_otp.place(relx=.4,rely=.1)
                entry_otp.focus()
                
                def getpass():
                    verify_otp=int(entry_otp.get())
                        
                    if otp==verify_otp:
                        messagebox.showinfo("Password Recovery",f"Your Pass:{row[1]}")
                        ifrm.destroy()
                        Frame(frm)
                        e_acn.delete(0,"end")
                        e_email.delete(0,"end")
                    
                    else:
                        messagebox.showerror("Password Recovery","Incorrect OTP")
                
                btn_summit=Button(ifrm,text="Summit",font=('arial',20,'bold'),bd=5,command=getpass)
                btn_summit.place(relx=.45,rely=.32)
                  
            else:
                messagebox.showerror("Password Recovery","Email is not correct or Empty feild")
        conobj.close()
        
    def clear():
        e_acn.delete(0,"end")
        e_email.delete(0,"end")
        
    btn_new=Button(frm,text="back",font=('arial',20,'bold'),bd=5,command=back)
    btn_new.place(relx=0,rely=0)

    lbl_acn=Label(frm,text="Account number",font=('arial',20,'bold'),bg='powder blue')
    lbl_acn.place(relx=.2,rely=.1)

    e_acn=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_acn.place(relx=.4,rely=.1)
    e_acn.focus()

    lbl_email=Label(frm,text="Email ID",font=('arial',20,'bold'),bg='powder blue')
    lbl_email.place(relx=.2,rely=.2)

    e_email=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_email.place(relx=.4,rely=.2)

    btn_sub=Button(frm,text="Verify email",font=('arial',20,'bold'),bd=5,command=forgotpass_db)
    btn_sub.place(relx=.40,rely=.35)
    
    btn_clr=Button(frm,text="Reset",font=('arial',20,'bold'),bd=5,command=clear)
    btn_clr.place(relx=.55,rely=.35)



def newuser_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)

    def back():
        frm.destroy()
        main_screen()

    def newuser_db():
        name=e_name.get()
        pwd=e_pass.get()
        email=e_email.get()
        mob=e_mob.get()
        gender=cb_gender.get()
        bal=0
        opendate=time.strftime("%d %B %Y,%A")
        typ=cb_type.get()
        
        match=re.fullmatch("^[A-Z][a-z]+(?: [A-Z][a-z]+)*$",name)
        if match==None:
            messagebox.showwarning("Name validation","Invalid format of Name (Frist letter should be Capital, Name should be more than three latters or Empty field)")
            return
        
        if len(pwd)<5:
            messagebox.showwarning("Password validation","Fill Password field or Password should be more than four characters.")
            return
        
        match=re.fullmatch("[a-zA-Z0-9_]+@[a-zA-Z]+\.[a-zA-Z]+",email)
        if match==None:
            messagebox.showwarning("Email validation","Invalid format of Email ID or Empty field")
            return
        
        match=re.fullmatch("[6-9][0-9]{9}",mob)
        if match==None:
            messagebox.showwarning("Mobile number validation","Invalid Mobile number or Empty field")
            return
        
        if gender !="Male" and gender !="Female" and gender !="Transgender":
            messagebox.showerror("Gender validation","Choose Gender in the list")
            return
        
        if typ !="Savings account" and typ!="Salary account" and typ!="Fixed deposit" and typ!="NRI account":
            messagebox.showerror("Account type validation","Choose Account type in the list")
            return           
        
        conobj=sqlite3.connect(database="bank.sqlite")
        curobj=conobj.cursor()
        curobj.execute("select acn_email from acn where acn_email=?",(email,))
        email_tup=curobj.fetchone()
        
        if email_tup!=None:
            messagebox.showerror("Email validation","Email already exists")
            return
        elif email_tup==None:
            otp=random.randint(1000,9999)
            try:
                con=gmail.GMail("mohitg12rana@gmail.com","kgwi gfih nopy laog")
                msg=gmail.Message(to=email,subject="OTP verification",text=f"You OTP is :{otp}")
                con.send(msg)
                messagebox.showinfo("Email","OTP sent, Check your email")
            except:
                messagebox.showerror("Email","Connect to the internet")
                return
            
            ifrm=Frame(frm)
            ifrm.configure(bg='powder blue')
            ifrm.place(relx=0,rely=.1,relwidth=1,relheight=.8)
                
            lbl_otp=Label(ifrm,text="Fill OTP",font=('arial',20,'bold'),bg='powder blue')
            lbl_otp.place(relx=.2,rely=.1)
    
            entry_otp=Entry(ifrm,font=('arial',20,'bold'),bd=5)
            entry_otp.place(relx=.4,rely=.1)
            entry_otp.focus()
                
            def getpass():
                verify_otp=int(entry_otp.get())
                        
                if otp==verify_otp:
                    conobj=sqlite3.connect(database="bank.sqlite")
                    curobj=conobj.cursor()
                    curobj.execute("insert into acn(acn_name,acn_pass,acn_email,acn_mob,acn_gender,acn_opendate,acn_bal,acn_type) values(?,?,?,?,?,?,?,?)",(name,pwd,email,mob,gender,opendate,bal,typ))
                    conobj.commit()
                    conobj.close()

                    conobj=sqlite3.connect(database="bank.sqlite")
                    curobj=conobj.cursor()
                    curobj.execute("select max(acn_no) from acn")
                    tup=curobj.fetchone()
                    conobj.close()
                    frm.destroy()
                    main_screen()
                    messagebox.showinfo("New User",f"Account Created with ACN No={tup[0]}")
     
                else:
                    messagebox.showerror("Password Recovery","Incorrect OTP")
                
            btn_summit=Button(ifrm,text="Summit",font=('arial',20,'bold'),bd=5,command=getpass)
            btn_summit.place(relx=.45,rely=.32)
                  
        else:
            messagebox.showerror("Password Recovery","Email is not correct or Empty feild")
        conobj.close()
        
        
    def clear():
        e_name.delete(0,"end")
        e_pass.delete(0,"end")
        e_email.delete(0,"end")
        e_mob.delete(0,"end")
        cb_gender.delete(0,"end")
        
        
    btn_new=Button(frm,text="back",font=('arial',20,'bold'),bd=5,command=back)
    btn_new.place(relx=0,rely=0)

    lbl_name=Label(frm,text="Name",font=('arial',20,'bold'),bg='powder blue')
    lbl_name.place(relx=.2,rely=.1)
    
    e_name=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_name.place(relx=.4,rely=.1)
    e_name.focus()

    lbl_pass=Label(frm,text="Password",font=('arial',20,'bold'),bg='powder blue')
    lbl_pass.place(relx=.2,rely=.2)
    
    e_pass=Entry(frm,font=('arial',20,'bold'),bd=5,show='*')
    e_pass.place(relx=.4,rely=.2)
    
    
    lbl_email=Label(frm,text="Email ID",font=('arial',20,'bold'),bg='powder blue')
    lbl_email.place(relx=.2,rely=.3)

    e_email=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_email.place(relx=.4,rely=.3)

    lbl_mob=Label(frm,text="Mobile",font=('arial',20,'bold'),bg='powder blue')
    lbl_mob.place(relx=.2,rely=.4)

    e_mob=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_mob.place(relx=.4,rely=.4)

    lbl_gender=Label(frm,text="Gender",font=('arial',20,'bold'),bg='powder blue')
    lbl_gender.place(relx=.2,rely=.5)

    cb_gender=Combobox(frm,values=['---select---','Male','Female','Transgender'],font=('arial',20,'bold'))
    cb_gender.place(relx=.4,rely=.5)

    lbl_type=Label(frm,text="Account type",font=('arial',20,'bold'),bg='powder blue')
    lbl_type.place(relx=.2,rely=.6)
    
    cb_type=Combobox(frm,values=['---select---','Savings account','Salary account','Fixed deposit','NRI account'],font=('arial',20,'bold'))
    cb_type.place(relx=.4,rely=.6)

    btn_sub=Button(frm,text="Verify",font=('arial',20,'bold'),bd=5,command=newuser_db)
    btn_sub.place(relx=.43,rely=.7)
    
    btn_clr=Button(frm,text="Reset",font=('arial',20,'bold'),bd=5,command=clear)
    btn_clr.place(relx=.53,rely=.7)
    
    
def admin_welcome_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)

    ifrm=Frame(frm,highlightbackground='black', highlightthickness=2)
    ifrm.configure(bg='white')
    ifrm.place(relx=.01,rely=.1,relwidth=.98,relheight=.89)
    
    def logout():
        frm.destroy()
        main_screen()
        
    def table_details():
        ifrm=Frame(frm,highlightbackground='black', highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.01,rely=.1,relwidth=.98,relheight=.89)
    
        tv=Treeview(ifrm)
        tv.place(x=0,y=0,height=560,width=1350)
        
        style = Style()
        style.configure("Treeview.Heading", font=('Arial',15,'bold'),fg='black')

        sb=Scrollbar(ifrm,orient='vertical',command=tv.yview)
        sb.place(relx=.99,rely=0,height=560)
        tv.configure(yscrollcommand=sb.set)

        tv['columns']=('col1','col2','col3','col4','col5','col6','col7','col8')

        tv.column('col1',width=150,anchor='c')
        tv.column('col2',width=150,anchor='c')
        tv.column('col3',width=150,anchor='c')
        tv.column('col4',width=150,anchor='c')
        tv.column('col5',width=150,anchor='c')
        tv.column('col6',width=150,anchor='c')
        tv.column('col7',width=150,anchor='c')
        tv.column('col8',width=150,anchor='c')
        

        tv.heading('col1',text='Account Number')
        tv.heading('col2',text='Name')
        tv.heading('col3',text='Password')
        tv.heading('col4',text='Email')
        tv.heading('col5',text='Phone number')
        tv.heading('col6',text='Balance')
        tv.heading('col7',text='Open date')
        tv.heading('col8',text='Gender')

        tv['show']='headings'
        
        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        curobj.execute("select * from acn")

        for row in curobj:
            tv.insert("","end",values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
            
    def table_delete():
        ifrm=Frame(frm,highlightbackground='black', highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.01,rely=.1,relwidth=.98,relheight=.89)
        
        lbl_contents=Label(ifrm,text="Enter account number which record you want to delete",font=('arial',20,'bold'),bg='white')
        lbl_contents.place(relx=.2,rely=.2)

        e_acc=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_acc.place(relx=.35,rely=.35)
        e_acc.focus()
        
        def confirmation():
            acn_id=e_acc.get()
            
            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select* from acn where acn_no=?",(acn_id,))
            tup=curobj.fetchone()
            conobj.close()
                
            if tup==None:
                messagebox.showerror("Error","Record not found")
                return
            else:
                ans=messagebox.askyesno("Confirmation","Are you sure, you want to delete record ?")
                if ans==1:
                    conobj=sqlite3.connect(database="bank.sqlite")
                    curobj=conobj.cursor()
                    curobj.execute("delete from acn where acn_no=?",(acn_id,))
                    conobj.commit()
                    conobj.close()
                    messagebox.showinfo("Delete","Record delete")
                    e_acc.delete(0,"end")
                else:
                    return
        
        btn_delete=Button(ifrm,text="Account delete",font=('arial',20,'bold'),bd=5,command=confirmation)
        btn_delete.place(relx=.38,rely=.5)
        
    btn_logout=Button(frm,text="logout",font=('arial',10,'bold'),bd=5,command=logout)
    btn_logout.place(relx=.95,rely=0)
    
    btn_table=Button(frm,text="Table details",font=('arial',20,'bold'),bd=5,command=table_details)
    btn_table.place(relx=0,rely=0)
    
    btn_delete=Button(frm,text="Account delete",font=('arial',20,'bold'),bd=5,command=table_delete)
    btn_delete.place(relx=.15,rely=0)

def welcome_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    ifrm=Frame(frm,highlightbackground='black', highlightthickness=2)
    ifrm.configure(bg='white')
    ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.7)
    
    conobj=sqlite3.connect(database="bank.sqlite")
    curobj=conobj.cursor()
    curobj.execute("select acn_name from acn where acn_no=?",(gacn,))
    name=curobj.fetchone()
    conobj.close()
    
    lbl_welcome=Label(ifrm,text=f"Welcome {name[0]}",font=('arial',20,'bold'),bg='white',fg='black')
    lbl_welcome.place(relx=.1,rely=.1)
    
    lbl_welcome=Label(ifrm,text="This project is for Banking purpose",font=('arial',20,'bold'),bg='white',fg='black')
    lbl_welcome.place(relx=.1,rely=.1)
    
    lbl_welcome=Label(ifrm,text="This project is for Admin and Super admin",font=('arial',20,'bold'),bg='white',fg='black')
    lbl_welcome.place(relx=.1,rely=.25)
    
    lbl_welcome=Label(ifrm,text="This project is created using Tkinter",font=('arial',20,'bold'),bg='white',fg='black')
    lbl_welcome.place(relx=.1,rely=.4)
    
    lbl_welcome=Label(ifrm,text="Tkinter is a Python binding to the Tk GUI toolkit",font=('arial',20,'bold'),bg='white',fg='black')
    lbl_welcome.place(relx=.1,rely=.55)
    
    lbl_welcome=Label(ifrm,text="In this project, I used Email configuration",font=('arial',20,'bold'),bg='white',fg='black')
    lbl_welcome.place(relx=.1,rely=.7)
    
    lbl_welcome=Label(ifrm,text="In future, I will add some more features like user photo",font=('arial',20,'bold'),bg='white',fg='black')
    lbl_welcome.place(relx=.1,rely=.85)

    def logout():
        frm.destroy()
        main_screen()

    def details():
        ifrm=Frame(frm,highlightbackground='black', highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.7)

        lbl_wel=Label(ifrm,text="This is Details Screen",font=('arial',20,'bold'),bg='white',fg='blue')
        lbl_wel.pack()

        conobj=sqlite3.connect(database="bank.sqlite")
        curobj=conobj.cursor()
        curobj.execute("select acn_opendate,acn_bal,acn_gender,acn_email,acn_mob,acn_type from acn where acn_no=?",(gacn,))
        tup=curobj.fetchone()
        conobj.close()
        
        lbl_opendate=Label(ifrm,text=f"Open Date:- {tup[0]}",font=('arial',15,'bold'),bg='white')
        lbl_opendate.place(relx=.2,rely=.12)

        lbl_bal=Label(ifrm,text=f"Balance:- {tup[1]}",font=('arial',15,'bold'),bg='white')
        lbl_bal.place(relx=.2,rely=.2)
        
        lbl_gender=Label(ifrm,text=f"Gender:- {tup[2]}",font=('arial',15,'bold'),bg='white')
        lbl_gender.place(relx=.2,rely=.28)

        lbl_email=Label(ifrm,text=f"Email:- {tup[3]}",font=('arial',15,'bold'),bg='white')
        lbl_email.place(relx=.2,rely=.36)

        lbl_mob=Label(ifrm,text=f"Mobile:- {tup[4]}",font=('arial',15,'bold'),bg='white')
        lbl_mob.place(relx=.2,rely=.44)
        
        lbl_mob=Label(ifrm,text=f"Account type:- {tup[5]}",font=('arial',15,'bold'),bg='white')
        lbl_mob.place(relx=.2,rely=.52)
        
    def update():
        ifrm=Frame(frm,highlightbackground='black', highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.7)

        conobj=sqlite3.connect(database="bank.sqlite")
        curobj=conobj.cursor()
        curobj.execute("select acn_name,acn_pass,acn_email,acn_mob from acn where acn_no=?",(gacn,))
        tup=curobj.fetchone()
        conobj.close()
        
        
        lbl_wel=Label(ifrm,text="This is Update Screen",font=('arial',20,'bold'),bg='white',fg='blue')
        lbl_wel.pack()

        lbl_name=Label(ifrm,text="Name",font=('arial',20,'bold'),bg='white')
        lbl_name.place(relx=.1,rely=.1)
    
        e_name=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_name.place(relx=.1,rely=.2)
        e_name.insert(0,tup[0])
    
        lbl_pass=Label(ifrm,text="Password",font=('arial',20,'bold'),bg='white')
        lbl_pass.place(relx=.1,rely=.4)
        
        e_pass=Entry(ifrm,font=('arial',20,'bold'),bd=5,show="*")
        e_pass.place(relx=.1,rely=.5)
        e_pass.insert(0,tup[1])
        
        lbl_email=Label(ifrm,text="Email ID",font=('arial',20,'bold'),bg='white')
        lbl_email.place(relx=.5,rely=.1)
    
        e_email=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_email.place(relx=.5,rely=.2)
        e_email.insert(0,tup[2])

        lbl_mob=Label(ifrm,text="Mobile",font=('arial',20,'bold'),bg='white')
        lbl_mob.place(relx=.5,rely=.4)
    
        e_mob=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_mob.place(relx=.5,rely=.5)
        e_mob.insert(0,tup[3])

        def update_db():
            name=e_name.get()
            pwd=e_pass.get()
            email=e_email.get()
            mob=e_mob.get()
            
            match=re.fullmatch("^[A-Z][a-z]+(?: [A-Z][a-z]+)*$",name)
            if match==None:
                messagebox.showwarning("Name validation","Invalid format of Name (Frist letter should be Capital, Name should be more than three latters or Empty field)")
                return
        
            if len(pwd)<5:
                messagebox.showwarning("Password validation","Fill Password field or Password should be more than four characters.")
                return
        
            match=re.fullmatch("[a-zA-Z0-9_]+@[a-zA-Z]+\.[a-zA-Z]+",email)
            if match==None:
                messagebox.showwarning("Email validation","Invalid format of Email ID or Empty field")
                return
        
            match=re.fullmatch("[6-9][0-9]{9}",mob)
            if match==None:
                messagebox.showwarning("Mobile number validation","Invalid Mobile number or Empty field")
                return
            
            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select acn_email from acn where acn_email=?",(email,))
            email_tup=curobj.fetchone()
        
            if email_tup!=None:
                messagebox.showerror("Email validation","Email already exists")
                return
            elif email_tup==None:
                otp=random.randint(1000,9999)
                try:
                    con=gmail.GMail("mohitg12rana@gmail.com","kgwi gfih nopy laog")
                    msg=gmail.Message(to=email,subject="OTP verification",text=f"You OTP is :{otp}")
                    con.send(msg)
                    messagebox.showinfo("Email","OTP sent, Check your email")
                except:
                    messagebox.showerror("Email","Connect to the internet")
                    return
            
                ifrm2=Frame(ifrm)
                ifrm2.configure(bg='powder blue')
                ifrm2.place(relx=.05,rely=.1,relwidth=.9,relheight=.8)
                
                lbl_otp=Label(ifrm2,text="Fill OTP",font=('arial',20,'bold'),bg='powder blue')
                lbl_otp.place(relx=.2,rely=.1)
    
                entry_otp=Entry(ifrm2,font=('arial',20,'bold'),bd=5)
                entry_otp.place(relx=.4,rely=.1)
                entry_otp.focus()
                
                def getpass():
                    verify_otp=int(entry_otp.get())
                        
                    if otp==verify_otp:
                        conobj=sqlite3.connect(database="bank.sqlite")
                        curobj=conobj.cursor()
                        curobj.execute("update acn set acn_name=?,acn_pass=?,acn_email=?,acn_mob=? where acn_no=?",(name,pwd,email,mob,gacn))
                        conobj.commit()
                        conobj.close()
                        messagebox.showinfo("Update","Record Updated")
                        welcome_screen()
     
                    else:
                        messagebox.showerror("Password Recovery","Incorrect OTP")
                
                btn_summit=Button(ifrm2,text="Summit",font=('arial',20,'bold'),bd=5,command=getpass)
                btn_summit.place(relx=.45,rely=.32)
                  
            else:
                messagebox.showerror("Password Recovery","Email is not correct or Empty feild")
            conobj.close()
        
            
        btn_Verify=Button(ifrm,text="Verify",font=('arial',20,'bold'),bd=5,command=update_db)
        btn_Verify.place(relx=.6,rely=.7)
        
    def deposit():
        ifrm=Frame(frm,highlightbackground='black', highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.7)

        lbl_wel=Label(ifrm,text="This is Deposit Screen",font=('arial',20,'bold'),bg='white',fg='blue')
        lbl_wel.pack()

        lbl_amt=Label(ifrm,text="Amount",font=('arial',20,'bold'),bg='white')
        lbl_amt.place(relx=.1,rely=.2)
    
        e_amt=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_amt.place(relx=.3,rely=.2)
        e_amt.focus()

        def deposit_db():
            amt=float(e_amt.get())
            
            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select acn_bal from acn where acn_no=?",(gacn,))
            bal=curobj.fetchone()[0]
            conobj.close()
            
            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("update acn set acn_bal=acn_bal+? where acn_no=?",(amt,gacn))
            curobj.execute("insert into txn values(?,?,?,?,?)",(gacn,amt,"Credit",time.ctime(),bal+amt))
            conobj.commit()
            conobj.close()
            messagebox.showinfo("Update",f"{amt} Amount Deposited")
            e_amt.delete(0,"end")
            
        def clear():
            e_amt.delete(0,"end")
        
        btn_sub=Button(ifrm,text="Submit",font=('arial',20,'bold'),bd=5,command=deposit_db)
        btn_sub.place(relx=.3,rely=.4)
        
        btn_clear=Button(ifrm,text="Reset",font=('arial',20,'bold'),bd=5,command=clear)
        btn_clear.place(relx=.5,rely=.4)

    def withdraw():
        ifrm=Frame(frm,highlightbackground='black', highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.7)

        lbl_wel=Label(ifrm,text="This is withdraw Screen",font=('arial',20,'bold'),bg='white',fg='blue')
        lbl_wel.pack()


        lbl_amt=Label(ifrm,text="Amount",font=('arial',20,'bold'),bg='white')
        lbl_amt.place(relx=.1,rely=.2)
    
        e_amt=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_amt.place(relx=.3,rely=.2)
        e_amt.focus()

        def withdraw_db():
            amt=float(e_amt.get())
            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select acn_bal from acn where acn_no=?",(gacn,))
            tup=curobj.fetchone()
            bal=tup[0]
            conobj.close()

            if bal>=amt:
                conobj=sqlite3.connect(database="bank.sqlite")
                curobj=conobj.cursor()
                curobj.execute("update acn set acn_bal=acn_bal-? where acn_no=?",(amt,gacn))
                curobj.execute("insert into txn values(?,?,?,?,?)",(gacn,amt,"Debit",time.ctime(),bal-amt))
                conobj.commit()
                conobj.close()
                messagebox.showinfo("Withdraw",f"{amt} Amount withdrawn")
                e_amt.delete(0,"end")
            else:
                messagebox.showwarning("Withdraw","Insufficient Bal")
                
        def clear():
            e_amt.delete(0,"end")
                
        btn_sub=Button(ifrm,text="Submit",font=('arial',20,'bold'),bd=5,command=withdraw_db)
        btn_sub.place(relx=.3,rely=.4)
        
        btn_clear=Button(ifrm,text="Reset",font=('arial',20,'bold'),bd=5,command=clear)
        btn_clear.place(relx=.5,rely=.4)
        
    def transfer():
        ifrm=Frame(frm,highlightbackground='black', highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.7)

        lbl_wel=Label(ifrm,text="This is Transfer Screen",font=('arial',20,'bold'),bg='white',fg='blue')
        lbl_wel.pack()

        lbl_amt=Label(ifrm,text="Amount",font=('arial',20,'bold'),bg='white')
        lbl_amt.place(relx=.1,rely=.2)
    
        e_amt=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_amt.place(relx=.3,rely=.2)
        e_amt.focus()

        lbl_to=Label(ifrm,text="To",font=('arial',20,'bold'),bg='white')
        lbl_to.place(relx=.1,rely=.4)
    
        e_to=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_to.place(relx=.3,rely=.4)

        def transfer_db():
            to_acn=e_to.get()
            amt=float(e_amt.get())

            if to_acn==gacn:
                messagebox.showwarning("Transfer","To and From can't be same")
                return
            
            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select acn_no,acn_bal from acn where acn_no=?",(to_acn,))
            tup=curobj.fetchone()
            conobj.close()

            if tup==None:
                messagebox.showwarning("Transfer","Invalid To ACN")
                return
            
            conobj=sqlite3.connect(database="bank.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select acn_bal from acn where acn_no=?",(gacn,))
            tup1=curobj.fetchone()
            avail_bal=tup1[0]
            conobj.close()
            
            if avail_bal>=amt:
                conobj=sqlite3.connect(database="bank.sqlite")
                curobj=conobj.cursor()
                curobj.execute("update acn set acn_bal=acn_bal+? where acn_no=?",(amt,to_acn))
                curobj.execute("update acn set acn_bal=acn_bal-? where acn_no=?",(amt,gacn))
                curobj.execute("insert into txn values(?,?,?,?,?)",(gacn,amt,"Transfer",time.ctime(),avail_bal-amt))
                curobj.execute("insert into txn values(?,?,?,?,?)",(to_acn,amt,"Credit through transfer",time.ctime(),tup[1]+amt))
                conobj.commit()
                conobj.close()
                messagebox.showinfo("Transfer",f"{amt} transered to ACN {to_acn}")
                e_to.delete(0,"end")
                e_amt.delete(0,"end")
            else:
                messagebox.showerror("Error","Insufficient amount")
                
                
        def clear():
            e_amt.delete(0,"end")
            e_to.delete(0,"end")
        
        btn_sub=Button(ifrm,text="Submit",font=('arial',20,'bold'),bd=5,command=transfer_db)
        btn_sub.place(relx=.3,rely=.6)
        
        btn_clr=Button(ifrm,text="Reset",font=('arial',20,'bold'),bd=5,command=clear)
        btn_clr.place(relx=.5,rely=.6)
        
    def delete():
        ifrm=Frame(frm,highlightbackground='black', highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.7)
        
        lbl=Label(ifrm,text="Are you sure, you want to delete account",font=('arial',20,'bold'),bg='white')
        lbl.place(relx=.2,rely=.1)
        
        
        def delete_db():
            if gacn=='1':
                messagebox.showerror("Error","Sorry this account number can not be deleted")
                return

            ans=messagebox.askyesno("Confirmation","Are you sure")
            if ans==1:
                conobj=sqlite3.connect(database="bank.sqlite")
                curobj=conobj.cursor()
                curobj.execute("delete from acn where acn_no=?",(gacn,))
                conobj.commit()
                conobj.close()
                frm.destroy()
                main_screen()
                messagebox.showinfo("Delete","Account delete")
            else:
                return
            
        btn_del=Button(ifrm,text="Delete",font=('arial',20,'bold'),bd=5,command=delete_db)
        btn_del.place(relx=.4,rely=.3)
        
    def history():
        ifrm=Frame(frm,highlightbackground='black', highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.1,relwidth=.7,relheight=.7)
        
        tv=Treeview(ifrm)
        tv.place(x=0,y=0,height=440,width=952)
        
        style = Style()
        style.configure("Treeview.Heading", font=('Arial',15,'bold'),foreground='black')

        sb=Scrollbar(ifrm,orient='vertical',command=tv.yview)
        sb.place(relx=.98,rely=0,height=439)
        tv.configure(yscrollcommand=sb.set)

        tv['columns']=('col1','col2','col3','col4')

        tv.column('col1',width=150,anchor='c')
        tv.column('col2',width=150,anchor='c')
        tv.column('col3',width=150,anchor='c')
        tv.column('col4',width=150,anchor='c')
        

        tv.heading('col1',text='Date')
        tv.heading('col2',text='Amount')
        tv.heading('col3',text='Transaction type')
        tv.heading('col4',text='Updated balance')

        tv['show']='headings'
        
        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        curobj.execute("select * from txn where acn=?",(gacn,))
        for row in curobj:
            tv.insert("","end",values=(row[3],row[1],row[2],row[4]))
        conobj.close()
        
    conobj=sqlite3.connect(database="bank.sqlite")
    curobj=conobj.cursor()
    curobj.execute("select acn_name from acn where acn_no=?",(gacn,))
    tup=curobj.fetchone()
    conobj.close()
    
    lbl_wel=Label(frm,text=f"Welcome,{tup[0]}",font=('arial',20,'bold'),bg='powder blue')
    lbl_wel.place(relx=0,rely=0)

    btn_logout=Button(frm,text="logout",font=('arial',20,'bold'),bd=5,command=logout)
    btn_logout.place(relx=.9,rely=0)

    btn_details=Button(frm,width=10,text="Details",font=('arial',20,'bold'),bd=5,command=details)
    btn_details.place(relx=0,rely=.1)

    btn_update=Button(frm,width=10,text="Update",font=('arial',20,'bold'),bd=5,command=update)
    btn_update.place(relx=0,rely=.2)

    btn_deposit=Button(frm,width=10,text="Deposit",font=('arial',20,'bold'),bd=5,command=deposit)
    btn_deposit.place(relx=0,rely=.3)

    btn_withdraw=Button(frm,width=10,text="Withdraw",font=('arial',20,'bold'),bd=5,command=withdraw)
    btn_withdraw.place(relx=0,rely=.4)

    btn_transfer=Button(frm,width=10,text="Transfer",font=('arial',20,'bold'),bd=5,command=transfer)
    btn_transfer.place(relx=0,rely=.5)
    
    btn_history=Button(frm,width=10,text="History",font=('arial',20,'bold'),bd=5,command=history)
    btn_history.place(relx=0,rely=.6)
    
    btn_delete=Button(frm,width=10,text="Delete",font=('arial',20,'bold'),bd=5,command=delete)
    btn_delete.place(relx=0,rely=.7)

main_screen()
win.mainloop()


# In[ ]:




