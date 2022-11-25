import sqlite3
from tkinter import *
from tkinter import font
from tkinter import messagebox
from PIL import Image,ImageTk #pip install pillow
from employeev2 import EmployeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
import time,os

class IMS: #we are make class hereself.
    def __init__(self,root):#this is defaule constructor. root is the object
        self.root = root#this define object of class using self(this is concept of oop's)
        self.root.geometry("1350x712+0+0")#it is used to define size of the frame or window
        self.root.title("Inventory Management System | Developed by Tech Love V")
        self.root.config(bg="white")
        self.canvas = Canvas(
            self.root,
            bg = "#ededed",
            height = 712,
            width = 1350,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"images/dashboard/background.png")
        self.background = self.canvas.create_image(
            675.0, 356.0,
            image=self.background_img)

        self.img0 = PhotoImage(file = f"images/dashboard/img0.png")
        self.b0 = Button(
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.employee,
            relief = "flat")

        self.b0.place(
            x = 48, y = 461,
            width = 137,
            height = 50)

        self.img1 = PhotoImage(file = f"images/dashboard/img1.png")
        self.b1 = Button(
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.category,
            relief = "flat")

        self.b1.place(
            x = 48, y = 405,
            width = 137,
            height = 50)

        self.img2 = PhotoImage(file = f"images/dashboard/img2.png")
        self.b2 = Button(
            image = self.img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.product,
            relief = "flat")

        self.b2.place(
            x = 50, y = 355,
            width = 137,
            height = 50)

        self.img3 = PhotoImage(file = f"images/dashboard/img3.png")
        self.b3 = Button(
            image = self.img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.supplier,
            relief = "flat")

        self.b3.place(
            x = 50, y = 293,
            width = 137,
            height = 50)

        self.img4 = PhotoImage(file = f"images/dashboard/img4.png")
        self.b4 = Button(
            image = self.img4,
            borderwidth = 0,
            highlightthickness = 0,
            # command = btn_clicked,
            relief = "flat")

        self.b4.place(
            x = 48, y = 238,
            width = 137,
            height = 50)

        self.img5 = PhotoImage(file = f"images/dashboard/img5.png")
        self.b5 = Button(
            image = self.img5,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.logout,
            relief = "flat")

        self.b5.place(
            x = 49, y = 615,
            width = 101,
            height = 42)
        self.trend1=self.canvas.create_text(
            341.0, 403.0,
            text = "name 1",
            fill = "#27bff1",
            font = ("IstriaPosterBold", int(20.0)))

        self.trend2=self.canvas.create_text(
            341.0, 437.0,
            text = "name 2",
            fill = "#27bff1",
            font = ("IstriaPosterBold", int(20.0)))

        self.trend3=self.canvas.create_text(
            340.0, 471.0,
            text = "name 3",
            fill = "#27bff1",
            font = ("IstriaPosterBold", int(20.0)))

        self.trend4=self.canvas.create_text(
            341.0, 504.0,
            text = "name 4",
            fill = "#27bff1",
            font = ("IstriaPosterBold", int(20.0)))

        self.trend5=self.canvas.create_text(
            340.0, 538.0,
            text = "name 5",
            fill = "#27bff1",
            font = ("IstriaPosterBold", int(20.0)))
        
        self.get_data_base()
        self.canvas.create_text(
            99.5, 190.5,
            text = f"{str(self.username[0])}",
            fill = "#3856C0",
            font = ("ArialBlack", int(10.0),"bold"))

        self.date_=self.canvas.create_text(
            1115.5, 88.0,
            text = "21/09/2022",
            fill = "#ffffff",
            font = ("IstriaBold", int(20.0)))

        self.time_=self.canvas.create_text(
            1279.0, 92.0,
            text = "09:09 PM",
            fill = "#ffffff",
            font = ("IstriaBold", int(20.0)))
        
        
        self.reproduct=self.canvas.create_text(
            629.5, 212.0,
            text = "0",
            fill = "#27bff1",
            font = ("IstriaPosterBold", int(20.0)))

        self.total_product=self.canvas.create_text(
            629.5, 398.0,
            text = "5",
            fill = "#27bff1",
            font = ("IstriaPosterBold", int(20.0)))

        self.total_supplier=self.canvas.create_text(
            629.5, 592.0,
            text = "1",
            fill = "#27bff1",
            font = ("IstriaPosterBold", int(20.0)))

        self.m_ts=self.canvas.create_text(
            917.5, 592.0,
            text = "1000",
            fill = "#27bff1",
            font = ("IstriaPosterBold", int(20.0)))

        self.total_category=self.canvas.create_text(
            918.5, 397.0,
            text = "2",
            fill = "#27bff1",
            font = ("IstriaPosterBold", int(20.0)))

        self.total_employee=self.canvas.create_text(
            919.5, 212.0,
            text = "10",
            fill = "#27bff1",
            font = ("IstriaPosterBold", int(20.0)))
        self.canvas.create_text(
            1203.0, 333.5,
            text = f"{str(self.username[0])}",
            fill = "#ffffff",
            font = ("IstriaPosterBold", int(15)))

        self.canvas.create_text(
            1199.0, 253.5,
            text = f"{str(self.username[1])}",
            fill = "#ffffff",
            font = ("IstriaPosterBold", int(15)))

        self.canvas.create_text(
            1195.0, 413.5,
            text = f"{str(self.username[3])}",
            fill = "#ffffff",
            font = ("IstriaPosterBold", int(15)))

        self.canvas.create_text(
            1203.0, 493.5,
            text = f"{str(self.username[2])}",
            fill = "#ffffff",
            font = ("IstriaPosterBold", int(15)))

        self.update_content()
        self.total_s=self.canvas.create_text(
            339.5, 212.0,
            text = "1540",
            fill = "#e3343e",
            font = ("IstriaPosterBold", int(20.0)))
        self.get_totalsales()
        self.m_total_sales()
        
        
        
       
        
