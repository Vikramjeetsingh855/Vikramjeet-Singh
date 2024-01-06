from tkinter import *
from tkinter import messagebox
import pymysql as pq
import time
from dbms import *


profilename=""

def getusername(username,password):
    conn=pq.connect(user="root",host="localhost",password="" ,database="my_expenses")
    cur=conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=%s AND password=%s",(username,password))
    result=cur.fetchone()
    global profilename
    if result!=None:
        profilename=result[0]
t=6
def appwindow():

    def connect1():
        conn=pq.connect(user="root",host="localhost",password="" ,database="my_expenses")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS expensetable(id INTEGER PRIMARY KEY,itemname TEXT,date TEXT,cost TEXT)")
        conn.commit()
        conn.close()
    connect1()

    def insert(itemname,date,cost):
        conn=pq.connect(user="root",host="localhost",password="" ,database="my_expenses")
        cur=conn.cursor()
        cur.execute("INSERT INTO expensetable VALUES(NULL,%s,%s,%s)",(itemname,date,cost))
        conn.commit()
        conn.close()

    def view():
        conn=pq.connect(user="root",host="localhost",password="" ,database="my_expenses")
        cur=conn.cursor()
        cur.execute("SELECT * FROM expensetable")
        rows=cur.fetchall()
        conn.commit()

        conn.close()
        return rows
    
    def search(itemname="",date="",cost=""):
        conn=pq.connect(user="root",host="localhost",password="" ,database="my_expenses")
        cur=conn.cursor()
        cur.execute("SELECT *FROM expensetable WHERE itemname=%s OR date=%s OR cost=%s",(itemname,date,cost))
        rows=cur.fetchall()
        conn.commit()
        conn.close()
        return rows

    def delete(id):
        conn=pq.connect(user="root",host="localhost",password="" ,database="my_expenses")
        cur=conn.cursor()
        cur.execute("DELETE FROM expensetable WHERE id=%s",(id))
        conn.commit()
        conn.close()
    
    def deletealldata():
        conn=pq.connect(user="root",host="localhost",password="" ,database="my_expenses")
        cur=conn.cursor()
        cur.execute("DELETE FROM expensetable")
        conn.commit()
        conn.close()
        list1.delete(0,END)
        messagebox.showinfo('Successful', 'All data deleted')

    def sumofitems():
        conn=pq.connect(user="root",host="localhost",password="" ,database="my_expenses")
        cur=conn.cursor()
        cur.execute("SELECT SUM(cost) FROM expensetable")
        sum=cur.fetchone()
        list1.delete(0,END)
        b=str(sum[0])
        a="YOU SPENT " + b
        messagebox.showinfo('TOTAL SPENT',a)
        conn.commit()
        conn.close()
        return sum
    
    def insertitems():
        # n=exp_id.get()
        a=exp_itemname.get()
        b=exp_date.get()
        c=exp_cost.get()
        d=c.replace('.', '', 1)
        e=b.count('-')      

        if a=="" or b=="" or c=="":
            messagebox.showinfo("oops something wrong","Field should not be empty")
        elif len(b)!=10 or e!=2:
            messagebox.showinfo("oops something wrong","DATE should be in format dd-mm-yyyy")
        elif (d.isdigit()==False):
            messagebox.showinfo("oops something wrong","Cost should be a number")
        else:
            insert(a,b,c)
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
        list1.delete(0,END)

    def viewallitems():
        list1.delete(0,END)
        list1.insert(END,"ID   NAME     DATE      COST")
        for row in view():
            a=str(row[0])
            b=str(row[1])
            c=str(row[2])
            d=str(row[3])
            f= a + "     " + b + "    " + c + "    " + d
            list1.insert(END,f)
    
    def deletewithid():
        list1.delete(0,END)
        a=exp_id.get()
        delete(a)
    
    def search_item():
        list1.delete(0,END)
        list1.insert(END,"ID   NAME     DATE      COST")
        for row in search(exp_itemname.get(),exp_date.get(),exp_cost.get()):
            a=str(row[0])
            b=str(row[1])
            c=str(row[2])
            d=str(row[3])
            f= a + "     " + b + "    " + c + "    " + d
            list1.insert(END,f)
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)

    
    def endpage():
        Label(gui,width=100,height=100,font=("century",35),bg="#9999ff",text="").place(x=-455,y=0)
        # Label(gui,font=("lucida fax",40),bg="#bfbfbf",text="EXPENSE TRACKER").place(x=190,y=10)
        Label(gui,font=("Bauhaus 93",66),fg="black",bg="#9999ff",text="EXPENSE ").place(x=300,y=0,width=380,height=85)
        Label(gui,font=("Bauhaus 93",66),fg="black",bg="#9999ff",text="TRACKER").place(x=640,y=0,width=380,height=85)
        Label(gui,font=("calibri bold",40),bg="#9999ff",text="This application developed using SQL and tkinter").place(x=110,y=230)
        # Label(gui,font=("calibri",40),bg="#bfbfbf",text="SQL and tkinter").place(x=800,y=250)
        Label(gui,font=("calibri bold",35),bg="#9999ff",text="By Vikramjeet Singh").place(x=228,y=464,width=822,height=135)
        h=Label(gui,font=("calibri bold",30),bg="#9999ff",text="Thanks for visiting \nhave a nice day")
        h.place(x=228,y=328,width=822,height=135)
        ltime=Label(gui,font=("century",50),bg="#9999ff",fg="black")
        ltime.place(x=625,y=640)      
        def timer():
            global t
            a=str(t)
            text_input = a
            ltime.config(text=text_input)
            ltime.after(1000, timer)
            t=t-1
        timer()
        gui.after(7000,gui.destroy)
        

    gui = Tk()

    gui.title("EXPENSE TRACKER")
    gui.configure(bg='#9999ff')
    gui.geometry("1280x720")
    l12=Label(gui,width=60,height=7,font=("century",35),bg="#9999ff",text="",borderwidth=2,relief="solid").place(x=0,y=60,width=640,height=340)

    l8=Label(gui,width=60,height=7,font=("century",35),bg="#1ad1ff",text="",borderwidth=2,relief="solid").place(x=0,y=380,width=640,height=340)
    # l7=Label(gui,width=100,height=10,font=("century",35),bg="#1affd1",text="").place(x=-455,y=410)
    l1=Label(gui,font=("comic sans ms",17),bg="#9999ff",text="Product name").place(x=10,y=150)
    exp_itemname=StringVar()
    e1=Entry(gui,font=("adobe clean",15),textvariable=exp_itemname)
    e1.place(x=220,y=155,height=27,width=165)
    l2=Label(gui,font=("comic sans ms",17),bg="#9999ff",text="Date(dd-mm-yyyy)").place(x=10,y=200)
    exp_date=StringVar()
    e2=Entry(gui,font=("adobe clean",15),textvariable=exp_date)
    e2.place(x=220,y=205,height=27,width=165)
    l3=Label(gui,font=("comic sans ms",17),bg="#9999ff",text="Cost of product").place(x=10,y=250)
    exp_cost=StringVar()
    e3=Entry(gui,font=("adobe clean",15),textvariable=exp_cost)
    e3.place(x=220,y=255,height=27,width=165)
    l4=Label(gui,font=("comic sans ms",17),bg="#1ad1ff",text="Select ID to delete").place(x=100,y=450,width=315,height=38)
    exp_id=StringVar()
    sb=Spinbox(gui, font=("adobe clean",17),from_= 0, to_ = 200,textvariable=exp_id,justify=CENTER)
    sb.place(x=400,y=453,height=30,width=50)
    scroll_bar=Scrollbar(gui)
    scroll_bar.place(x=1256,y=60,height=720,width=20)  
    list1=Listbox(gui,height=7,width=30,font=("comic sans ms",20),bg="grey",yscrollcommand = scroll_bar.set,borderwidth=2,relief="solid")
    list1.place(x=640,y=60,width=620,height=720)
    scroll_bar.config( command = list1.yview )
    b1=Button(gui,text="Add Item",font=("georgia",17),activebackground="black",activeforeground="red",width=10,command=insertitems).place(x=30,y=300)
    b2=Button(gui,text="View all items",font=("georgia",17),bg="#6fc276",activebackground="black",activeforeground="red",width=12,command=viewallitems,borderwidth=2,relief="solid").place(x=640,y=0,width=375,height=60)
    b3=Button(gui,text="Delete with id",font=("georgia",17),activebackground="black",activeforeground="red",width=12,command=deletewithid).place(x=170,y=505)
    b4=Button(gui,text="Delete all items",font=("georgia",17),activebackground="black",activeforeground="red",width=15,command=deletealldata).place(x=140,y=575)
    b5=Button(gui,text="Search",font=("georgia",17),activebackground="black",activeforeground="red",width=10,command=search_item).place(x=220,y=298)
    b6=Button(gui,text="Total spent",font=("georgia",17),activebackground="black",activeforeground="red",width=15,command=sumofitems).place(x=140,y=645)
    b7=Button(gui,text="Close app",font=("georgia",17),bg="#6fc276",activebackground="black",activeforeground="red",width=10,command=endpage,borderwidth=2,relief="solid").place(x=1016,y=0,width=262,height=60)
    Label(gui,font=("Bauhaus 93",55,"underline"),fg="black",bg="#6fc276",text="EXPENSE TRACKER",borderwidth=2,relief="solid").place(x=0,y=0,width=640,height=60)
    # Label(gui,font=("Bauhaus 93",66),fg="black",bg="white",text="TRACKER").place(x=640,y=0,width=380,height=85)
    name = "Welcome " + profilename
    l9=Label(gui,width=60,font=("century",30,"underline"),bg="#9999ff",fg="black",text=name).place(x=5,y=75,width=630,height=62)
    ltime=Label(gui,font=("century",30),bg="#6fc276",fg="black",borderwidth=2,relief="solid")
    ltime.place(x=640,y=657,width=640,height=63)
    def digitalclock():
        text_input = time.strftime("%d-%m-%Y   %H:%M:%S")
        ltime.config(text=text_input)
        ltime.after(1000, digitalclock)
    digitalclock()
    gui.resizable(False, False)
    gui.mainloop()

    # gui = Tk()
    # gui.title("EXPENSE TRACKER")
    # gui.configure(bg='#0066ff')
    # gui.geometry("900x700")
    # l8=Label(gui,width=60,height=7,font=("century",35),bg="#1ad1ff",text="").place(x=450,y=60)
    # l7=Label(gui,width=100,height=10,font=("century",35),bg="#1affd1",text="").place(x=-455,y=410)
    # l1=Label(gui,font=("comic sans ms",17),bg="#0066ff",text="Product name").place(x=10,y=150)
    # exp_itemname=StringVar()
    # e1=Entry(gui,font=("adobe clean",15),textvariable=exp_itemname)
    # e1.place(x=220,y=155,height=27,width=165)
    # l2=Label(gui,font=("comic sans ms",17),bg="#0066ff",text="Date(dd-mm-yyyy)").place(x=10,y=200)
    # exp_date=StringVar()
    # e2=Entry(gui,font=("adobe clean",15),textvariable=exp_date)
    # e2.place(x=220,y=205,height=27,width=165)
    # l3=Label(gui,font=("comic sans ms",17),bg="#0066ff",text="Cost of product").place(x=10,y=250)
    # exp_cost=StringVar()
    # e3=Entry(gui,font=("adobe clean",15),textvariable=exp_cost)
    # e3.place(x=220,y=255,height=27,width=165)
    # l4=Label(gui,font=("comic sans ms",17),bg="#1ad1ff",text="Select ID to delete").place(x=520,y=170)
    # exp_id=StringVar()
    # sb=Spinbox(gui, font=("adobe clean",17),from_= 0, to_ = 200,textvariable=exp_id,justify=CENTER)
    # sb.place(x=745,y=174,height=30,width=50)
    # scroll_bar=Scrollbar(gui)
    # scroll_bar.place(x=651,y=410,height=277,width=20)  
    # list1=Listbox(gui,height=7,width=30,font=("comic sans ms",20),yscrollcommand = scroll_bar.set)
    # list1.place(x=168,y=410)
    # scroll_bar.config( command = list1.yview )
    # b1=Button(gui,text="Add Item",font=("georgia",17),activebackground="#fffa66",activeforeground="red",width=10,command=insertitems).place(x=30,y=300)
    # b2=Button(gui,text="View all items",font=("georgia",17),activebackground="#fffa66",activeforeground="red",width=12,command=viewallitems).place(x=110,y=355)
    # b3=Button(gui,text="Delete with id",font=("georgia",17),activebackground="#fffa66",activeforeground="red",width=12,command=deletewithid).place(x=572,y=220)
    # b4=Button(gui,text="Delete all items",font=("georgia",17),activebackground="#fffa66",activeforeground="red",width=15,command=deletealldata).place(x=550,y=280)
    # b5=Button(gui,text="Search",font=("georgia",17),activebackground="#fffa66",activeforeground="red",width=10,command=search_item).place(x=220,y=298)
    # b6=Button(gui,text="Total spent",font=("georgia",17),activebackground="#fffa66",activeforeground="red",width=15,command=sumofitems).place(x=550,y=340)
    # b7=Button(gui,text="Close app",font=("georgia",17),activebackground="#fffa66",activeforeground="red",width=10,command=endpage).place(x=700,y=650)
    # l6=Label(gui,width=60,font=("century",35),bg="#ff9999",fg="#b32d00",text="EXPENSE  TRACKER").place(x=-450,y=0)
    # name = "Welcome " + profilename
    # l9=Label(gui,width=60,font=("century",30),bg="#9999ff",fg="black",text=name).place(x=-530,y=61)
    # ltime=Label(gui,font=("century",30),bg="#9999ff",fg="black")
    # ltime.place(x=470,y=61)
    # def digitalclock():
    #     text_input = time.strftime("%d-%m-%Y   %H:%M:%S")
    #     ltime.config(text=text_input)
    #     ltime.after(1000, digitalclock)
    # digitalclock()
    # gui.resizable(False, False)
    # gui.mainloop()