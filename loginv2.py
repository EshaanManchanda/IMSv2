from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import sqlite3 , os,email_pass,time
import smtplib
class Login_system:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x712+0+0")
        self.root.title("Inventory Management System|Login")
        self.root.config(bg="#fafafa")
        #============variables =============
        self.otp=''
        self.employee_id=StringVar()
        self.password=StringVar()
        self.date_=time.strftime("%d/%m/%Y")
        self.time_=time.strftime("%I:%M:%S")
        
        canvas = Canvas(
            self.root,
            bg = "#ffffff",
            height = 712,
            width = 1350,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        self.img_login = PhotoImage(file = f"images/login/img0.png")
        self.btn_login = Button(
            image = self.img_login,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.login,
            relief = "flat")

        self.btn_login.place(
            x = 948, y = 526,
            width = 177,
            height = 61)

        self.entry0_img = PhotoImage(file = f"images/login/img_textBox0.png")
        entry0_bg = canvas.create_image(
            1050.0, 236.0,
            image = self.entry0_img)

        self.entry0 = Entry(
            bd = 0,
            bg = "#ffffff",
            fg="#3856C0",
            textvariable=self.employee_id,
            font=("goudy old style",20,"bold"),
            highlightthickness = 0)

        self.entry0.place(
            x = 870, y = 211,
            width = 360,
            height = 48)

        self.entry1_img = PhotoImage(file = f"images/login/img_textBox1.png")
        self.entry1_bg = canvas.create_image(
            1050.0, 380.0,
            image = self.entry1_img)

        self.entry1 = Entry(
            bd = 0,
            bg = "#ffffff",
            fg="#3856C0",
            textvariable=self.password,
            font=("goudy old style",20,"bold"),
            highlightthickness = 0)

        self.entry1.place(
            x = 870, y = 355,
            width = 360,
            height = 48)

        self.img1 = PhotoImage(file = f"images/login/img1.png")
        self.b1 = Button(
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.forget_window,
            relief = "flat")

        self.b1.place(
            x = 1128, y = 423,
            width = 121,
            height = 24)

        self.background_img = PhotoImage(file = f"images/login/background.png")
        self.background = canvas.create_image(
            492.5, 278.5,
            image=self.background_img)
        
# =========================All Functions========================
    def login(self):
        con=sqlite3.connect(database=r'BMS.db')
        cur=con.cursor()
        # print(self.employee_id.get(),self.password.get())
        try:
            if self.employee_id.get()==""or self.password.get()=="":
                messagebox.showerror("Error","All fields are required!",parent=self.root)
            else:
                cur.execute("select utype from employee where eid=? and pass=?",(self.employee_id.get(),self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error","Invalid Employee ID or Password!",parent=self.root)
                else:
                    cur.execute("update employee set loginDate=?,loginTime=? where eid=?",(self.date_,self.time_,self.employee_id.get()))
                    # cur.execute("UPDATE product SET sales = '0' WHERE sales IS NULL;")
                    con.commit()
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboardv2.py")
                    else:
                        self.root.destroy()
                        os.system("python billingv2.py")
                    cur.execute("update employee set loginDate=NULL,loginTime=NULL where eid=?",(self.employee_id.get(),))
                    con.commit()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    
    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_img.config(image=self.im)
        self.lbl_change_img.after(3000,self.animate)
        
    def forget_window(self):
        con=sqlite3.connect(database=r'BMS.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="":
                messagebox.showerror("Error","Employee ID must me required!",parent=self.root)
            else:
                cur.execute("select email from employee where eid=?",(self.employee_id.get(),))
                email=cur.fetchone()
                if email==None:
                    messagebox.showerror("Error","Invalid Employee ID, try again!",parent=self.root)
                else:
                    # ==============Forget Window============
                    # call send_email_function()
                    chk=self.send_email(email[0])
                    if chk=='f':
                        messagebox.showerror("Error","Connection Error, Try again",parent=self.root)
                    else:
                        self.var_otp=StringVar()
                        self.var_new_pass=StringVar()
                        self.var_conf_pass=StringVar()
                        self.forget_win=Toplevel(self.root)
                        self.forget_win.title("Reset Password")
                        self.forget_win.geometry('400x350+500+100')
                        self.forget_win.focus_force()

                        title=Label(self.forget_win, text='Reset Password',font=('goudy old style',15,'bold'),bg='#3f51b5',fg='white').pack(side=TOP,fill=X)
                        
                        
                        lbl_reset=Label(self.forget_win, text='Enter OTP send on Register Email',font=("times new roman",15)).place(x=20,y=60)
                        text_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",15),bg="lightyellow").place(x=20,y=100,width=250,height=30)
                        
                        lbl_newpass=Label(self.forget_win, text='New Password',font=("times new roman",15)).place(x=20,y=160)
                        text_newpass=Entry(self.forget_win,textvariable=self.var_new_pass,font=("times new roman",15),bg="lightyellow").place(x=20,y=190,width=250,height=30)
                        
                        lbl_confpass=Label(self.forget_win, text='confirm Password',font=("times new roman",15)).place(x=20,y=225)
                        text_confpass=Entry(self.forget_win,textvariable=self.var_conf_pass,font=("times new roman",15),bg="lightyellow").place(x=20,y=250,width=250,height=30)
                        
                        self.update=Button(self.forget_win,text="Update",command=self.update_password,state=DISABLED,font=("times new roman",15),bg="lightblue")
                        self.update.place(x=150,y=300,width=100,height=30)
                        
                        self.btn_reset=Button(self.forget_win,text="SUBMIT",command=self.validate_otp_functon,font=("times new roman",15),bg="lightblue")
                        self.btn_reset.place(x=280,y=100,width=100,height=30)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    
    def update_password(self):
        if self.var_new_pass.get()==""or self.var_conf_pass.get()=="":
            messagebox.showerror("Error","Password is required", self.forget_win)
        elif self.var_new_pass.get()!=self.var_conf_pass.get():
            messagebox.showerror("Error","New Password and Confirm Password should be same", self.forget_win)
        else:
            con=sqlite3.connect(database=r'BMS.db')
            cur=con.cursor()
            try:
                cur.execute("update employee set pass=? where eid=?",(self.var_new_pass.get(),self.employee_id.get()))
                con.commit()
                messagebox.showinfo("Success","Password updated successfully",parent=self.forget_win)
                self.forget_win.destroy()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.forget_win)
            
    def validate_otp_functon(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
        else:
            messagebox.showerror("Error","Invalid OTP, Try Again",parent=self.forget_win)
    def send_email(self,to_):
        s=smtplib.SMTP("smtp.gmail.com",587)
        s.starttls()
        email_=email_pass.email
        pass_=email_pass.pass_
        s.login(email_,pass_)
        self.otp=int(time.strftime("%S%M%H"))+int(time.strftime("%S"))
        subj='IMS- Reset Password OTP'
        msg=f'Dear sir/Madam,\n\nYour Reset OTP is {str(self.otp)}.\n\nWith Regards,\nIMS Team'
        msg="Subject:{}\n\n{}".format(subj,msg)
        s.sendmail(email_,to_,msg)
        chk=s.ehlo()
        if chk[0]==250:
            return 's'
        else:
            return 'f'
        
root=Tk()
obj=Login_system(root)
root.mainloop()