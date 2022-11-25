from tkinter import *
from tkinter import ttk,messagebox
import sqlite3,time,os,tempfile
# from barcode import EAN13


class billClass: 
    def __init__(self,root): #this is defaule constructor. root is the object
        self.root = root #this define object of class using self(this is concept of oop's)
        self.root.geometry("1350x712+0+0") #it is used to define size of the frame or window
        self.root.title("Inventory Management System | Developed by Tech Love V")
        self.root.config(bg="#FFFFFF")
        self.cart_list = [] 
        self.chk_print=0
        self.canvas = Canvas( 
            self.root,
            bg = "#FFFFFF",
            height = 712,
            width = 1350,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"images/billing/background.png")
        background = self.canvas.create_image(
            675.0, 360.0,
            image=self.background_img)

        self.canvas.create_text(
            125, 29.5,
            text = "Employee",
            fill = "#ffffff",
            font = ("IstriaPosterBold", int(32.0)))

        self.img0 = PhotoImage(file = f"images/billing/img0.png")
        self.b0 = Button(
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.logout,cursor="hand2",
            relief = "flat")

        self.b0.place(
            x = 1196, y = 11,
            width = 140,
            height = 40)

        self.img1 = PhotoImage(file = f"images/billing/img1.png")
        self.b1 = Button(
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.show,cursor="hand2",
            relief = "flat")

        self.b1.place(
            x = 271, y = 159,
            width = 118,
            height = 26)

        self.img2 = PhotoImage(file = f"images/billing/img2.png")
        self.b2 = Button(
            image = self.img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.add_update,cursor="hand2",
            relief = "flat")

        self.b2.place(
            x = 694, y = 566,
            width = 154,
            height = 27)

        self.img3 = PhotoImage(file = f"images/billing/img3.png")
        self.b3 = Button(
            image = self.img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.search,cursor="hand2",
            relief = "flat")

        self.b3.place(
            x = 186, y = 159,
            width = 78,
            height = 25)

        self.img4 = PhotoImage(file = f"images/billing/img4.png")
        self.b4 = Button(
            image = self.img4,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.clear_cart,cursor="hand2",
            relief = "flat")

        self.b4.place(
            x = 732, y = 612,
            width = 78,
            height = 25)

        self.entry0_img = PhotoImage(file = f"images/billing/img_textBox0.png")
        self.entry0_bg = self.canvas.create_image(
            550.0, 143.5,
            image = self.entry0_img)
        #================Customer================================================
        #===========================================================
        
        cartFrame=Frame(self.canvas,bd=3,relief=RIDGE)
        cartFrame.place(x=655,y=215,width=228,height=300)
        
        
        scrolly=Scrollbar(cartFrame,orient=VERTICAL) 
        scrollx =Scrollbar(cartFrame,orient=HORIZONTAL)
        
        self.cartTable=ttk.Treeview(cartFrame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.cartTable.xview)
        scrolly.config(command=self.cartTable.yview)
        self.cartTable.heading("pid",text="P ID")
        self.cartTable.heading("name",text="Name")
        self.cartTable.heading("price",text="Price")
        self.cartTable.heading("qty",text="QTY")
        self.cartTable["show"]="headings"

        self.cartTable.column("pid",width=40)
        self.cartTable.column("name",width=90)
        self.cartTable.column("price",width=70)
        self.cartTable.column("qty",width=40)
        self.cartTable.pack(fill=BOTH,expand=1)
        self.cartTable.bind("<ButtonRelease-1>",self.get_data_cart)
        #=========== ADD cart Widgets Frame ================================================
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        self.entry0 = Entry(
            bd = 0,
            bg = "#ffffff",
            textvariable=self.var_cname,
            highlightthickness = 0)

        self.entry0.place(
            x = 475.0, y = 131,
            width = 150.0,
            height = 23)

        self.entry1_img = PhotoImage(file = f"images/billing/img_textBox1.png")
        self.entry1_bg = self.canvas.create_image(
            802.0, 143.5,
            image = self.entry1_img)
        self.entry1 = Entry(
            bd = 0,
            bg = "#ffffff",
            textvariable=self.var_contact,
            highlightthickness = 0)

        self.entry1.place(
            x = 727.0, y = 131,
            width = 150.0,
            height = 23)
        #====================================Prouct=========================================
        self.entry2_img = PhotoImage(file = f"images/billing/img_textBox2.png")
        self.entry2_bg = self.canvas.create_image(
            99.0, 171.5,
            image = self.entry2_img)
        self.var_search=StringVar()
        self.entry2 = Entry(
            bd = 0,
            bg = "#ffffff",
            textvariable=self.var_search,
            highlightthickness = 0)

        self.entry2.place(
            x = 24.0, y = 159,
            width = 150.0,
            height = 23)
        #===================================== product Table==================================
        ProductFrame3=Frame(self.canvas,bd=3,relief=RIDGE)
        ProductFrame3.place(x=20,y=200,width=365,height=450)
        
        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL) 
        scrollx =Scrollbar(ProductFrame3,orient=HORIZONTAL)
        
        self.product_table=ttk.Treeview(ProductFrame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)
        self.product_table.heading("pid",text="P ID")
        self.product_table.heading("name",text="Name")
        self.product_table.heading("price",text="Price")
        self.product_table.heading("qty",text="QTY")
        self.product_table.heading("status",text="Status")
        self.product_table["show"]="headings"

        self.product_table.column("pid",width=40)
        self.product_table.column("name",width=100)
        self.product_table.column("price",width=60)
        self.product_table.column("qty",width=40)
        self.product_table.column("status",width=90)
        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)
        
        #====================================================================================
        self.entry3_img = PhotoImage(file = f"images/billing/img_textBox3.png")
        self.entry3_bg = self.canvas.create_image(
            599.0, 539.5,
            image = self.entry3_img)
        self.entry3 = Entry(
            bd = 0,
            bg = "#ffffff",
            textvariable=self.var_pname,
            highlightthickness = 0)

        self.entry3.place(
            x = 524.0, y = 527,
            width = 150.0,
            height = 23)

        self.entry4_img = PhotoImage(file = f"images/billing/img_textBox4.png")
        self.entry4_bg = self.canvas.create_image(
            599.0, 580.5,
            image = self.entry4_img)
        self.var_price=StringVar()
        self.entry4 = Entry(
            bd = 0,
            bg = "#ffffff",
            textvariable=self.var_price,
            highlightthickness = 0)

        self.entry4.place(
            x = 524.0, y = 568,
            width = 150.0,
            height = 23)

        self.entry5_img = PhotoImage(file = f"images/billing/img_textBox5.png")
        self.entry5_bg = self.canvas.create_image(
            596.0, 624.5,
            image = self.entry5_img)
        self.var_qty=StringVar()
        self.entry5 = Entry(
            bd = 0,
            bg = "#ffffff",
            textvariable=self.var_qty,
            highlightthickness = 0)

        self.entry5.place(
            x = 521.0, y = 612,
            width = 150.0,
            height = 23)

        self.entry6_img = PhotoImage(file = f"images/billing/img_textBox6.png")
        self.entry6_bg = self.canvas.create_image(
            533.0, 222.0,
            image = self.entry6_img)
        #=================================Calculator input===================================================
        self.var_cal_input=StringVar()
        self.entry6 = Entry(
            bd = 0,
            bg = "#fbfbfb",
            textvariable=self.var_cal_input,
            highlightthickness = 0)
        #========================================================================
        #================Billing Area================
        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billFrame.place(x=920,y=130,width=410,height=350)
        # bTitle=Label(billFrame,text="Customer Bill Area",font=("goudy old style",20,"bold"),bg="#f44336",fg="white").pack(side=TOP,fill=X)
        
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.text_bill_area=Text(billFrame,font=("goudy old style",11),yscrollcommand=scrolly.set)
        self.text_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.text_bill_area.yview)
        #=========================================================
        self.entry6.place(
            x = 422, y = 196,
            width = 222,
            height = 50)
        #cal7
        self.img5 = PhotoImage(file = f"images/billing/img5.png")
        self.b5 = Button(
            image = self.img5,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda:self.get_input(7),
            relief = "flat")

        self.b5.place(
            x = 422, y = 257,
            width = 48,
            height = 46)

        self.img6 = PhotoImage(file = f"images/billing/img6.png")
        self.b6 = Button(
            image = self.img6,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda:self.get_input(8),
            relief = "flat")

        self.b6.place(
            x = 480, y = 257,
            width = 48,
            height = 46)

        self.img7 = PhotoImage(file = f"images/billing/img7.png")
        self.b7 = Button(
            image = self.img7,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda:self.get_input(5),
            relief = "flat")

        self.b7.place(
            x = 480, y = 322,
            width = 49,
            height = 46)

        self.img8 = PhotoImage(file = f"images/billing/img8.png")
        self.b8 = Button(
            image = self.img8,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda:self.get_input(2),
            relief = "flat")

        self.b8.place(
            x = 480, y = 387,
            width = 49,
            height = 46)

        self.img9 = PhotoImage(file = f"images/billing/img9.png")
        self.b9 = Button(
            image = self.img9,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.clear_cal,
            relief = "flat")

        self.b9.place(
            x = 480, y = 451,
            width = 49,
            height = 46)

        self.img10 = PhotoImage(file = f"images/billing/img10.png")
        self.b10 = Button(
            image = self.img10,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda:self.get_input(9),
            relief = "flat")

        self.b10.place(
            x = 538, y = 258,
            width = 49,
            height = 46)

        self.img11 = PhotoImage(file = f"images/billing/img11.png")
        self.b11 = Button(
            image = self.img11,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda:self.get_input(6),
            relief = "flat")

        self.b11.place(
            x = 538, y = 322,
            width = 49,
            height = 46)

        self.img12 = PhotoImage(file = f"images/billing/img12.png")
        self.b12 = Button(
            image = self.img12,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda:self.get_input(3),
            relief = "flat")

        self.b12.place(
            x = 538, y = 387,
            width = 49,
            height = 46)

        self.img13 = PhotoImage(file = f"images/billing/img13.png")
        self.b13 = Button(
            image = self.img13,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.perform_cal,
            relief = "flat")

        self.b13.place(
            x = 538, y = 451,
            width = 49,
            height = 46)

        self.img14 = PhotoImage(file = f"images/billing/img14.png")
        self.b14 = Button(
            image = self.img14,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda:self.get_input("-"),
            relief = "flat")

        self.b14.place(
            x = 595, y = 258,
            width = 49,
            height = 46)

        self.img15 = PhotoImage(file = f"images/billing/img15.png")
        self.b15 = Button(
            image = self.img15,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda:self.get_input("+"),
            relief = "flat")

        self.b15.place(
            x = 595, y = 322,
            width = 49,
            height = 46)

        self.img16 = PhotoImage(file = f"images/billing/img16.png")
        self.b16 = Button(
            image = self.img16,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda:self.get_input("/"),
            relief = "flat")

        self.b16.place(
            x = 595, y = 387,
            width = 49,
            height = 46)

        self.img17 = PhotoImage(file = f"images/billing/img17.png")
        self.b17 = Button(
            image = self.img17,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda:self.get_input(4),
            relief = "flat")

        self.b17.place(
            x = 423, y = 322,
            width = 49,
            height = 46)

        self.img18 = PhotoImage(file = f"images/billing/img18.png")
        self.b18 = Button(
            image = self.img18,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda:self.get_input(1),
            relief = "flat")

        self.b18.place(
            x = 423, y = 387,
            width = 49,
            height = 46)

        self.img19 = PhotoImage(file = f"images/billing/img19.png")
        self.b19 = Button(
            image = self.img19,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda:self.get_input(0),
            relief = "flat")

        self.b19.place(
            x = 423, y = 451,
            width = 49,
            height = 46)

        self.img20 = PhotoImage(file = f"images/billing/img20.png")
        self.b20 = Button(
            image = self.img20,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda:self.get_input("*"),
            relief = "flat")

        self.b20.place(
            x = 596, y = 451,
            width = 49,
            height = 46)

        self.total_product=self.canvas.create_text(
            862.0, 202.0,
            text = "0",
            fill = "#ffffff",
            font = ("IstriaPosterBold", int(15.0)))

        self.instock=self.canvas.create_text(
            809.5, 539.5,
            text = "0",
            fill = "#000000",
            font = ("IstriaPosterBold", int(14.0)))

        self.billamt=self.canvas.create_text(
            972.0, 552.0,
            text = "0",
            fill = "#ffffff",
            font = ("IstriaPosterBold", int(16.0)))

        self.canvas.create_text(
            1121.5, 559.5,
            text = "5%",
            fill = "#ffffff",
            font = ("IstriaPosterBold", int(16.0)))

        self.netpay=self.canvas.create_text(
            1269.0, 557.0,
            text = "0",
            fill = "#ffffff",
            font = ("IstriaPosterBold", int(16.0)))

        self.img21 = PhotoImage(file = f"images/billing/img21.png")
        self.b21 = Button(
            image = self.img21,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.print_bill,cursor="hand2",
            relief = "flat")

        self.b21.place(
            x = 913, y = 597,
            width = 102,
            height = 51)

        self.img22 = PhotoImage(file = f"images/billing/img22.png")
        self.b22 = Button(
            image = self.img22,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.clear_all,cursor="hand2",
            relief = "flat")

        self.b22.place(
            x = 1037, y = 598,
            width = 112,
            height = 50)

        self.img23 = PhotoImage(file = f"images/billing/img23.png")
        self.b23 = Button(
            image = self.img23,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.generate_bill,cursor="hand2",
            relief = "flat")

        self.b23.place(
            x = 1165, y = 596,
            width = 166,
            height = 51)

        self.date_show=self.canvas.create_text(
            967.0, 691.5,
            text = "21/09/2002",
            fill = "#ffffff",
            font = ("IstriaPosterBold", int(15)))

        self.time_show=self.canvas.create_text(
            1281.5, 691.5,
            text = "11:40:30",
            fill = "#ffffff",
            font = ("IstriaPosterBold", int(15)))
        self.show()
        # self.bill_top()
        self.update_date_time()
        