#=======================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        print(self.new_win)
        self.new_obj=EmployeeClass(self.new_win)
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)
    def logout(self):
        self.root.destroy()
        os.system("python loginv2.py")
    
    def get_data_base(self):
        con=sqlite3.connect(database=r'BMS.db')
        cur=con.cursor()
        self.pname_list=[]
        try:
            cur.execute("select name,eid,email,contact,loginDate,loginTime from employee where utype='Admin' ORDER BY loginDate DESC,loginTime DESC",())
            self.username=cur.fetchone()
            
            cur.execute("select name from product ORDER BY sales DESC ",())
            pname=cur.fetchall()
            for i in range(5):
                self.pname_list.append(pname[i][0])
            
            self.canvas.itemconfig(self.trend1,text=f"{str(self.pname_list[0])}")
            self.canvas.itemconfig(self.trend2,text=f"{str(self.pname_list[1])}")
            self.canvas.itemconfig(self.trend3,text=f"{str(self.pname_list[2])}")
            self.canvas.itemconfig(self.trend4,text=f"{str(self.pname_list[3])}")
            self.canvas.itemconfig(self.trend5,text=f"{str(self.pname_list[4])}")
            # print(self.pname_list)
            
            
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    
    def m_total_sales(self):
        con=sqlite3.connect(database=r'BMS.db')
        cur=con.cursor()
        try:
            month_t=time.strftime("%m")
            # print(month_t)
            cur.execute(f"select price from customer where date like '%{int(month_t)}%';")
            tsales=cur.fetchall()
            # print(tsales)
            M_total_sale=0.0
            for i in tsales:
                k=i[0]
                M_total_sale=M_total_sale+float(k)
            # print(M_total_sale)
            self.canvas.itemconfig(self.m_ts,text=f"{str(M_total_sale)}")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    def get_totalsales(self):
        con=sqlite3.connect(database=r'BMS.db')
        cur=con.cursor()
        try:
            cur.execute("select price from customer where date=?",(self.dateFetch,))
            sales=cur.fetchall()
            # print(sales)
            total_sale=0.0
            for i in sales:
                k=i[0]
                # print(k)
                total_sale=total_sale+float(k)
            # print(total_sale)
            self.canvas.itemconfig(self.total_s,text=f"{str(total_sale)}")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    def update_content(self):
        con=sqlite3.connect(database=r'BMS.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.canvas.itemconfig(self.total_product,text=f"{str(len(product))}")
            
            
            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.canvas.itemconfig(self.total_supplier,text=f"{str(len(supplier))}")
            
            
            cur.execute("select * from category")
            category=cur.fetchall()
            self.canvas.itemconfig(self.total_category,text=f"{str(len(category))}")
            
            
            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.canvas.itemconfig(self.total_employee,text=f"{str(len(employee))}")
            
            cur.execute("select * from product where qty<=1")
            ReProducr=cur.fetchall()
            self.canvas.itemconfig(self.reproduct,text=f"{str(len(ReProducr))}")
            
            
            # self.lbl_sales.config(text=f"Total Sales\n{str(len(os.listdir('bill')))}")
            
            time_=time.strftime("%I:%M:%S")
            self.dateFetch=time.strftime("%d-%m-%Y")
            self.canvas.itemconfig(self.date_,text=f"{str(self.dateFetch)}")
            self.canvas.itemconfig(self.time_,text=f"{str(time_)}")
            self.canvas.after(200,self.update_content)
            
            
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        
if __name__ == "__main__":
    root=Tk()#make root oject of tk class
    obj=IMS(root)#making obj  object of IMS class, passig   root to attache with tk class
    root.mainloop()#i  use this program to stay the window  otherwise it exit imidately 