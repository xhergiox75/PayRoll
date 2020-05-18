from tkinter import*
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import locale
locale.setlocale(locale.LC_ALL, 'en_US')

import random
import time
import datetime

#from time import strftime *

"""payroll= Tk()
payroll.geometry('1350x650+0+0')
payroll.title('Payroll Management')"""

def Exit():
    Payroll.destroy()

def Reset():
    Employee.set('')
    Address.set('')
    Reference.set('')
    EmployerName.set('')
    BasicSalary.set('')
    OverTime.set('')
    GrossPay.set('')


def MonthSalary():
  #  BS= float(BasicSalary.get())
   # CW= float(City.get())
    OT= float(OverTime.get())

#--------------------------------------------------------
#Connecting App to database 
def update ():

    Id=e1.get();
    Employee=e2.get();
    BasicSalary=e3.get();
    OverTime=e4.get();
    
    if (Id==""or Employee=="" ):
        MessageBox.showinfo("insert status","all fields are required")
    else:
        con=mysql.connect(host="localhost",user="root", password="",database="python-tkinter")
        cur=con.cursor()
        
        sql="update student set Employee='%s',BasicSalary='%s',OverTime='%s' where Id='%s'"%(Employee,BasicSalary,OverTime,Id)
      
        cur.execute(sql)
        
        con.commit();
        MessageBox.showinfo('update status','updated successfully');
        con.close()


def clear():
    Id.set('')
    Employee.set('')
    BasicSalary.set('')
    OverTime.set('')
    GrossPay.set('')
    e1.configure(state='normal')



root=Tk()
root.geometry('600x300')
root.title("python+tkinter+mysql")

def Exit():
    root.destroy()

Id=StringVar()
Employee=StringVar()
BasicSalary=IntVar()
OverTime=IntVar()
GrossPay=IntVar()



def search():
    
    try:
        con=mysql.connect(host="localhost",user="root", password="",database="python-tkinter")
        cur=con.cursor()
        
        sql="select *  from student where Id='%s'"%Id.get()
        #sql="Select Employee, CONCAT('$',FORMAT(BasicSalary,OverTime,GrossPay 2)) As BasicSalary,OverTime,GrossPay from student where id='%s'"%Id.get() 
        #concat('$', format(sum(price), 2))
              
        cur.execute(sql)
        result=cur.fetchone()
        Employee.set(result[1])
        BasicSalary.set(result[2])
        OverTime.set(result[3])
        #Gr=Grosspay.format(:.2) 
        GrossPay.set(result[4])


        e1.configure(state='disabled')
        #con.commit();
    except:
            MessageBox.showinfo('','No suchdata')
          
            con.close();


def Sum(): 

    Id=e1.get();
    Employee=e2.get();
    BasicSalary=e3.get();
    OverTime=e4.get();  
    if (Id==""or Employee=="" ):
        MessageBox.showinfo("insert status","all fields are required")
    else:
        con=mysql.connect(host="localhost",user="root", password="",database="python-tkinter")
        cur=con.cursor()
   
        sql="UPDATE student SET GrossPay=BasicSalary+OverTime "
        #where Id='%s'"%(Employee,BasicSalary,OverTime,Id)      
    
        cur.execute(sql)
        #result=cur.fetchone()
        #con.commit('commit')
        cur.execute('commit');
        MessageBox.showinfo('update status','updated successfully');
        con.close()

#sum()

#SELECT id, name, class,( social + science + math) AS total FROM `student3`
#SELECT Id,Employee,(BasicSalary+OverTime) As GrossPay FROM

l1=Label(root,text='Id')
e1=Entry(root,textvariable=Id)


l2=Label(root,text='Employee')
e2=Entry(root,textvariable=Employee)


l3=Label(root,text='Basic_Salary')
e3=Entry(root,locale.format("%d",locale.LC_ALL,'en_US'),textvariable=BasicSalary)

l4=Label(root,text='OverTime')
e4=Entry(root,textvariable=OverTime)

l5=Label(root,text='GrossPay')
e5=Entry(root,textvariable=GrossPay,state=DISABLED)

b1=Button(root,text='search',command=search)
b2=Button(root,text='clear',command=clear)
b3=Button(root,text='Exit',command=Exit)
b4=Button(root,text='update',command=update)
b5=Button(root,text='Wage',command=Sum)

l1.grid(row=1,column=0)
e1.grid(row=1,column=1)
l2.grid(row=2,column=0)
e2.grid(row=2,column=1)
l3.grid(row=3,column=0)
e3.grid(row=3,column=1)
l4.grid(row=4,column=0)
e4.grid(row=4,column=1)
l5.grid(row=5,column=0)
e5.grid(row=5,column=1)
#----------------------------------

b1.grid(row=5,column=2)
b2.grid(row=6,column=0)
b3.grid(row=7,column=0)
b4.grid(row=8,column=0)
b5.grid(row=9,column=0)

root.mainloop()