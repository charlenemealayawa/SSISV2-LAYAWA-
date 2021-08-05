from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as font
import os
import sqlite3

root = Tk()
root.geometry("1360x700")
root.title('SSISV2')
root.state('zoomed')
root.resizable(False, False)
positionRight = int((root.winfo_screenwidth()/2 - 688))
positionDown = int((root.winfo_screenheight()/2 - 386))
root.geometry("+{}+{}".format(positionRight, positionDown))



Frame1 = LabelFrame(root, bg="white", highlightbackground="gray26",highlightthickness=4)
Frame1.place(x=8,y=90,height=320,width=1350)

Frame2 = LabelFrame(root, bg="white",highlightbackground="gray26",highlightthickness=4)
Frame2.place(x=8,y=430,height=310,width=1350)



Label(root, text="STUDENT INFORMATION SYSTEM", font = ('Britannic Bold', 50, 'bold'),fg="black", width=32).pack(side=TOP,fill=X)   


conn = sqlite3.connect('studentinformation.db')
c= conn.cursor()
conn.execute("PRAGMA foreign_keys = ON;"); 

c.execute("""CREATE TABLE IF NOT EXISTS COURSEINFO(
        course_code text PRIMARY KEY,
        course_name text
        )""")


c.execute("""CREATE TABLE IF NOT EXISTS STUDENTINFO(
        ID_number text PRIMARY KEY,
        name text,
        course_code varchar(10),
        year_level text,
        gender text,
        FOREIGN KEY (course_code)
            REFERENCES COURSEINFO(course_code)
                ON DELETE CASCADE
        )""")

conn.commit()



#============================================TREEVIEW==================================================================================#

# FRAME 1


style = ttk.Style(Frame1)
style.configure("Treeview",
    background = "silver",
    foreground = "black",
    fieldbackground = "silver"
    )
style.map('Treeview',background=[('selected','blue')])

tree_frame1 = Frame(Frame1)
tree_frame1.place(x=1310,y=30,width = 20, height=270)

tree_scroll1 = Scrollbar(tree_frame1)
tree_scroll1.pack(side=RIGHT , fill = Y)


my_tree = ttk.Treeview(Frame1, height=20, yscrollcommand=tree_scroll1.set)
my_tree.grid(row=1, column=0, columnspan=6, padx=12, pady=10)

tree_scroll1.config(command=my_tree.yview)

         
my_tree['columns'] = ("ID number", "Name","Course","Year Level","Gender")

my_tree.column('#0',width=0, stretch=NO)
my_tree.column("ID number", anchor=CENTER, width=90)
my_tree.column("Name", anchor=CENTER, width=150)
my_tree.column("Course", anchor=CENTER, width=50)
my_tree.column("Year Level", anchor=CENTER, width=20)
my_tree.column("Gender", anchor=CENTER, width=50)

my_tree.heading("ID number", text="ID number", anchor=CENTER)
my_tree.heading("Name", text="Name", anchor=CENTER)
my_tree.heading("Course", text="Course", anchor=CENTER)
my_tree.heading("Year Level", text="Year Level", anchor=CENTER)
my_tree.heading("Gender", text="Gender", anchor=CENTER)

my_tree.place(x=10,y=30,height=270, width=1300)







# FRAME 2


style = ttk.Style(Frame2)
style.configure("Treeview",
    background = "silver",
    foreground = "black",
    fieldbackground = "silver"
    )
style.map('Treeview',background=[('selected','blue')])

 



tree_frame2 = Frame(Frame2)
tree_frame2.place(x=1310,y=30,width = 20, height=260)

tree_scroll2 = Scrollbar(tree_frame2)
tree_scroll2.pack(side=RIGHT , fill = Y)


my_tree1 = ttk.Treeview(Frame2, height=20, yscrollcommand=tree_scroll2.set)
my_tree1.grid(row=1, column=0, columnspan=6, padx=12, pady=10)

tree_scroll2.config(command=my_tree1.yview)

my_tree1['columns'] = ("Course Code","Course Name")

my_tree1.column('#0',width=0, stretch=NO)
my_tree1.column("Course Code", anchor=CENTER, width=90)
my_tree1.column("Course Name", anchor=CENTER, width=90)

my_tree1.heading("Course Code", text="Course Code", anchor=CENTER)
my_tree1.heading("Course Name", text="Course Name", anchor=CENTER)

my_tree1.place(x=10,y=30,height=260, width=1300)



