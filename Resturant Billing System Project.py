from tkinter import *
import random
import time
import sqlite3

#============ All Methods====================
def reset():
    rand.set("")
    FriedRice.set("")
    ChickenBiriyani.set("")
    MuttonBiriyani.set("")
    ChilliChicken.set("")
    ChickenManchurian.set("")
    Cost.set("")
    Tax.set("")
    Total.set("")

def Ref():
    fr=(int(FriedRice.get()))*150
    cb=(int(ChickenBiriyani.get()))*200 
    mb=(int(MuttonBiriyani.get()))*220
    cc=(int(ChilliChicken.get()))*210
    cm=(int(ChickenManchurian.get()))*230
    t=fr+cb+mb+cc+cm;
    Cost.set(str(t))
    tax=t*(.05)
    Tax.set(str(tax))
    gt=t+tax
    Total.set(str(gt))

def Store():
    fr=(int(FriedRice.get()))*150
    cb=(int(ChickenBiriyani.get()))*200 
    mb=(int(MuttonBiriyani.get()))*220
    cc=(int(ChilliChicken.get()))*210
    cm=(int(ChickenManchurian.get()))*230
    t=fr+cb+mb+cc+cm;
    tax=t*(.05)
    gt=t+tax
    studdata=[(fr,cb,mb,cc,cm,t,tax,gt),]
    c.executemany('insert into stud values(?,?,?,?,?,?,?,?)',studdata)
    mydb.commit()
    
def Display():
    disp=Tk()
       
    #------------------------

    disp.geometry("600x300+0+0")
    disp.title("Foodplaza Database")
    
    #----code for scroll bar
    scrollbar=Scrollbar(disp,orient="vertical")
    lb = Listbox(disp, width=50, height=20, yscrollcommand=scrollbar.set)
    scrollbar.config(command=lb.yview)
    scrollbar.pack(side="right", fill="y")
    lb.pack(side="left",fill="both", expand=True)
    #----alternate code for scroll bar
    record=1
    myrow=5
    mycol=5
    for row in mydb.execute('select * from stud'):
        lb.insert("end","----------------------------------------------------------------------------------------------------------------------------")
        lb.insert("end","Record Number : %s" %record, "Fried Rice : %s"  %row[0],"Chicken Biriyani : %s" %row[1],"Mutton Biriyani : %s" %row[2],"Chilli Chicken: %s" %row[3],"Chicken Manchurian : %s" %row[4],"Total Cost : %s" %row[5],"Tax : %s" %row[6],"Grand Total : %s" %row[7])
        lb.insert("end","----------------------------------------------------------------------------------------------------------------------------")
        record=record+1
    disp.mainloop()

def Print():
    disp1=Tk()
    disp1.geometry("400x400+0+0")
    disp1.title("Bill Details")
    
    fr=(int(FriedRice.get()))*150
    cb=(int(ChickenBiriyani.get()))*200
    mb=(int(MuttonBiriyani.get()))*220
    cc=(int(ChilliChicken.get()))*210
    cm=(int(ChickenManchurian.get()))*230
    
    lb1=Listbox(disp1,width=30, height=60)
    lb1.pack(side="left",fill="both",expand=True)
    lb1.insert("end","                                             EXPRESS FOODPLAZA")
    lb1.insert("end","                                                      KOLAGHAT")
    lb1.insert("end","                                                EAST MIDNAPORE")
    lb1.insert("end","----------------------------------------------------------------------------------")
    lb1.insert("end","                                                       RECEIPT")
    lb1.insert("end","----------------------------------------------------------------------------------")
    lb1.insert("end","   ITEM NAME                               RATE                QTY              AMT")
    lb1.insert("end","----------------------------------------------------------------------------------")
    
    a="   FRIED RICE :                               150"+"                      "+FriedRice.get()+"                   "
    a+=str(fr)
    lb1.insert("end","%s" %a)
    
    a="   CHICKEN BIRIYANI :                 200"+"                      "+ChickenBiriyani.get()+"                   "
    a+=str(cb)
    lb1.insert("end","%s" %a)
    
    a="   MUTTON BIRIYANI :                 220"+"                      "+MuttonBiriyani.get()+"                   "
    a+=str(mb)
    lb1.insert("end","%s" %a)

    a="   CHILLI CHICKEN :                     210"+"                      "+ChilliChicken.get()+"                   "
    a+=str(cc)
    lb1.insert("end","%s" %a)

    a="   CHICKEN MANCHURIAN :      230"+"                      "+ChickenManchurian.get()+"                   "
    a+=str(cm)
    lb1.insert("end","%s" %a)

    lb1.insert("end","----------------------------------------------------------------------------------")
    lb1.insert("end","   TOTAL AMOUNT : %s" %Cost.get(),"   TAX AMOUNT : %s" % Tax.get(),"   AMOUNT TO BE PAYED : %s" % Total.get())
    lb1.insert("end","----------------------------------------------------------------------------------")
    lb1.insert("end","                                             HAVE A GOOD DAY")
    lb1.insert("end","                                      THANK YOU, VISIT AGAIN ")
    
