import os
from tkinter import *
from tkinter import font
from tkinter import messagebox
from PIL import Image,ImageTk 
from tkinter import ttk
import sqlite3


class IMS: 
    def __init__(self,root):
        self.root = root
        self.root.geometry("100x65+500+350")
        self.root.config(bg="white")
        
        self.phone_image=ImageTk.PhotoImage(file="images/logo.png")
        self.bg=Label(self.root,image=self.phone_image,bd=0)
        self.bg.pack(fill=BOTH)
        self.root.overrideredirect(True)
        # self.fetchemp()
        self.root.after(3000, self.fetchemp)
    
    def fetchemp(self):
        con=sqlite3.connect(database=r'BMS.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee",)
            user=cur.fetchone()
            cur.close()
            con.close()
            if user==None:
                self.root.destroy()
                os.system("python first_user.py")
            else:
                self.root.destroy()
                os.system("python loginv2.py")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    

                    
    
        
        
if __name__ == "__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()