#============================================FRAME 1===========================================================================#
STD_ID = StringVar()
STD_name = StringVar()       
STD_yearLevel = StringVar()
STD_gender = StringVar()
STD_course = StringVar()
SearchBar_Var1 = StringVar()

Lccode = StringVar()
Lcname = StringVar()

def viewTRV():

    conn = sqlite3.connect('studentinformation.db')
    c= conn.cursor()
    c.execute("SELECT * FROM STUDENTINFO")
    records = c.fetchall()

    global count
    count=0
    for record in records:
        my_tree.insert(parent='',index='end', iid=count, values = (record))
        count += 1
    conn.commit()

def addstudent():
    win=Toplevel()
    win.title('ADD STUDENT')
    win.geometry("550x300")
    win.resizable(False,False)
    win.configure(background="white")

    L_ID = Label(win, font=('Apple SD Gothic Neo',13, 'bold'),text="Student ID:  ", padx=2, pady=2, bg ="white", fg="black")
    L_ID.grid(row=0, column=0, sticky=W)
    E_ID = Entry(win, font=('Apple SD Gothic Neo',13), width=25)
    E_ID.grid(row=0, column=1, pady=8)
    
    L_name = Label(win, font=('Apple SD Gothic Neo',13, 'bold'),text="Name", padx=2, pady=2,  bg ="white", fg="black")
    L_name.grid(row=1, column=0, sticky=W)
    E_name = Entry(win, font=('Apple SD Gothic Neo',13), width=25)
    E_name.grid(row=1, column=1, pady=8)
    
    L_course = Label(win, font=('Apple SD Gothic Neo',13, 'bold'),text="Course", padx=2, pady=2, bg ="white", fg="black")
    L_course.grid(row=2, column=0, sticky=W)
    l_course = ttk.Combobox(win, font=('Apple SD Gothic Neo',13),state='readonly', width=23)
    E_course = Entry(win, font=('Apple SD Gothic Neo',13), width=25)
    E_course.grid(row=2, column=1, pady=8)
    
    L_year = Label(win,text="Year Level ", padx=2, pady=2, font=('Apple SD Gothic Neo',13, 'bold'), bg ="white", fg="black")
    L_year.grid(row=3, column=0, sticky=W)
    ylevel = ttk.Combobox(win, font=('Apple SD Gothic Neo',13),state='readonly', width=23)
    ylevel['values']=('','1ST-Year','2ND-Year','3RD-Year','4TH-Year')
    ylevel.current(0)
    ylevel.grid(row=3, column=1, pady=8)

    L_gender = Label(win, text="Gender ", padx=2, pady=2, font=('Apple SD Gothic Neo',13, 'bold'), bg ="white", fg="black")
    L_gender.grid(row=4, column=0, sticky=W)
    gender = ttk.Combobox(win, font=('Apple SD Gothic Neo',13),state='readonly', width=23)
    gender['values']=('','Female','Male')
    gender.current(0)
    gender.grid(row=4, column=1, pady=8)

    def addstudent():
        if E_ID.get() =="" or E_name.get() =="" or E_course.get()=="" or ylevel.get()=="" or gender.get()=="":
            messagebox.showinfo("Please Fill In the Box")
        else:
            c.execute("INSERT INTO STUDENTINFO(ID_number,name,course_code,year_level,gender) VALUES(?,?,?,?,?)",
                (E_ID.get(),E_name.get(),E_course.get(),ylevel.get(),gender.get()))
        win.destroy()
        conn.commit()
        Displaystudent()



                

    addButt=Button(win, text="ADD STUDENT", font=('Apple SD Gothic Neo',13, 'bold'), bg ="gray68", fg="black",command=addstudent)
    addButt.grid(row=5, column=0, columnspan=3,pady=8) 


