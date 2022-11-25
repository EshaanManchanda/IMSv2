from tkinter import *
from tkinter import font
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk, messagebox # to import droup down list or chombo box
import sqlite3


class productClass: #we are make class here
    def __init__(self,root):#this is defaule constructor. root is the object
        self.root = root#this define object of class using self(this is concept of oop's)
        self.root.geometry("1100x500+210+140")#it is used to define size of the frame or window
        self.root.title("Products")
        self.root.config(bg="white")
        self.root.focus_force()
        #====================================================
        #All Variables =============================
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.cat_list=[]
        self.sup_list=[]
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_name=StringVar()
        self.var_status=StringVar()
        self.fetch_cat_sup()
        
        #====Product Frame ==========================
        product_Frame=Frame(self.root,bg="white",bd=2,relief=RIDGE)
        product_Frame.place(x=10,y=10,width=450,height=480)
        
         #====Title =====
        title=Label(product_Frame,text="Product Details",font=("goudy old style",18),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)
        
        
        #=====content in product_Frame================
        
        lbl_category=Label(product_Frame,text="Category",font=("goudy old style",18),bg="white").place(x=30,y=60)
        lbl_supplier=Label(product_Frame,text="Supplier",font=("goudy old style",18),bg="white").place(x=30,y=110)
        lbl_Name=Label(product_Frame,text="Name",font=("goudy old style",18),bg="white").place(x=30,y=160)
        lbl_price=Label(product_Frame,text="Price",font=("goudy old style",18),bg="white").place(x=30,y=210)
        lbl_qty=Label(product_Frame,text="QTY",font=("goudy old style",18),bg="white").place(x=30,y=260)
        lbl_status=Label(product_Frame,text="Status",font=("goudy old style",18),bg="white").place(x=30,y=310)
        
        cmd_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=self.cat_list,font=("goudy old style",15),state='readonly',justify=CENTER)
        cmd_cat.place(x=150,y=60,width=200)
        cmd_cat.current(0)
        
        cmd_sup=ttk.Combobox(product_Frame,textvariable=self.var_sup,values=self.sup_list,font=("goudy old style",15),state='readonly',justify=CENTER)
        cmd_sup.place(x=150,y=110,width=200)
        cmd_sup.current(0)
        
        
        txt_name=Entry(product_Frame,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow")
        txt_name.place(x=150,y=160,width=200)
        
        
        txt_price=Entry(product_Frame,textvariable=self.var_price,font=("goudy old style",15),bg="lightyellow")
        txt_price.place(x=150,y=210,width=200)
        
        
        txt_qty=Entry(product_Frame,textvariable=self.var_qty,font=("goudy old style",15),bg="lightyellow")
        txt_qty.place(x=150,y=260,width=200)
        
        
        cmd_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Active","Inactive"),font=("goudy old style",15),state='readonly',justify=CENTER)
        cmd_status.place(x=150,y=310,width=200)
        cmd_status.current(0)
        
        
        #====Buttons =================================
        
        btn_add=Button(product_Frame,text="Save",command=self.add,font=("goudy old style",15),cursor="hand2",bg="#2196f3",fg="white").place(x=10,y=400,width=100,height=40)
        btn_update=Button(product_Frame,text="Update",command=self.update,font=("goudy old style",15),cursor="hand2",bg="#4caf50",fg="white").place(x=120,y=400,width=100,height=40)
        btn_delete=Button(product_Frame,text="Delete",command=self.delete,font=("goudy old style",15),cursor="hand2",bg="#f44336",fg="white").place(x=230,y=400,width=100,height=40)
        btn_clear=Button(product_Frame,text="Clear",command=self.clear,font=("goudy old style",15),cursor="hand2",bg="#607d8b",fg="white").place(x=340,y=400,width=100,height=40)
        
        
        #====Search Frame =====
        
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bg="white",bd=2,relief=RIDGE)
        SearchFrame.place(x=480,y=10,width=600,height=80)
        
        #=====options =====
        
        cmd_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Category","Name","Supplier"),font=("goudy old style",15),state='readonly',justify=CENTER)
        cmd_search.place(x=10,y=10,width=180)
        cmd_search.current(0)
        
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),cursor="hand2",bg="#4caf50",fg="white").place(x=410,y=9,width=150,height=30)
        
        #====Product Details ==========================
        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=390)
        
        scrolly=Scrollbar(p_frame,orient=VERTICAL) 
        scrollx =Scrollbar(p_frame,orient=HORIZONTAL)
        
        self.productTable=ttk.Treeview(p_frame,columns=("pid","Category","Supplier","Name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)
        self.productTable.heading("pid",text="Product ID")
        self.productTable.heading("Name",text="Name")
        self.productTable.heading("Category",text="Category")
        self.productTable.heading("Supplier",text="Supplier")
        self.productTable.heading("price",text="Price")
        self.productTable.heading("qty",text="Qty")
        self.productTable.heading("status",text="Status")
    
        self.productTable["show"]="headings"

        self.productTable.column("pid",width=80)
        self.productTable.column("Name",width=100)
        self.productTable.column("Category",width=100)
        self.productTable.column("Supplier",width=100)
        self.productTable.column("price",width=100)
        self.productTable.column("qty",width=60)
        self.productTable.column("status",width=100)
        
        self.productTable.pack(fill=BOTH,expand=1)
        self.productTable.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()
        
# ===================================================================================


    def fetch_cat_sup(self):
        con=sqlite3.connect(database=r'BMS.db')
        cur=con.cursor()
        try:
            self.cat_list.append("Empty")
            self.sup_list.append("Empty")
            cur.execute("Select name from category")  
            cat=cur.fetchall()
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
            cur.execute("Select name from supplier")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:(str(ex))",parent=self.root)
#====add function ==========================
    def add(self):
        con=sqlite3.connect(database=r'BMS.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_name.get()=="" or self.var_sup=="Select":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
            else:
                cur.execute("select * from product where Category=? and Supplier=? and Name=?",(self.var_cat.get(),self.var_sup.get(),self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Product already exist , try different one",parent=self.root)
                else:
                    cur.execute("Insert into product(Category , Supplier , Name , price , qty , status,sales ) values(?,?,?,?,?,?,0)",(
                        self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Added successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        self.show()

    def show(self):
        con=sqlite3.connect(database=r'BMS.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('',END,values=row)
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
 
    def get_data(self,ev):
        f=self.productTable.focus()
        content=(self.productTable.item(f))
        row=content['values']
        self.var_cat.set(row[1]),
        self.var_sup.set(row[2]),
        self.var_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_qty.set(row[5]),
        self.var_status.set(row[6])
#================================================================
#====Update Funtion ==========================

    def update(self):
        con=sqlite3.connect(database=r'BMS.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_name.get()=="" or self.var_sup=="Select":
                messagebox.showerror("Error","All product details  required",parent=self.root)
            else:
                cur.execute("select * from product where Category=? and Supplier=? and Name=?",(self.var_cat.get(),self.var_sup.get(),self.var_name.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product",parent=self.root)
                else:
                    cur.execute("update product set price=?, qty=?, status=? where Category=? and Supplier=? and Name=?",(
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                        self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_name.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Updated successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        self.show()
        
#================================================================
#====Delete Funtion ==========================

    def delete(self):
        con=sqlite3.connect(database=r'BMS.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_name.get()=="" or self.var_sup=="Select":
                messagebox.showerror("Error","All product details required",parent=self.root)
            else:
                cur.execute("select * from product where Category=? and Supplier=? and Name=?",(self.var_cat.get(),self.var_sup.get(),self.var_name.get(),))
                row=cur.fetchone()
                if row==None:
                     messagebox.showerror("Error","Invalid Product",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from product  where Category=? and Supplier=? and Name=?",(self.var_cat.get(),self.var_sup.get(),self.var_name.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Product Delete Successfully")
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        self.show()
        self.clear()
# ====================================================
#====clear Function ==========================

    def clear(self):
        self.var_cat.set("Select"),
        self.var_sup.set("Select"),
        self.var_name.set(""),
        self.var_price.set(""),
        self.var_qty.set(""),
        self.var_status.set("Active"),
        self.var_searchby.set("Select"),
        self.var_searchtxt.set("")
        self.show()


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
                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
            rows=cur.fetchall()
            if len(rows)!=0:
                self.productTable.delete(* self.productTable.get_children())
                for row in rows:
                    self.productTable.insert('',END,values=row)
            else:
                 messagebox.showerror("Error","No Record Found!",parent=self.root)   
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
            
                    
if __name__ == "__main__":
    root=Tk()#make root oject of tk class
    obj=productClass(root)#making obj  object of IMS class, passig   root to attache with tk class
    root.mainloop()#i  use this program to stay the window  otherwise it exit imidately 