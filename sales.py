from tkinter import *
from tkinter import font
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk, messagebox # to import droup down list or chombo box
import sqlite3
import os


class salesClass: #we are make class here
    def __init__(self,root):#this is defaule constructor. root is the object
        self.root = root#this define object of class using self(this is concept of oop's)
        self.root.geometry("1100x500+210+140")#it is used to define size of the frame or window
        self.root.title("Sales")
        self.root.config(bg="white")
        self.root.focus_force()
        self.bill_list = []
        
        self.var_invoice=StringVar()
        
        #=====Title ==========================
        lbl_title = Label(self.root,text="View Customer Bill",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        
        lbl_invoice=Label(self.root,text="Invoice No.",font=("times new roman",15),bg="white").place(x=50,y=100)
        
        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("times new roman",15),bg="lightyellow").place(x=160,y=100,width=180,height=28)
        
        btn_search=Button(self.root,text="Search",command=self.search,font=("times new roman",15,"bold"),cursor="hand2",bg="#2196f3",fg="white").place(x=360,y=100,width=120,height=28)
        
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15,"bold"),cursor="hand2",bg="lightgray").place(x=490,y=100,width=120,height=28)
        
        #=====Bill List =================
        sales_Frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_Frame.place(x=50,y=140,width=200,height=330)
        
        scrolly=Scrollbar(sales_Frame,orient=VERTICAL)
        self.sales_list=Listbox(sales_Frame,font=("goudy old style",15),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH,expand=1)
        self.sales_list.bind("<ButtonRelease-1>",self.get_data)
        #=====Bill area =================
        bill_Frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_Frame.place(x=280,y=140,width=410,height=330)
        
        lbl_title2 = Label(bill_Frame,text="Customer Bill Area",font=("goudy old style",20),bg="orange").pack(side=TOP,fill=X)
        
        scrolly2=Scrollbar(bill_Frame,orient=VERTICAL)
        self.bill_area=Text(bill_Frame,bg="lightyellow",yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)
        
        #====Image================================
        self.bill_photo=Image.open("images/cat2.jpg")
        self.bill_photo=self.bill_photo.resize((450,300),Image.LANCZOS)
        self.bill_photo=ImageTk.PhotoImage(self.bill_photo)
        
        lbl_image=Label(self.root,image=self.bill_photo,bd=0)
        lbl_image.place(x=700,y=110)
        
        self.show()
#========================================================================================
    def show(self):
        del self.bill_list[:]
        self.sales_list.delete(0,END)
        # print(os.listdir("bill"))
        for i in os.listdir('bill'):
            if i.split(".")[-1]=='txt':
                self.sales_list.insert(END,i)
                self.bill_list.append(i.split('.')[0])
    def get_data(self,ev):
        index_=self.sales_list.curselection()
        file_name=self.sales_list.get(index_)
        # print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()
    
    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice No. should be required ", parent=self.root)    
        else:
            if self.var_invoice.get() in self.bill_list:
                self.bill_area.delete('1.0',END)
                fp=open(f'bill/{self.var_invoice.get()}.txt','r')
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close() 
            else:
                 messagebox.showerror("Error","Invalid Invoice Number", parent=self.root)
                 
    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)
if __name__ == "__main__":
    root=Tk()#make root oject of tk class
    obj=salesClass(root)#making obj  object of IMS class, passig   root to attache with tk class
    root.mainloop()#i  use this program to stay the window  otherwise it exit imidately 