def editstudent(index):
    def select(student):
        stdselect = my_tree.selection()
        for i in stdselect:
            c.execute("UPDATE STUDENTINFO SET ID_number=?, name=?,course_code=?,year_level=?,gender=?\
                WHERE ID_number = ?",(STD_ID.get(),STD_name.get(),STD_course.get(),STD_yearLevel.get(),STD_gender.get(),\
                my_tree.set(i,'#1')))
            win4.destroy()
            conn.commit()


            messagebox.showinfo("Student Data updated successfully")

            Displaystudent()

    data = my_tree.focus()
    values = my_tree.item(data,"values")

    win4=Toplevel()
    win4.title('EDIT STUDENT')
    win4.geometry("550x300")
    win4.resizable(False,False)
    win4.configure(background="white")



    student = my_tree.item(index)['values']

    L_ID = Label(win4, font=('Apple SD Gothic Neo',13, 'bold'),text="Student ID:  ", padx=2, pady=2, bg ="white", fg="black")
    L_ID.grid(row=0, column=0, sticky=W)
    E_ID = Entry(win4, font=('Apple SD Gothic Neo',13), width=25,textvariable= STD_ID)
    E_ID.grid(row=0, column=1, pady=8)
    
    L_name = Label(win4, font=('Apple SD Gothic Neo',13, 'bold'),text="Name", padx=2, pady=2,  bg ="white", fg="black")
    L_name.grid(row=1, column=0, sticky=W)
    E_name = Entry(win4, font=('Apple SD Gothic Neo',13), width=25,textvariable= STD_name)
    E_name.grid(row=1, column=1, pady=8)
    
    L_course = Label(win4, font=('Apple SD Gothic Neo',13, 'bold'),text="Course", padx=2, pady=2, bg ="white", fg="black")
    L_course.grid(row=2, column=0, sticky=W)
    E_course = Entry(win4, font=('Apple SD Gothic Neo',13), width=25,textvariable= STD_course)
    E_course.grid(row=2, column=1, pady=8)
    
    L_year = Label(win4,text="Year Level ", padx=2, pady=2, font=('Apple SD Gothic Neo',13, 'bold'), bg ="white", fg="black")
    L_year.grid(row=3, column=0, sticky=W)
    ylevel = ttk.Combobox(win4, font=('Apple SD Gothic Neo',13),state='readonly', width=23,textvariable=STD_yearLevel)
    ylevel['values']=('','1ST-Year','2ND-Year','3RD-Year','4TH-Year')
    ylevel.current(0)
    ylevel.grid(row=3, column=1, pady=8)

    L_gender = Label(win4, text="Gender ", padx=2, pady=2, font=('Apple SD Gothic Neo',13, 'bold'), bg ="white", fg="black")
    L_gender.grid(row=4, column=0, sticky=W)
    gender = ttk.Combobox(win4, font=('Apple SD Gothic Neo',13),state='readonly', width=23,textvariable=STD_gender)
    gender['values']=('','Female','Male')
    gender.current(0)
    gender.grid(row=4, column=1, pady=8)

    submit2 = Button(win4, text="UPDATE", command=lambda: select(student), font=('Apple SD Gothic Neo',15, 'bold'), bg="gray68", fg="black")
    submit2.grid(row=5, column=0, columnspan=3,pady=8)



    STD_ID.set(values[0])
    E_ID.config(state=DISABLED)
    STD_name.set(values[1])
    STD_course.set(values[2])
    STD_yearLevel.set(values[3])
    STD_gender.set(values[4])



def searchstudent():
    for i in my_tree.get_children():
        my_tree.delete(i)

    searchstud = search.get()
    conn=sqlite3.connect('studentinformation.db')
    c=conn.cursor()
    c.execute("SELECT * FROM STUDENTINFO")
    studentdata = c.fetchall()
    count=0
    for record in studentdata:
        if record[0].startswith(searchstud) or record[1].startswith(searchstud) or record[2].startswith(searchstud) or record[3].startswith(searchstud) or record[4].startswith(searchstud) :
            my_tree.insert(parent='',index='end',iid=count, values = (record))
        count += 1
    removesearchItem()



def Deletestudent():
    click = messagebox.askyesno(" DELETE DATA?")
    if click > 0:
        x = my_tree.selection()[0]
        ID_num = my_tree.item(x)['values'][0]
        conn = sqlite3.connect('studentinformation.db')
        c= conn.cursor()
        records = c.fetchall()
        for record in records:
            if ccode == record[0]:
                ccode=record[0]


        c.execute("DELETE FROM STUDENTINFO WHERE ID_number = ?",(ID_num,))
        conn.commit()
        my_tree.delete(x)
        Displaystudent()

def Deletemanystud():
        x = my_tree.selection()[0]
        ID_num = my_tree.item(x)['values'][0]
        conn = sqlite3.connect('studentinformation.db')
        c= conn.cursor()
        records = c.fetchall()
        for record in records:
            if ccode == record[0]:
                ccode=record[0]


        c.execute("DELETE FROM STUDENTINFO WHERE ID_number = ?",(ID_num,))
        conn.commit()
        my_tree.delete(x)    

