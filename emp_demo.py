from tkinter import *
from tkinter import font
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk, messagebox # to import droup down list or chombo box
import sqlite3


class EmployeeClass: #we are make class here
    def __init__(self,root):#this is defaule constructor. root is the object
        self.root = root#this define object of class using self(this is concept of oop's)
        self.root.geometry("1150x712+0+0")#it is used to define size of the frame or window
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
        self.var_salary=StringVar()
        
        self.canvas = Canvas(
            self.root,
            bg = "#ededed",
            height = 712,
            width = 1150,
            bd = 0,
             
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"images/employee/background.png")
        self.background = self.canvas.create_image(
            575.0, 366.5,
            image=self.background_img)

        self.img0 = PhotoImage(file = f"images/employee/img0.png")
        self.b0 = Button(
            image = self.img0,
            borderwidth = 0,
             
            # command = btn_clicked, 
            relief = "flat")

        self.b0.place(
            x = 775, y = 60,
            width = 100,
            height = 50)

        self.img1 = PhotoImage(file = f"images/employee/img1.png")
        self.b1 = Button(
            image = self.img1,
            borderwidth = 0,
             
            # command = btn_clicked,
            relief = "flat")

        self.b1.place(
            x = 1038, y = 439,
            width = 100,
            height = 40)

        self.img2 = PhotoImage(file = f"images/employee/img2.png")
        self.b2 = Button(
            image = self.img2,
            borderwidth = 0,
            # command = btn_clicked,
            relief = "flat")

        self.b2.place(
            x = 626, y = 439,
            width = 100,
            height = 40)

        self.img3 = PhotoImage(file = f"images/employee/img3.png")
        self.b3 = Button(
            image = self.img3,
            borderwidth = 0,
             
            # command = btn_clicked,
            relief = "flat")

        self.b3.place(
            x = 771, y = 439,
            width = 100,
            height = 40)

        self.img4 = PhotoImage(file = f"images/employee/img4.png")
        self.b4 = Button(
            image = self.img4,
            borderwidth = 0,
            # command = btn_clicked,
            relief = "flat")

        self.b4.place(
            x = 916, y = 439,
            width = 100,
            height = 40)

        self.canvas.create_text(
            1077.0, 74.0,
            text = "09:09:09",
            fill = "#ffffff",
            font = ("IstriaPosterBold", int(15)))

        self.canvas.create_text(
            951.0, 74.0,
            text = "21/09/2022",
            fill = "#ffffff",
            font = ("IstriaPosterBold", int(15)))

        self.entry0_img = PhotoImage(file = f"images/employee/img_textBox0.png")
        self.entry0_bg = self.canvas.create_image(
            645.5, 85,
            image = self.entry0_img)

        self.entry0 = Entry(
            bd = 0,
            # bg = "#ffffff",
             )

        self.entry0.place(
            x = 553.0, y = 65,
            width = 185.0,
            height = 40)

        self.entry1_img = PhotoImage(file = f"images/employee/img_textBox1.png")
        self.entry1_bg = self.canvas.create_image(
            283.5, 187.5,
            image = self.entry1_img)

        self.entry1 = Entry(
            bd = 0,
            bg = "#ffffff",
             )

        self.entry1.place(
            x = 191.0, y = 173,
            width = 185.0,
            height = 33)

        self.entry2_img = PhotoImage(file = f"images/employee/img_textBox2.png")
        self.entry2_bg = self.canvas.create_image(
            1022.5, 187.5,
            image = self.entry2_img)

        self.entry2 = Entry(
            bd = 0,
            bg = "#ffffff",
             )

        self.entry2.place(
            x = 930.0, y = 173,
            width = 185.0,
            height = 33)

        self.entry3_img = PhotoImage(file = f"images/employee/img_textBox3.png")
        self.entry3_bg = self.canvas.create_image(
            847.5, 405.5,
            image = self.entry3_img)

        self.entry3 = Entry(
            bd = 0,
            bg = "#ffffff",
             )

        self.entry3.place(
            x = 755.0, y = 391,
            width = 185.0,
            height = 33)

        self.entry4_img = PhotoImage(file = f"images/employee/img_textBox4.png")
        self.entry4_bg = self.canvas.create_image(
            283.5, 261.5,
            image = self.entry4_img)

        self.entry4 = Entry(
            bd = 0,
            bg = "#ffffff",
             )

        self.entry4.place(
            x = 191.0, y = 247,
            width = 185.0,
            height = 33)

        self.entry5_img = PhotoImage(file = f"images/employee/img_textBox5.png")
        self.entry5_bg = self.canvas.create_image(
            651.5, 261.5,
            image = self.entry5_img)

        self.entry5 = Entry(
            bd = 0,
            bg = "#ffffff",
             )

        self.entry5.place(
            x = 559.0, y = 247,
            width = 185.0,
            height = 33)

        self.entry6_img = PhotoImage(file = f"images/employee/img_textBox6.png")
        self.entry6_bg = self.canvas.create_image(
            1022.5, 261.5,
            image = self.entry6_img)

        self.entry6 = Entry(
            bd = 0,
            bg = "#ffffff",
             )

        self.entry6.place(
            x = 930.0, y = 247,
            width = 185.0,
            height = 33)

        self.entry7_img = PhotoImage(file = f"images/employee/img_textBox7.png")
        self.entry7_bg = self.canvas.create_image(
            283.5, 336.5,
            image = self.entry7_img)

        self.entry7 = Entry(
            bd = 0,
            bg = "#ffffff",
             )

        self.entry7.place(
            x = 191.0, y = 322,
            width = 185.0,
            height = 33)

        self.entry8_img = PhotoImage(file = f"images/employee/img_textBox8.png")
        self.entry8_bg = self.canvas.create_image(
            651.5, 336.5,
            image = self.entry8_img)

        self.entry8 = Entry(
            bd = 0,
            bg = "#ffffff",
             )

        self.entry8.place(
            x = 559.0, y = 322,
            width = 185.0,
            height = 33)

        self.entry9_img = PhotoImage(file = f"images/employee/img_textBox9.png")
        self.entry9_bg = self.canvas.create_image(
            383.5, 426.5,
            image = self.entry9_img)

        self.entry9 = Entry(
            bd = 0,
            bg = "#ffffff",
             )

        self.entry9.place(
            x = 191.0, y = 397,
            width = 385.0,
            height = 63)

        self.entry10_img = PhotoImage(file = f"images/employee/img_textBox10.png")
        self.entry10_bg = self.canvas.create_image(
            395.0, 85.0,
            image = self.entry10_img)

        self.entry10 = Entry(
            bd = 0,
            bg = "#fdc2c2",
             )

        self.entry10.place(
            x = 270, y = 63,
            width = 250,
            height = 48)

        self.entry11_img = PhotoImage(file = f"images/employee/img_textBox11.png")
        self.entry11_bg = self.canvas.create_image(
            652.5, 189.0,
            image = self.entry11_img)

        self.entry11 = Entry(
            bd = 0,
            bg = "#fdc2c2",
             )

        self.entry11.place(
            x = 553, y = 171,
            width = 199,
            height = 40)

        self.entry12_img = PhotoImage(file = f"images/employee/img_textBox12.png")
        self.entry12_bg = self.canvas.create_image(
            1023.5, 338.0,
            image = self.entry12_img)

        self.entry12 = Entry(
            bd = 0,
            bg = "#fdc2c2",
             )

        self.entry12.place(
            x = 924, y = 320,
            width = 199,
            height = 40)
        
        
        #====Employees Details ==========================
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=10,y=520,width=1130,height=190)
        
        scrolly=Scrollbar(emp_frame,orient=VERTICAL) 
        scrollx =Scrollbar(emp_frame,orient=HORIZONTAL)
        
        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("eid",text="Employee ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="Email")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="D.O.B")
        self.EmployeeTable.heading("doj",text="D.O.J")
        self.EmployeeTable.heading("pass",text="Password")
        self.EmployeeTable.heading("utype",text="User Type")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("salary",text="Salary")
        self.EmployeeTable["show"]="headings"

        self.EmployeeTable.column("eid",width=90)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email",width=200)
        self.EmployeeTable.column("gender",width=70)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("dob",width=70)
        self.EmployeeTable.column("doj",width=70)
        self.EmployeeTable.column("pass",width=100)
        self.EmployeeTable.column("utype",width=100)
        self.EmployeeTable.column("address",width=100)
        self.EmployeeTable.column("salary",width=100)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()
# ===================================================================================
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
            self.show()

    def show(self):
        con=sqlite3.connect(database=r'BMS.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
 
    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[9])
        self.var_salary.set(row[10])
#================================================================   
#====Update Funtion ==========================

    def update(self):
        con=sqlite3.connect(database=r'BMS.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="" or self.var_name.get()=="":
                messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
            else:
                cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    cur.execute("update employee set name=?, email=?, gender=?, contact=?, dob=?, doj=?, pass=?, utype=?, address=?, salary=? where eid=?",(
                    self.var_name.get(),self.var_email.get(),self.var_gender.get(),self.var_contact.get(),self.var_dob.get(),self.var_doj.get(),self.var_pass.get(),self.var_utype.get(),self.txt_address.get('1.0',END),self.var_salary.get(),self.var_emp_id.get()))
                    con.commit()
                    messagebox.showinfo("Success","Employee Updated successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        self.show()
        
#================================================================
#====Delete Funtion ==========================

    def delete(self):
        con=sqlite3.connect(database=r'BMS.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="" or self.var_name.get()=="":
                messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
            else:
                cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                     messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee Delete Successfully")
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        self.show()
        self.clear()
# ====================================================
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
        self.var_salary.set("")
        self.show()
        
        
 #================================================
 #====search Function =========================
        
           
    def search(self):
        con=sqlite3.connect(database=r'BMS.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select by option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
            rows=cur.fetchall()
            if len(rows)!=0:
                self.EmployeeTable.delete(* self.EmployeeTable.get_children())
                for row in rows:
                    self.EmployeeTable.insert('',END,values=row)
            else:
                 messagebox.showerror("Error","No Record Found!",parent=self.root)   
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
            
            
if __name__ == "__main__":
    root=Tk()#make root oject of tk class
    obj=EmployeeClass(root)#making obj  object of IMS class, passig   root to attache with tk class
    root.mainloop()#i  use this program to stay the self.root  otherwise it exit imidately 
    # this is the help of the python i can create this please help in deed 