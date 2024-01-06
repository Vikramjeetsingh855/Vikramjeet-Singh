from tkinter import *
from tkinter import messagebox
import pymysql as pq
import time




def database():
    
    conn=pq.connect(
        user="root",
        host="localhost",
        password="" ,
        database="")
    cur=conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS my_expenses")
    conn.commit()


def connect():
    global conn,cur
    conn=pq.connect(
        user="root",
        host="localhost",
        password="" ,
        database="my_expenses")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users(name TEXT,username TEXT,password TEXT)")

    
def connect1():
    # global conn,cur
    conn=pq.connect(
        user="root",
        host="localhost",
        password="" ,
        database="my_expenses")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS expensetable(id INTEGER PRIMARY KEY AUTO_INCREMENT,itemname TEXT,date TEXT,cost TEXT)")



def viewallusers():
    conn=pq.connect(user="root",host="localhost",password="" ,database="my_expenses")
    cur=conn.cursor()
    cur.execute("SELECT * FROM users")
    rows=cur.fetchall()
    conn.commit()
    conn.close()   
    return rows

def adduser(name,username,password):
    conn=pq.connect(user="root",host="localhost",password="" ,database="my_expenses")
    cur=conn.cursor()
    cur.execute("INSERT INTO users VALUES(%s,%s,%s)",(name,username,password))
    conn.commit()
    conn.close()

def deleteallusers():
    conn=pq.connect(user="root",host="localhost",password="" ,database="my_expenses")
    cur=conn.cursor()
    cur.execute("DELETE FROM users")
    conn.commit()
    conn.close()
    messagebox.showinfo('Successful', 'All users deleted')

def checkuser(username,password):
    conn=pq.connect(user="root",host="localhost",password="" ,database="my_expenses")
    cur=conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=%s AND password=%s",(username,password))
    result=cur.fetchone()
    return result

def getusername(username,password):
    conn=pq.connect(user="root",host="localhost",password="" ,database="my_expenses")
    cur=conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=%s AND password=%s",(username,password))
    result=cur.fetchone()
    global profilename
    if result!=None:
        profilename=result[0]
        




