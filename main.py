from tkinter import *
from tkinter import messagebox
import pymysql as pq
import time
from dbms import *
from functions import *


database()
connect()
connect1()
def viewwindow():
    gui = Toplevel(root)
    gui.title("VIEW ALL USERS")
    gui.geometry("800x700")
    Message(gui,font=("Castellar", 22, "bold"),text = "NAME      USERNAME      PASSWORD",width=700).pack()
    for row in viewallusers():
        a=row[0]
        b=row[1]
        c=""
        f=len(row[2])
        for i in range (f):
            c= c + "*"
        d = a + "         " + b + "           " + c
        Message(gui,fg='#6680ff',font=("adobe clean", 25, "bold"),text = d,width=700).pack()
    Button(gui,text="Delete all users",font=("candara",15,"bold"),activebackground="black",activeforeground="red",width=12,command=deleteallusers).pack()
    Button(gui,text="Exit Window",font=("candara",15,"bold"),activebackground="black",activeforeground="red",width=12,command=gui.destroy).pack()

def register():
        
    


        a = register_name.get()
        b = register_username.get()
        c = register_password.get()
        d = register_repassword.get()
        password_to_check="swaraj"
        

        conn=pq.connect(user="root",host="localhost",password="" ,database="my_expenses")
        cur=conn.cursor()
        # pa=cur.execute('''SELECT username FROM users WHERE name='ab' ''')
        # pa=cur.fetchone()
        # print(pa)
        query=('''SELECT * FROM users WHERE username=%s ''')
        cur.execute(query,(register_username.get()))
        row=cur.fetchone()
        
        query=('''SELECT * FROM users WHERE password=%s ''')
        cur.execute(query,(register_password.get()))
        row1=cur.fetchone()



        if c==d and c!="" and len(c)>5 and a!="" and b!="" and row==None and row1==None and a!=b:
        
            adduser(a,b,c)
            messagebox.showinfo(':)', 'Registration Successful')      
        else :
            if(a=="" or b=="" or c=="" or d==""):
                messagebox.showinfo('oops something wrong', 'Field should not be empty')
            elif(row!=None):
                messagebox.showinfo(':)', 'user name alredy taken \n please try with anotherone')
            elif(row1!=None):
                messagebox.showinfo(':)', 'password alredy taken \n please try with anotherone')
            elif(a==b):
                messagebox.showinfo('warning', 'username should not same as name')
            else:
                # if(b==row):
                #     messagebox.showinfo('warning', 'user name alredy taken /n please try with anotherone')
                # elif(c==row1):
                #     messagebox.showinfo('warning', 'password  alredy taken /n please try with anotherone')
                # else:
                    messagebox.showinfo('oops something wrong', 'Both passwords should be same! \nPassword should contain atleast 6 characters')
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)


        conn.commit()
        conn.close()
   


def login():
    a = login_username.get()
    b = login_password.get()
    getusername(a,b)   
    if (checkuser(a,b))!=None:
        root.destroy()
        appwindow()     
    else:
        e1.delete(0,END)
        e2.delete(0,END)
        messagebox.showinfo('oops something wrong', 'Invalid credentials')




root = Tk()
# width=root.winfo_screenwidth()
# height=root.winfo_screenheight()
# root.geometry(f"{width}x{height}")

# root.configure(bg='#0066ff')
frame = Frame(bd=0, highlightthickness=0, background="#2684a6").place(relx=0.5, y=0, relwidth=1, relheight=1)
frame = Frame(bd=0, highlightthickness=0, background="#b789c4").place(x=0, y=0,height=720,width=640)

# frame2 = Frame(bd=0, highlightthickness=0, background="#33cccc").place(x=0, rely=0.5, relwidth=1, relheight=1)
root.title("LOGIN / REGISTER")
root.geometry("1280x720")
l1=Label(root,font=("comic sans ms",19),text="Username",fg="red",bg="black").place(x=783,y=280)
l2=Label(root,font=("comic sans ms",19),text="Password",fg="red",bg="black").place(x=785,y=345)
b1=Button(root,text="Login",font=("algerian",19),activebackground="black",activeforeground="red",width=12,height=1,command=login).place(x=980,y=427)
l6=Label(root,font=("comic sans ms",19),text="Name",fg="red",bg="black").place(x=216,y=150)#,width=265,height=25)
l3=Label(root,font=("comic sans ms",19),text="Username",fg="red",bg="black").place(x=166,y=216)#,width=265,height=25)
l4=Label(root,font=("comic sans ms",19),text="Password",fg="red",bg="black").place(x=172,y=280)#,width=265,height=25)
l5=Label(root,font=("comic sans ms",17),text="Confirm password",fg="red",bg="black").place(x=88,y=345)#,width=265,height=25)
b2=Button(root,text="Register",font=("algerian",19),activebackground="black",activeforeground="red",width=12,command=register).place(x=320,y=427)
login_username=StringVar()
e1=Entry(root,font=("adobe clean",15),textvariable=login_username)
e1.place(x=990,y=285,height=30,width=165)
login_password=StringVar()
e2=Entry(root,font=("adobe clean",15),textvariable=login_password,show="*")
e2.place(x=990,y=349,height=30,width=165)
register_name=StringVar()
e6=Entry(root,font=("adobe clean",15),textvariable=register_name)
e6.place(x=335,y=156,height=30,width=165)
register_username=StringVar()
e3=Entry(root,font=("adobe clean",15),textvariable=register_username)
e3.place(x=335,y=225,height=30,width=165)
register_password=StringVar()
e4=Entry(root,font=("adobe clean",15),textvariable=register_password, show="*")
e4.place(x=335,y=285,height=30,width=165)
register_repassword=StringVar()
e5=Entry(root,font=("adobe clean",15),textvariable=register_repassword, show="*")
e5.place(x=335,y=349,height=30,width=165)
Label(root,font=("Bauhaus 93",66),fg="black",bg="#2684a6",text="EXPENSE ").place(x=300,y=0,width=380,height=85)
Label(root,font=("Bauhaus 93",66),fg="black",bg="#b789c4",text="TRACKER").place(x=640,y=0,width=380,height=85)

Label(root,font=("calibri",16),bg="#b789c4",fg="black",text="Vicky").place(x=585,y=690)
Label(root,font=("calibri",16),bg="#2684a6",fg="black",text="Sandhu").place(x=640,y=690)

b3=Button(root,text="E\nx\ni\nt \n\nW\ni\nn\nd\no\nw",font=("candara",15,"bold"),activebackground="black",activeforeground="red",command=root.destroy).place(x=1245,y=440)
b5=Button(root,text="View all users",font=("algerian",15),activebackground="black",activeforeground="red",width=15,height=1,command=viewwindow).place(x=980,y=500)
ltime=Label(root,font=("century",30),bg="#2684a6",fg="black")
ltime.place(x=850,y=675)
# dtime=Label(root,font=("century",30),bg="#b789c4",fg="black")
# dtime.place(x=0,y=675)
def digitalclock():
    text_input = time.strftime("%d-%m-%Y  %H:%M:%S")
    ltime.config(text=text_input)
    ltime.after(1000,digitalclock)
digitalclock()
root.resizable(False, False)
root.mainloop()
