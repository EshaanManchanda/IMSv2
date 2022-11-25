import os
from tkinter import *
from tkinter import font
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk, messagebox # to import droup down list or chombo box
import sqlite3


class userAdmin: #we are make class here
    def __init__(self,root):#this is defaule constructor. root is the object
        self.root = root#this define object of class using self(this is concept of oop's)
        self.root.geometry("1100x500+210+140")#it is used to define size of the frame or window
        self.root.title("Employees")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #====================================================
        #All Variables =============================
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_salary="N/A"
        #====Title =====
        title=Label(self.root,text="Admin Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=50,width=1000)
                
        #====Content===========================
        #====Row 1 =================================
        lbl_empid=Label(self.root,text="Emp ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gemder",font=("goudy old style",15),bg="white").place(x=350,y=150)
        lbl_contact=Label(self.root,text="Contace",font=("goudy old style",15),bg="white").place(x=750,y=150)
                
                
        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)
                
                
        cmd_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),font=("goudy old style",15),state='readonly',justify=CENTER)
        cmd_gender.place(x=500,y=150,width=180)
        cmd_gender.current(0)
                
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)
                
        #====Row 2================================
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15),bg="white").place(x=350,y=190)
        lbl_doj=Label(self.root,text="D.O.J",font=("goudy old style",15),bg="white").place(x=750,y=190)
                
                
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)
                
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15),bg="lightyellow").place(x=500,y=190,width=180)
                
                
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)
                
        #====Row 3 ==============================
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=50,y=230)
        lbl_pass=Label(self.root,text="Password",font=("goudy old style",15),bg="white").place(x=350,y=230)
        lbl_utype=Label(self.root,text="User Type",font=("goudy old style",15),bg="white").place(x=750,y=230)
                
                
        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=180)
                
        txt_pass=Entry(self.root,textvariable=self.var_pass,font=("goudy old style",15),bg="lightyellow").place(x=500,y=230,width=180)
                
                
        cmd_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Admin","Employee"),font=("goudy old style",15),state=DISABLED,justify=CENTER)
        cmd_utype.place(x=850,y=230,width=180)
        cmd_utype.current(0)
                
        #====Row 4 ==============================
        lbl_address=Label(self.root,text="Address",font=("goudy old style",15),bg="white").place(x=50,y=270)
        lbl_salary=Label(self.root,text="Salary",font=("goudy old style",15),bg="white").place(x=500,y=270)
                
                
        self.txt_address=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_address.place(x=150,y=270,width=300, height=60)
        txt_salary=Entry(self.root,text="N/A",state=DISABLED,font=("goudy old style",15),bg="lightyellow").place(x=600,y=270,width=180)
                
        #====Buttons =================================
                
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),cursor="hand2",bg="#2196f3",fg="white").place(x=200,y=400,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),cursor="hand2",bg="#607d8b",fg="white").place(x=500,y=400,width=110,height=28)
        btn_exit=Button(self.root,text="Exit",command=self.exit_,font=("goudy old style",15),cursor="hand2",bg="#607d8b",fg="white").place(x=800,y=400,width=110,height=28)          
                
    #====add function ==========================
    def add(self):
        con=sqlite3.connect(database=r'BMS.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="" or self.var_name.get()=="":
                messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
            else:
                cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee ID already assigned , try different one",parent=self.root)
                else:
                    cur.execute("Insert into employee(eid , name , email , gender , contact , dob , doj , pass , utype , address , salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_emp_id.get(),self.var_name.get(),self.var_email.get(),self.var_gender.get(),self.var_contact.get(),self.var_dob.get(),self.var_doj.get(),self.var_pass.get(),self.var_utype.get(),self.txt_address.get('1.0',END),self.var_salary.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Added successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
            
    def exit_(self):
            self.root.destroy()
            os.system("python login.py")
#====clear Function ==========================

    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.txt_address.delete('1.0',END)
        
        
if __name__ == "__main__":
    root=Tk()#make root oject of tk class
    obj=userAdmin(root)#making obj  object of IMS class, passig   root to attache with tk class
    root.mainloop()