#=================================All funtions =================================================
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set("")
    
    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))
        
    #=======================================
    
    def show(self):
        con=sqlite3.connect(database=r'BMS.db')
        cur=con.cursor()
        try:
            cur.execute("select pid,name,price,qty,status from product where status='Active'")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        
    #====search Function =========================
        
           
    def search(self):
        con=sqlite3.connect(database=r'BMS.db')
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("select  pid,name,price,qty,status from product where name LIKE '%"+self.var_search.get()+"%' and status='Active'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_table.delete(* self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('',END,values=row)
                else:
                     messagebox.showerror("Error","No Record Found!",parent=self.root)   
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        
        
    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        self.var_pid.set(row[0]),
        self.var_pname.set(row[1]),
        self.var_price.set(row[2]),
        # self.lbl_instock.config(text=f"In Stock [{str(row[3])}]")
        self.canvas.itemconfig(self.instock,text=f"{str(row[3])}")
        self.var_stock.set(row[3])
        self.var_qty.set('1')
        
        
    def get_data_cart(self,ev):
        f=self.cartTable.focus()
        content=(self.cartTable.item(f))
        row=content['values']
        self.var_pid.set(row[0]),
        self.var_pname.set(row[1]),
        self.var_price.set(row[2]),
        self.var_qty.set(row[3])
        self.canvas.itemconfig(self.instock,text=f"{str(row[4])}")
        self.var_stock.set(row[4])
       
       
    def add_update(self):
        con=sqlite3.connect(database=r'BMS.db')
        cur=con.cursor()
        if self.var_pid.get()=="":
            messagebox.showerror("Error","Please select product from the list!",parent=self.root)
            
        elif self.var_qty.get()=="":
            messagebox.showerror("Error","Quantity is Required!",parent=self.root)
        elif int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror("Error","Invalid Quantity!",parent=self.root)
        else:
            # price_cal=int(self.var_qty.get())*float(self.var_price.get())
            # price_cal=float(price_cal)
            price_cal=self.var_price.get()
            cur.execute("select sales from product where pid=?",(self.var_pid.get(),))
            self.sale=cur.fetchone()
            # print(self.sale[0])
            # pid,name,price,qty,status
            cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get(),self.sale[0]]
            # print(self.cart_list)
            #======= Update Cart ==================
            present='no'
            index_=0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present='yes'
                    break
                index_+=1
            if present=='yes':
                op=messagebox.askyesno("Confirm","Product already present\nDo you want to update| Remove from the Cart List",parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        # self.cart_list[index_][2]=price_cal
                        self.cart_list[index_][3]=self.var_qty.get()
            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_update()
    
    def bill_update(self):
        self.bill_amt=0
        self.net_pay=0
        self.discount=0
        for row in self.cart_list:
            self.bill_amt=self.bill_amt+(float(row[2])*int(row[3]))
            
        self.discount=(self.bill_amt*5)/100
        self.net_pay=self.bill_amt-self.discount
        self.canvas.itemconfig(self.billamt,text=f"{str(self.bill_amt)}")
        self.canvas.itemconfig(self.netpay,text=f"{str(self.net_pay)}")
        self.canvas.itemconfig(self.total_product,text=f"{str(len(self.cart_list))}")
    
    
    
    
    def show_cart(self):
        try:
            self.cartTable.delete(*self.cartTable.get_children())
            for row in self.cart_list:
                self.cartTable.insert('',END,values=row)
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
            
    
    def generate_bill(self):
        con=sqlite3.connect(database=r'BMS.db')
        cur=con.cursor()
        try:
            if self.var_cname.get()=='' or self.var_contact.get()=='':
                messagebox.showerror("Error","Customer details are required to generate bill!",parent=self.root)
            elif len(self.cart_list)==0:
                messagebox.showerror("Error","Please add product to the cart!!!",parent=self.root)
            else:
                #==========Bill Top=============
                self.bill_top()
                #==========Bill Middle=============
                self.bill_middle()
                #==========Bill Bottom=============
                self.bill_bottom()
                
                cur.execute("insert into customer (billno,name,contact,price,date) values(?,?,?,?,?)",(str(self.invoice),self.var_cname.get(),self.var_contact.get(),str(self.net_pay),str(self.date_),))
                con.commit()
                fp=open(f'bill/{str(self.invoice)}.txt','w')
                fp.write(self.text_bill_area.get('1.0',END))
                fp.close()
                messagebox.showinfo("Saved","Bill Has generated Successfully",parent=self.root)
                self.chk_print=1
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    
    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp=f'''
\t\tTech Love V-Inventory
\t Phone No. 8377012270, Delhi-110018
{str("="*47)}
 Customer Name: {str(self.var_cname.get())}
 Ph no. : {str(self.var_contact.get())}
 Bill No. : {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*47)}
 Product Name\t\t\tQTY\tPrice
{str("="*47)}
        '''
        self.text_bill_area.delete('1.0',END)
        self.text_bill_area.insert('1.0',bill_top_temp)
    
    def bill_middle(self):
        con=sqlite3.connect(database=r'BMS.db')
        cur=con.cursor()
        try:
            for row in self.cart_list:
                # print(str(row[5]))
                # row 3 is a qty
                # row 4 is a stock
                pid=row[0]
                name=row[1]
                qty=int(row[4])-int(row[3])
                sale=self.sale[0]
                sale=str(int(row[5])+int(row[3]))
                print(row[5],row[3],sale) 
                if int(row[3])==int(row[4]):
                    status='Inactive'
                if int(row[3])!=int(row[4]):
                    status='Active'
                price=str(float(row[2])*int(row[3]))
                self.text_bill_area.insert(END,"\n "+name+"\t\t\t"+row[3]+"\tRs. "+price)
                #=======Update Qty in product table =====
                cur.execute('update product set qty=?,sales=?,status=? where pid=?',(
                      qty,sale,status,pid), )
                con.commit()
            con.close()
            self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    
    
    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*47)}
 Bill Amount\t\t\t\tRs.{self.bill_amt}
 Discount\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\tRs.{self.net_pay}
{str("="*47)}\n
        '''
        self.text_bill_area.insert(END,bill_bottom_temp)
        
    
    def clear_cart(self):
        self.var_pid.set(''),
        self.var_pname.set(''),
        self.var_price.set(''),
        self.var_qty.set('')
        self.canvas.itemconfig(self.instock,text="0")
        self.var_stock.set('')
    
    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.chk_print=0
        self.var_search.set('')
        self.canvas.itemconfig(self.total_product,text="0")
        self.text_bill_area.delete('1.0',END)
        self.canvas.itemconfig(self.billamt,text="0")
        self.canvas.itemconfig(self.netpay,text="0")
        self.canvas.itemconfig(self.total_product,text="0")
        self.clear_cart()
        self.show()
        self.show_cart()
    
    
    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        self.date_=time.strftime("%d-%m-%Y")
        self.canvas.itemconfig(self.date_show,text=f"{str(self.date_)}")
        self.canvas.itemconfig(self.time_show,text=f"{str(time_)}")
        self.canvas.after(200,self.update_date_time)
        
    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo("Print","Please wait while printing ",parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.text_bill_area.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror("Print","Please generate bill , to print recipt",parent=self.root)
    def logout(self):
        self.root.destroy()
        os.system("python loginv2.py")
    def btn_clicked(self):
        print(" search name=",self.var_search.get())
        print(" customer Name=",self.var_cname.get())
        print(" customer Number=",self.var_contact.get())
        print(" product name=",self.var_pname.get())
        print(" price=",self.var_price.get())
        print(" qty=",self.var_qty.get())
        print(" price=",self.var_cal_input.get())

if __name__ == "__main__":
    root=Tk()
    obj=billClass(root)
    root.mainloop() 