#=================END=======================

#====== Creating window ====================
root=Tk()
root.geometry("1600x800+0+0")
root.title("Resturant Billing System")
#------------------------------------------------------------------
mydb=sqlite3.connect("resturant.db")
c=mydb.cursor()
'''
c.execute('create table stud(fr int,cb int,mb int,cc int,cm int,total decimal(7,2),tax decimal(7,2),gt decimal(7,2))')
mydb.commit()
'''
#======= creating Frames ====================
Tops=Frame(root,width=1600,height=50)
Tops.pack(side=TOP)
f1=Frame(root,width=600,height=70)
f1.pack(side=LEFT)
f2=Frame(root,width=800,height=70)
f2.pack(side=RIGHT)
f3=Frame(f2,width=400,height=70)
f3.pack(side=LEFT)
f4=Frame(f2,width=400,height=70)
f4.pack(side=RIGHT)

#===================END==================

#=============== Adding Time==============================
localtime=time.asctime(time.localtime(time.time() ) )
#=============== END ======================

#=================== Info 1(HEADINGS)==========================
lblInfo=Label(Tops,font=('Arial',50,'bold'),text='Express Foodplaza',fg='steel blue',bd=10,
                          anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo=Label(Tops,font=('Arial',20,'bold'),text=localtime,fg='steel blue',bd=10,
                          anchor='w')
lblInfo.grid(row=1,column=0)
#=================== END ===========================

#======================= ADD MENUCARD ================================================
label1=Label(f3,text="MENU CARD ",font=('Arial',20,'bold'),fg='RED',bd=16,anchor='w')
label1.grid(row=1,column=1)
label2=Label(f3,text="Fried Rice = 150", font =('Arial',15,'bold'),fg='BLACK',bd=16,anchor='w')
label2.grid(row=2,column=1)
label3=Label(f3,text="Chicken Biriyani = 200", font =('Arial',15,'bold'),fg='BLACK',bd=16,anchor='w')
label3.grid(row=3,column=1)
label4=Label(f3,text="Mutton Biriyani = 220", font =('Arial',15,'bold'),fg='BLACK',bd=16,anchor='w')
label4.grid(row=4,column=1)
label6=Label(f3,text="Chilli Chicken = 210", font =('Arial',15,'bold'),fg='BLACK',bd=16,anchor='w')
label6.grid(row=5,column=1)
label7=Label(f3,text="Chiken Manchurian = 230", font =('Arial',15,'bold'),fg='BLACK',bd=16,anchor='w')
label7.grid(row=6,column=1)
label9=Label(f3,text="||", fg='GREEN',bd=16)
label9.grid(row=1,column=2)
label10=Label(f3,text="||",fg='GREEN',bd=16)
label10.grid(row=2,column=2)
label11=Label(f3,text="||", fg='GREEN',bd=16)
label11.grid(row=3,column=2)
label12=Label(f3,text="||",fg='GREEN',bd=16)
label12.grid(row=4,column=2)
label13=Label(f3,text="||", fg='GREEN',bd=16)
label13.grid(row=5,column=2)
label14=Label(f3,text="||",fg='GREEN',bd=16)
label14.grid(row=6,column=2)
label17=Label(f3,text="||", fg='GREEN',bd=16)
label17.grid(row=1,column=0)
label18=Label(f3,text="||",fg='GREEN',bd=16)
label18.grid(row=2,column=0)
label19=Label(f3,text="||", fg='GREEN',bd=16)
label19.grid(row=3,column=0)
label20=Label(f3,text="||",fg='BLACK',bd=16)
label20.grid(row=4,column=0)
label21=Label(f3,text="||", fg='GREEN',bd=16)
label21.grid(row=5,column=0)
label22=Label(f3,text="||",fg='GREEN',bd=16)
label22.grid(row=6,column=0)
#=====================END MENUCARD ============================

#=====================Add CALCULATOR===================================

#Accept value from key
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

#------------END----------------

#Method for clear operation
def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")
#---------------END----------------

#Method for equals operation
def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
#-------------END-------------------

#Variable to accept the value
operator=""
text_Input=StringVar()
#---------------END------------------

#Creating Display Unit
txtDisplay=Entry(f4,font=('Arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg="powder blue",justify="right").grid(columnspan=4)
#---------------------END---------------------

#Creating button 7,8,9,+ -------------------
btn7=Button(f4,padx=16,pady=16,bd=8,fg="black",font=('Arial',20,'bold'),text="7",bg="powder blue",command=lambda:btnClick(7)).grid(row=1,column=0)
btn8=Button(f4,padx=16,pady=16,bd=8,fg="black",font=('Arial',20,'bold'),text="8",bg="powder blue",command=lambda:btnClick(8)).grid(row=1,column=1)
btn9=Button(f4,padx=16,pady=16,bd=8,fg="black",font=('Arial',20,'bold'),text="9",bg="powder blue",command=lambda:btnClick(9)).grid(row=1,column=2)
Addition=Button(f4,padx=16,pady=16,bd=8,fg="black",font=('Arial',20,'bold'),text="+",bg="powder blue",command=lambda:btnClick("+")).grid(row=1,column=3)
#---------------END-----------------

#Creating button 4,5,6,- -------------------
btn4=Button(f4,padx=16,pady=16,bd=8,fg="black",font=('Arial',20,'bold'),text="4",bg="powder blue",command=lambda:btnClick(4)).grid(row=2,column=0)
btn5=Button(f4,padx=16,pady=16,bd=8,fg="black",font=('Arial',20,'bold'),text="5",bg="powder blue",command=lambda:btnClick(5)).grid(row=2,column=1)
btn6=Button(f4,padx=16,pady=16,bd=8,fg="black",font=('Arial',20,'bold'),text="6",bg="powder blue",command=lambda:btnClick(6)).grid(row=2,column=2)
Subtract=Button(f4,padx=16,pady=16,bd=8,fg="black",font=('Arial',20,'bold'),text="-",bg="powder blue",command=lambda:btnClick("-")).grid(row=2,column=3)
#--------------END---------------------

#Creating button 1,2,3,*---------------------------
btn1=Button(f4,padx=16,pady=16,bd=8,fg="black",font=('Arial',20,'bold'),text="1",bg="powder blue",command=lambda:btnClick(1)).grid(row=3,column=0)
btn2=Button(f4,padx=16,pady=16,bd=8,fg="black",font=('Arial',20,'bold'),text="2",bg="powder blue",command=lambda:btnClick(2)).grid(row=3,column=1)
btn3=Button(f4,padx=16,pady=16,bd=8,fg="black",font=('Arial',20,'bold'),text="3",bg="powder blue",command=lambda:btnClick(3)).grid(row=3,column=2)
Multi=Button(f4,padx=16,pady=16,bd=8,fg="black",font=('Arial',20,'bold'),text="*",bg="powder blue",command=lambda:btnClick("*")).grid(row=3,column=3)
#------------------END------------------

#Creating button 0,c,=,/----------------
btn0=Button(f4,padx=16,pady=16,bd=8,fg="black",font=('Arial',20,'bold'),text="0",bg="powder blue",command=lambda:btnClick(0)).grid(row=4,column=0)
btnClear=Button(f4,padx=16,pady=16,bd=8,fg="black",font=('Arial',20,'bold'),text="C",bg="powder blue",command=btnClearDisplay).grid(row=4,column=1)
btnEquals=Button(f4,padx=16,pady=16,bd=8,fg="black",font=('Arial',20,'bold'),text="=",bg="powder blue",command=btnEqualsInput).grid(row=4,column=2)
Div=Button(f4,padx=16,pady=16,bd=8,fg="black",font=('Arial',20,'bold'),text="/",bg="powder blue",command=lambda:btnClick("/")).grid(row=4,column=3)
#------------------END----------------------

#======================= END CALCULATOR ======================================================

#======================= INFO 2===================================================
rand=StringVar()
ChickenBiriyani=StringVar()
MuttonBiriyani=StringVar()
ChilliChicken=StringVar()
ChickenManchurian=StringVar()
FriedRice=StringVar()
Cost=StringVar()
Tax=StringVar()
Total=StringVar()

l1=Label(f1,font=('arial',15,'bold'),text='Fried Rice',bd=16,anchor='w')
l1.grid(row=0,column=0)
e1=Entry(f1,font=('arial',16,'bold'),textvariable=FriedRice,bd=10,insertwidth=4,
                 justify='right')
e1.grid(row=0,column=1)

l2=Label(f1,font=('arial',16,'bold'),text='Chicken Biriyani',bd=16,anchor='w')
l2.grid(row=1,column=0)
e2=Entry(f1,font=('arial',16,'bold'),textvariable=ChickenBiriyani,bd=10,insertwidth=3,
            justify='right')
e2.grid(row=1,column=1)

l3=Label(f1,font=('arial',16,'bold'),text='Mutton Biriyani',bd=16,anchor='w')
l3.grid(row=2,column=0)
e3=Entry(f1,font=('arial',16,'bold'),textvariable=MuttonBiriyani,bd=10,insertwidth=3,
            justify='right')
e3.grid(row=2,column=1)

l4=Label(f1,font=('arial',15,'bold'),text='Chilli Chicken',bd=16,anchor='w')
l4.grid(row=3,column=0)
e4=Entry(f1,font=('arial',16,'bold'),textvariable=ChilliChicken,bd=10,insertwidth=3,
               justify='right')
e4.grid(row=3,column=1)

l5=Label(f1,font=('arial',16,'bold'),text='Chicken Manchurian',bd=16,anchor='w')
l5.grid(row=4,column=0)
e5=Entry(f1,font=('arial',16,'bold'),textvariable=ChickenManchurian,bd=10,insertwidth=3,
            justify='right')
e5.grid(row=4,column=1)

#=================================END=================================================

#===========================INFO 3================================================
lblCost=Label(f1,font=('arial',16,'bold'),text='Total Cost',bd=16,anchor='w')
lblCost.grid(row=5,column=0)
txtCost=Entry(f1,font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=3,
                 justify='right')
txtCost.grid(row=5,column=1)

lblTax=Label(f1,font=('arial',16,'bold'),text='Tax',bd=16,anchor='w')
lblTax.grid(row=6,column=0)
txtTax=Entry(f1,font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=3,
                 justify='right')
txtTax.grid(row=6,column=1)

lblTotal=Label(f1,font=('arial',16,'bold'),text='Grand Total',bd=16,anchor='w')
lblTotal.grid(row=7,column=0)
txtTotal=Entry(f1,font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=3,
                 justify='right')
txtTotal.grid(row=7,column=1)
#======================================END=======================================

#============== Add Buttons================================================
btnqExit=Button(f1,bd=16,fg='black',font=('arial',16,'bold'),width=5,text="Exit",
                bg="powder blue",command=root.destroy)
btnqExit.grid(row=1,column=3)

btnClear=Button(f1,bd=16,fg='black',font=('arial',16,'bold'),width=5,text="Reset",
                bg="powder blue",command=reset)
btnClear.grid(row=2,column=3)

btnTotal=Button(f1,bd=16,fg='black',font=('arial',16,'bold'),width=5,text="Total",
                bg="powder blue",command=Ref)
btnTotal.grid(row=3,column=3)

btnSave=Button(f1,bd=16,fg='black',font=('arial',16,'bold'),width=5,text="Save",
                bg="powder blue",command=Store)
btnSave.grid(row=5,column=3)

btnDisp=Button(f1,bd=16,fg='black',font=('arial',16,'bold'),width=5,text="Display",
                bg="powder blue",command=Display)
btnDisp.grid(row=6,column=3)

btnGen=Button(f1,bd=16,fg='black',font=('arial',16,'bold'),width=5,text="Print",
                bg="powder blue",command=Print)
btnGen.grid(row=7,column=3)


root.mainloop()