def Displaystudent():

    my_tree.tag_configure('oddrow',background="white")
    my_tree.tag_configure('evenrow',background="silver")


    conn = sqlite3.connect('studentinformation.db')
    c= conn.cursor()
    c.execute("SELECT * FROM STUDENTINFO")
    data = c.fetchall() 

    for i in my_tree.get_children():
        my_tree.delete(i)
    global count    
    count=0
    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='',index='end',iid=count,text=f'{count + 1}', values = (record), tags=('evenrow',))
        
        else:
            my_tree.insert(parent='',index='end',iid=count,text=f'{count + 1}', values = (record), tags=('oddrow',))
        count += 1



    conn.commit()

Displaystudent()





#============================================FRAME 2===========================================================================#

SearchBar_Var = StringVar()


def add():
    win=Toplevel()
    win.title('ADD course')
    win.geometry("400x150")
    win.resizable(False,False)
    win.configure(background="white")

    win1 = Frame(win, bg="white")
    win1.grid()



    Lccode = Label(win1, font=('Apple SD Gothic Neo',13, 'bold'),text="Course code  ", padx=2, pady=2, bg ="white", fg="black")
    Lccode.grid(row=0, column=0, sticky=W)
    Eccode = Entry(win1, font=('Apple SD Gothic Neo',13), width=25)
    Eccode.grid(row=0, column=1, pady=8)
    
    Lcname = Label(win1, font=('Apple SD Gothic Neo',13, 'bold'),text="Course name", padx=2, pady=2,  bg ="white", fg="black")
    Lcname.grid(row=1, column=0, sticky=W)
    Ecname = Entry(win1, font=('Apple SD Gothic Neo',13), width=25)
    Ecname.grid(row=1, column=1, pady=8)

    def adddata():
        if Eccode.get() =="" or Ecname.get() =="":
            messagebox.showinfo("Please Fill In the Box")
        else:
            c.execute("INSERT INTO COURSEINFO(course_code,course_name) VALUES(?,?)",
                (Eccode.get(),Ecname.get()))
        win.destroy()



        conn.commit()
        Display()
        


    
    addc=Button(win1, text="ADD course", font=('Apple SD Gothic Neo', 15,'bold'),  bg ="gray68", fg="black",command = adddata)
    addc.grid(row=5, column=0, columnspan=3,pady=8) 

    Eccode.delete(0, END)
    Ecname.delete(0, END)
  
def edit(index):
    def selected(select):
        cselect = my_tree1.selection()
        for i in cselect:
            c.execute("UPDATE COURSEINFO SET course_name=?\
                            WHERE course_code=?",(Lcname.get(),Lccode.get(),))
            win2.destroy()
            conn.commit()
            messagebox.showinfo("Course updated successfully")
            Display()
    infoitem = my_tree1.focus()
    values = my_tree1.item(infoitem,"values")
    


    win2=Toplevel()
    win2.title('EDIT course')
    win2.geometry("400x150")
    win2.resizable(False,False)
    win2.configure(background="white")

    select = my_tree1.item(index)['values']

    win3 = Frame(win2, bg="white")
    win3.grid()



    Lccode1 = Label(win3, font=('Apple SD Gothic Neo',13, 'bold'),text="Course code  ", padx=2, pady=2, bg ="white", fg="black")
    Lccode1.grid(row=0, column=0, sticky=W)
    Eccode1 = Entry(win3, font=('Apple SD Gothic Neo',13), width=25,textvariable=Lccode)
    Eccode1.grid(row=0, column=1, pady=8)
    
    Lcname1 = Label(win3, font=('Apple SD Gothic Neo',13, 'bold'),text="Course name", padx=2, pady=2,  bg ="white", fg="black")
    Lcname1.grid(row=1, column=0, sticky=W)
    Ecname1 = Entry(win3, font=('Apple SD Gothic Neo',13), width=25,textvariable=Lcname)
    Ecname1.grid(row=1, column=1, pady=8)


    Submit1=Button(win3, text="UPDATE", command=lambda: selected(select), font=('Apple SD Gothic Neo',15, 'bold'), bg="gray68", fg="black")
    Submit1.grid(row=5, column=0, columnspan=3,pady=8)

    Lccode.set(values[0])
    Eccode1.config(state=DISABLED)
    Lcname.set(values[1])


def Delete():
    response = messagebox.askyesno(" DELETE DATA?")

    if response > 0:
        x = my_tree1.selection()[0]
        ccode = my_tree1.item(x)['values'][0]
        conn = sqlite3.connect('studentinformation.db')
        c= conn.cursor()
        records = c.fetchall()
        for record in records:
            if ccode == record[0]:
                ccode=record[0]


        c.execute("DELETE FROM COURSEINFO WHERE course_code = ?",(ccode,))
        conn.commit()
        my_tree1.delete(x)
        Deletemanystud()
        Displaystudent()
        Display()




def searchcourse():
    for i in my_tree1.get_children():
        my_tree1.delete(i)

    search = search2.get()
    conn = sqlite3.connect('studentinformation.db')
    c=conn.cursor()
    c.execute("SELECT* FROM COURSEINFO")
    records = c.fetchall()
    count=0
    for record in records:
        if record[0].startswith(search):
            my_tree1.insert(parent='',index='end',iid=count, values = (record))
        count += 1
        

    removesearchItem()




def Display():

    my_tree1.tag_configure('oddrow',background="white")
    my_tree1.tag_configure('evenrow',background="silver")


    conn = sqlite3.connect('studentinformation.db')
    c= conn.cursor()
    c.execute("SELECT * FROM COURSEINFO")
    records = c.fetchall() 

    for i in my_tree1.get_children():
        my_tree1.delete(i)
    global count    
    count=0
    for record in records:
        if count % 2 == 0:
            my_tree1.insert(parent='',index='end',iid=count,text=f'{count + 1}', values = (record), tags=('evenrow',))
        
        else:
            my_tree1.insert(parent='',index='end',iid=count,text=f'{count + 1}', values = (record), tags=('oddrow',))
        count += 1

    conn.commit()

Display()
#============================================BUTTONS==========================================================================#

#FRAME 1
search = Entry(Frame1,font=('Apple SD Gothic Neo',12), width=38,textvariable= SearchBar_Var1)
search.grid(row=0, column=0, padx = 10)

searchBut = Button(Frame1, text="SEARCH",font = ('Apple SD Gothic Neo', 9, 'bold'),fg="black",bg= "gray68", width=20,command=searchstudent)
searchBut.grid(row=0, column=1, padx = 20)
    
viewBut = Button(Frame1, text="VIEW ALL", font = ('Apple SD Gothic Neo', 9, 'bold'),fg="black",bg= "gray68",width=20,command=Displaystudent )
viewBut.grid(row=0, column=2, padx = 20)

addBut = Button(Frame1, text="ADD STUDENT", font = ('Apple SD Gothic Neo', 9, 'bold'),fg="black",bg= "gray68",width=20,command=addstudent )
addBut.grid(row=0, column=3, padx = 20)
    
editBut = Button(Frame1, text="EDIT", font = ('Apple SD Gothic Neo', 9, 'bold'),fg="black",bg= "gray68", width=20,command=lambda:editstudent(int(my_tree.focus())))
editBut.grid(row=0, column=4, padx = 20)
    
delete = Button(Frame1, text="DELETE",font = ('Apple SD Gothic Neo', 9, 'bold'),fg="black",bg= "gray68", width=20,command=Deletestudent)
delete.grid(row=0, column=5, padx = 20)


#FRAME 2 
search2 = Entry(Frame2,font=('Apple SD Gothic Neo',12), width=38,textvariable= SearchBar_Var)
search2.grid(row=0, column=0, padx = 10)

searchBut2 = Button(Frame2, text="SEARCH",font=('Apple SD Gothic Neo', 9,'bold'), bg="gray68", fg="black", width=20, command= searchcourse)
searchBut2.grid(row=0, column=1, padx = 20)
    
viewBut2 = Button(Frame2, text="VIEW ALL",font=('Apple SD Gothic Neo', 9,'bold'), bg="gray68", fg="black",width=20,command = Display)
viewBut2.grid(row=0, column=2, padx = 20)

addBut2 = Button(Frame2, text="ADD COURSE", font=('Apple SD Gothic Neo', 9,'bold'), bg="gray68", fg="black",width=20,command= add)
addBut2.grid(row=0, column=3, padx = 20)
    
editBut2 = Button(Frame2, text="EDIT",font=('Apple SD Gothic Neo', 9,'bold'), bg="gray68", fg="black", width=20,command=lambda:edit(int(my_tree1.focus())))
editBut2.grid(row=0, column=4, padx = 20)
    
delete2 = Button(Frame2, text="DELETE",font=('Apple SD Gothic Neo', 9,'bold'), bg="gray68", fg="black", width=20,command=Delete)
delete2.grid(row=0, column=5, padx = 20)



#=====
def removesearchItem():
    search2.delete(0,END)
    search.delete(0,END)







root.mainloop()
