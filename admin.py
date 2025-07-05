# ==================imports===================
import mysql.connector 
import re
import random
import string
import webbrowser
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from time import strftime
from datetime import date
from tkinter import scrolledtext as tkst
# ============================================

root = Tk()
root.geometry("1366x768")
root.title("Charity Manager(ADMIN)")
user = StringVar()
passwd = StringVar()
fname = StringVar()
lname = StringVar()


db = mysql.connector.connect(
host="localhost",
user="root",
password="Herobrinewastaken7"
)
cur = db.cursor()  
cur.execute("USE project")

def random_emp_id(stringLength):
    Digits = string.digits
    strr=''.join(random.choice(Digits) for i in range(stringLength-3))
    return ('EMP'+strr)

def valid_phone(phn):
    if re.match(r"[789]\d{9}$", phn):
        return True
    return False

def valid_aadhar(aad):
    if aad.isdigit() and len(aad)==12:
        return True
    return False


class login_page:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("CHarity Manager(ADMIN)")

        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/admin_login.png")
        self.label1.configure(image=self.img)
        

        self.entry1 = Entry(root)
        self.entry1.place(x=143, y=305, width=460, height=41)
        self.entry1.configure(font="-family {Poppins} -size 20")
        self.entry1.configure(relief="flat")
        self.entry1.configure(textvariable=user)

        self.entry2 = Entry(root)
        self.entry2.place(x=143, y=428, width=460, height=41)
        self.entry2.configure(font="-family {Poppins} -size 20")
        self.entry2.configure(relief="flat")
        self.entry2.configure(show="*")
        self.entry2.configure(textvariable=passwd)

        self.button1 = Button(root)
        self.button1.place(x=155, y=556, width=256, height=65)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#FF4D00")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#FF4D00")
        self.button1.configure(font="-family {Poppins SemiBold} -size 30")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""LOGIN""")
        self.button1.configure(command=self.login)

    def login(self, Event=None):
        username = user.get()
        password = passwd.get()

        db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Herobrinewastaken7"
        )
        cur = db.cursor()  
        cur.execute("USE project")
        cur.execute("SELECT designation FROM employee WHERE emp_id = %s AND password = %s", (username, password))
        results = cur.fetchall()
        print(results)
        if results:
            if results[0][0]=="ADMIN":
                messagebox.showinfo("Login Page", "The login is successful.")
                page1.entry1.delete(0, END)
                page1.entry2.delete(0, END)

                root.withdraw()
                global adm
                global page2
                adm = Toplevel()
                page2 = Admin_Page(adm)
                #page2.time()
                adm.protocol("WM_DELETE_WINDOW", exitt)
                adm.mainloop()
            else:
                messagebox.showerror("Oops!!", "You are not an admin.")

        else:
            messagebox.showerror("Error", "Incorrect username or password.")
            page1.entry2.delete(0, END)

    
def exitt():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=root)
    if sure == True:
        adm.destroy()
        root.destroy()

def inventory():
    adm.withdraw()
    global inv
    global page3
    inv = Toplevel()
    page3 = Inventory(inv)
    page3.time()
    inv.protocol("WM_DELETE_WINDOW", exitt)
    inv.mainloop()


def employee():
    adm.withdraw()
    global emp
    global page5
    emp = Toplevel()
    page5 = Employee(emp)
    page5.time()
    emp.protocol("WM_DELETE_WINDOW", exitt)
    emp.mainloop()


def invoices():
    adm.withdraw()
    global invoice
    invoice = Toplevel()
    page7 = Invoice(invoice)
    page7.time()
    invoice.protocol("WM_DELETE_WINDOW", exitt)
    invoice.mainloop()

def about():
    webbrowser.open_new("https://www.linkedin.com/in/aditya-acharya-78b7a7296/")


class Admin_Page:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("ADMIN Mode")

        self.label1 = Label(adm)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/admin.png")
        self.label1.configure(image=self.img)

        self.label2 =Label(adm)
        self.label2.place(x=894,y=311,width=427,height=30)
        self.label2.configure(font="-family {Poppins} -size 16")
        self.label2.configure(foreground="#000000")
        self.label2.configure(background="#ffffff")

        self.label3 =Label(adm)
        self.label3.place(x=894,y=381,width=427,height=30)
        self.label3.configure(font="-family {Poppins} -size 16")
        self.label3.configure(foreground="#000000")
        self.label3.configure(background="#ffffff")

        self.label4 =Label(adm)
        self.label4.place(x=894,y=457,width=427,height=30)
        self.label4.configure(font="-family {Poppins} -size 16")
        self.label4.configure(foreground="#000000")
        self.label4.configure(background="#ffffff")

        self.label5 =Label(adm)
        self.label5.place(x=894,y=533,width=427,height=30)
        self.label5.configure(font="-family {Poppins} -size 16")
        self.label5.configure(foreground="#000000")
        self.label5.configure(background="#ffffff")

        self.label6 =Label(adm)
        self.label6.place(x=894,y=609,width=427,height=30)
        self.label6.configure(font="-family {Poppins} -size 16")
        self.label6.configure(foreground="#000000")
        self.label6.configure(background="#ffffff")

        self.message = Label(adm)
        self.message.place(x=970, y=85, width=166, height=39)
        self.message.configure(font="-family {Poppins} -size 36")
        self.message.configure(foreground="#ffffff")
        self.message.configure(background="#6C6862")
        self.message.configure(text="""ADMIN""")
        self.message.configure(anchor="w")

        self.button1 = Button(adm)
        self.button1.place(x=1170, y=85, width=135, height=36)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 25")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Logout""")
        self.button1.configure(command=self.Logout)

        self.button2 = Button(adm)
        self.button2.place(x=78, y=203, width=248, height=73)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#ffffff")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#333333")
        self.button2.configure(background="#ffffff")
        self.button2.configure(font="-family {Poppins SemiBold} -size 30")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""CHARITIES""")
        self.button2.configure(command=inventory)

        self.button3 = Button(adm)
        self.button3.place(x=78, y=337, width=248, height=73)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#ffffff")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#333333")
        self.button3.configure(background="#ffffff")
        self.button3.configure(font="-family {Poppins SemiBold} -size 30")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""EMPLOYEES""")
        self.button3.configure(command=employee)


        self.button4 = Button(adm)
        self.button4.place(x=78, y=471, width=248, height=73)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#ffffff")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#333333")
        self.button4.configure(background="#ffffff")
        self.button4.configure(font="-family {Poppins SemiBold} -size 30")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""INVOICES""")
        self.button4.configure(command=invoices)


        self.button5 = Button(adm)
        self.button5.place(x=78, y=605, width=248, height=73)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#ffffff")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#333333")
        self.button5.configure(background="#ffffff")
        self.button5.configure(font="-family {Poppins SemiBold} -size 30")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""ABOUT""")
        self.button5.configure(command=about)

        self.button6 = Button(adm)
        self.button6.place(x=1192, y=235, width=103, height=29)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#CF1E14")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#CF1E14")
        self.button6.configure(font="-family {Poppins SemiBold} -size 16")
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""SEARCH""")
        self.button6.configure(command=self.searchcharity)

        self.entry1 = Entry(adm)
        self.entry1.place(x=894, y=233, width=271, height=32)
        self.entry1.configure(font="-family {Poppins} -size 20")
        self.entry1.configure(relief="flat")

    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?", parent=adm)
        if sure == True:
            adm.destroy()
            root.deiconify()
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)

    def searchcharity(self):
        ch=self.entry1.get()
        if(ch!=""): 
            cur.execute("SELECT charity from charitylist where charity ='{}'".format(ch))
            res=cur.fetchall()
            self.label2.configure(text=res[0][0])
            cur.execute("Select sum(donation) from donations where charity = '{}'".format(ch))
            total=cur.fetchall()
            self.label3.configure(text=total[0][0])
            cur.execute("select count(donation) from donations where charity='{}'".format(ch))
            count=cur.fetchall()
            self.label4.configure(text=count[0][0])
            cur.execute("select count(DISTINCT dnt_id)  from donations where charity='{}'".format(ch))
            no=cur.fetchall()
            self.label5.configure(text=no[0][0])
            cur.execute("select Head  from charitylist where charity='{}'".format(ch))
            head=cur.fetchall()
            self.label6.configure(text=head[0][0])
        else:
            messagebox.showerror("Oops!!", "Enter Correct Charity Name", parent=adm)



    

        


class Inventory:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Charity List")

        self.label1 = Label(inv)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/inventory.png")
        self.label1.configure(image=self.img)

        self.message = Label(inv)
        self.message.place(x=90, y=80, width=90, height=20)
        self.message.configure(font="-family {Poppins} -size 10")
        self.message.configure(foreground="#000000")
        self.message.configure(background="#ffffff")
        self.message.configure(text="""ADMIN""")
        self.message.configure(anchor="w")

        self.clock = Label(inv)
        self.clock.place(x=1190, y=67, width=120, height=33)
        self.clock.configure(font="-family {Poppins Light} -size 16")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.entry1 = Entry(inv)
        self.entry1.place(x=68, y=222, width=228, height=27)
        self.entry1.configure(font="-family {Poppins} -size 16")
        self.entry1.configure(relief="flat")

        self.button1 = Button(inv)
        self.button1.place(x=321, y=223, width=84, height=27)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 16")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Search""")
        self.button1.configure(command=self.search_product)

        self.button2 = Button(inv)
        self.button2.place(x=207, y=75, width=90, height=20)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#CF1E14")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Logout""")
        self.button2.configure(command=self.Logout)

        self.button3 = Button(inv)
        self.button3.place(x=96, y=327, width=290, height=29)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#CF1E14")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#CF1E14")
        self.button3.configure(font="-family {Poppins SemiBold} -size 12")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""ADD CHARITY""")
        self.button3.configure(command=self.add_product)

        self.button4 = Button(inv)
        self.button4.place(x=96, y=392, width=290, height=29)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#CF1E14")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#ffffff")
        self.button4.configure(background="#CF1E14")
        self.button4.configure(font="-family {Poppins SemiBold} -size 12")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""UPDATE CHARITY""")
        self.button4.configure(command=self.update_product)

        self.button5 = Button(inv)
        self.button5.place(x=96, y=455, width=290, height=29)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#CF1E14")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#ffffff")
        self.button5.configure(background="#CF1E14")
        self.button5.configure(font="-family {Poppins SemiBold} -size 12")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""DELETE CHARITY""")
        self.button5.configure(command=self.delete_product)

        self.button6 = Button(inv)
        self.button6.place(x=167, y=650, width=145, height=29)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#CF1E14")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#CF1E14")
        self.button6.configure(font="-family {Poppins SemiBold} -size 12")
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""EXIT""")
        self.button6.configure(command=self.Exit)

        self.scrollbarx = Scrollbar(inv, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(inv, orient=VERTICAL)
        self.tree = ttk.Treeview(inv)
        self.tree.place(relx=0.307, rely=0.203, width=880, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
        self.scrollbarx.place(x=421, y=702, width=861, height=23)

        self.tree.configure(
            columns=(
                "Charity ID",
                "Name",
                "Category",
                "Head",
                "City",
                "State",
                "Phone No.",
                "Status",
            )
        )

        self.tree.heading("Charity ID", text="Charity ID", anchor=W)
        self.tree.heading("Name", text="Name", anchor=W)
        self.tree.heading("Category", text="Category", anchor=W)
        self.tree.heading("Head", text="Head", anchor=W)
        self.tree.heading("City", text="City", anchor=W)
        self.tree.heading("State", text="State", anchor=W)
        self.tree.heading("Phone No.", text="Phone No.", anchor=W)
        self.tree.heading("Status", text="Status", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=80)
        self.tree.column("#2", stretch=NO, minwidth=0, width=260)
        self.tree.column("#3", stretch=NO, minwidth=0, width=100)
        self.tree.column("#4", stretch=NO, minwidth=0, width=120)
        self.tree.column("#5", stretch=NO, minwidth=0, width=80)
        self.tree.column("#6", stretch=NO, minwidth=0, width=80)
        self.tree.column("#7", stretch=NO, minwidth=0, width=80)
        self.tree.column("#8", stretch=NO, minwidth=0, width=100)

        self.DisplayData()

    def DisplayData(self):
    # Connect to the database
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Herobrinewastaken7",
                database="project"
            )
            cur = db.cursor()
        
            # Query to fetch updated data
            cur.execute("SELECT * FROM charitylist")
            rows = cur.fetchall()
        
            # Clear current treeview
            self.tree.delete(*self.tree.get_children())
        
            # Insert fetched rows into the treeview
            for row in rows:
                self.tree.insert("", "end", values=row)
        
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        

    def search_product(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        try:
            to_search = int(self.entry1.get())
        except ValueError:
            messagebox.showerror("Oops!!", "Invalid Product Id.", parent=inv)
        else:
            for search in val:
                if search==to_search:
                    self.tree.selection_set(val[val.index(search)-1])
                    self.tree.focus(val[val.index(search)-1])
                    messagebox.showinfo("Success!!", "Product ID: {} found.".format(self.entry1.get()), parent=inv)
                    break
            else: 
                messagebox.showerror("Oops!!", "Product ID: {} not found.".format(self.entry1.get()), parent=inv)
    
    sel = []
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def delete_product(self):
        val = []
        to_delete = []

        if len(self.sel)!=0:
            sure = messagebox.askyesno("Confirm", "Are you sure you want to delete selected products?", parent=inv)
            if sure == True:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)
                
                for j in range(len(val)):
                    if j%8==0:
                        to_delete.append(val[j])
                
                for k in to_delete:
                    
                    cur.execute("DELETE FROM charitylist WHERE char_id = %s"%(k))
                    db.commit()

                messagebox.showinfo("Success!!", "Products deleted from database.", parent=inv)
                self.sel.clear()
                self.tree.delete(*self.tree.get_children())
                self.DisplayData()
        else:
            messagebox.showerror("Error!!","Please select a product.", parent=inv)

    def update_product(self):
        if len(self.sel)==1:
            global p_update
            p_update = Toplevel()
            page9 = Update_Product(p_update)
            p_update.protocol("WM_DELETE_WINDOW", self.ex2)
            global valll
            valll = []
            for i in self.sel:
                for j in self.tree.item(i)["values"]:
                    valll.append(j)

            page9.entry1.insert(0, valll[1])
            page9.entry2.insert(0, valll[2])
            page9.entry3.insert(0, valll[4])
            page9.entry4.insert(0, valll[5])
            page9.entry6.insert(0, valll[3])
            page9.entry7.insert(0, valll[6])
            page9.entry8.insert(0, valll[7])


        elif len(self.sel)==0:
            messagebox.showerror("Error","Please choose a product to update.", parent=inv)
        else:
            messagebox.showerror("Error","Can only update one product at a time.", parent=inv)

        p_update.mainloop()

    

    def add_product(self):
        global p_add
        global page4
        p_add = Toplevel()
        page4 = add_product(p_add)
        p_add.mainloop()

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def Exit(self):
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=inv)
        if sure == True:
            inv.destroy()
            adm.deiconify()

    def ex2(self):
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=p_update)
        if sure == True:
            p_update.destroy()
            inv.deiconify()



    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            root.deiconify()
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)


class add_product:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Add Charity")

        self.label1 = Label(p_add)
        self.label1.place(x=0, y=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/add_product.png")
        self.label1.configure(image=self.img)

        self.entry1 = Entry(p_add)
        self.entry1.place(x=755, y=140, width=517, height=32)
        self.entry1.configure(font="-family {Poppins} -size 20")
        self.entry1.configure(relief="flat")

        self.entry2 = Entry(p_add)
        self.entry2.place(x=100, y=264, width=517, height=32)
        self.entry2.configure(font="-family {Poppins} -size 20")
        self.entry2.configure(relief="flat")

        self.r2 = p_add.register(self.testint)

        self.entry3 = Entry(p_add)
        self.entry3.place(x=100, y=402, width=517, height=32)
        self.entry3.configure(font="-family {Poppins} -size 20")
        self.entry3.configure(relief="flat")
       

        self.entry4 = Entry(p_add)
        self.entry4.place(x=100, y=534, width=517, height=32)
        self.entry4.configure(font="-family {Poppins} -size 20")
        self.entry4.configure(relief="flat")
       

        self.entry6 = Entry(p_add)
        self.entry6.place(x=755, y=271, width=517, height=32)
        self.entry6.configure(font="-family {Poppins} -size 20")
        self.entry6.configure(relief="flat")
       

        self.entry7 = Entry(p_add)
        self.entry7.place(x=755, y=402, width=517, height=32)
        self.entry7.configure(font="-family {Poppins} -size 20")
        self.entry7.configure(relief="flat")
       

        self.entry8 = Entry(p_add)
        self.entry8.place(x=755, y=535, width=517, height=32)
        self.entry8.configure(font="-family {Poppins} -size 20")
        self.entry8.configure(relief="flat")
        
       

        self.button1 = Button(p_add)
        self.button1.place(x=500, y=652, width=151, height=49)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 25")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""ADD""")
        self.button1.configure(command=self.add)

        self.button2 = Button(p_add)
        self.button2.place(x=726, y=652, width=151, height=49)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#CF1E14")
        self.button2.configure(font="-family {Poppins SemiBold} -size 25")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""CLEAR""")
        self.button2.configure(command=self.clearr)

    def add(self):
        id1 = random.randint(100,900)
        city = self.entry3.get()
        pcat = self.entry2.get()  
        state = self.entry4.get()  
        pname = self.entry1.get()  
        phead = self.entry6.get()  
        status = self.entry8.get()  
        phone = self.entry7.get()

        if pname.strip():
            if pcat.strip():
                if phead.strip():
                    if city.strip():
                        if valid_phone(phone):                        
                            if state.strip():
                                if status.strip():                                               
                                    
                                    try:
                                        db = mysql.connector.connect(
                                            host="localhost",
                                            user="root",
                                            password="Herobrinewastaken7",
                                            database="project"
                                        )
                                        cur = db.cursor()
                                        query = """
                                            INSERT INTO charitylist
                                            (char_id,charity,char_type,Head,city,state,phone,active_status)
                                            VALUES (%s, %s, %s, %s, %s, %s, %s,%s)
                                        """
                                        values = (id1,pname, pcat, phead, city, state, phone, status)
                                        cur.execute(query, values)
                                        db.commit()
                                        messagebox.showinfo("Success!", "Charity successfully added in list.", parent=p_add)                                    
                                        # Clear fields and refresh the display                                       
                                        Inventory.sel.clear()
                                        page3.tree.delete(*page3.tree.get_children())
                                        page3.DisplayData()
                                        p_add.destroy()
                                    except mysql.connector.Error as err:
                                        messagebox.showerror("Database Error", f"Error: {err}", parent=p_add)
                                    finally:
                                        db.close()
                                else:
                                    messagebox.showerror("Oops!", "Invalid Status.", parent=p_add)
                            else:
                                messagebox.showerror("Oops!", "Please enter State.", parent=p_add)
                        else:
                            messagebox.showerror("Oops!", "Please enter valid phone no.", parent=p_add)
                    else:
                        messagebox.showerror("Oops!", "Please enter City.", parent=p_add)
                else:
                    messagebox.showerror("Oops!", "Please enter product sub-category.", parent=p_add)
            else:
                messagebox.showerror("Oops!", "Please enter product category.", parent=p_add)
        else:
            messagebox.showerror("Oops!", "Please enter charity name", parent=p_add)

    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry6.delete(0, END)
        self.entry7.delete(0, END)
        self.entry8.delete(0, END)

    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    


class Update_Product:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Update Charity")

        self.label1 = Label(p_update)
        self.label1.place(x=0, y=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/update_product.png")
        self.label1.configure(image=self.img)

        self.entry1 = Entry(p_update)
        self.entry1.place(x=755, y=140, width=517, height=32)
        self.entry1.configure(font="-family {Poppins} -size 20")
        self.entry1.configure(relief="flat")

        self.entry2 = Entry(p_update)
        self.entry2.place(x=100, y=264, width=517, height=32)
        self.entry2.configure(font="-family {Poppins} -size 20")
        self.entry2.configure(relief="flat")

       

        self.entry3 = Entry(p_update)
        self.entry3.place(x=100, y=402, width=517, height=32)
        self.entry3.configure(font="-family {Poppins} -size 20")
        self.entry3.configure(relief="flat")
        
       

        self.entry4 = Entry(p_update)
        self.entry4.place(x=100, y=534, width=517, height=32)
        self.entry4.configure(font="-family {Poppins} -size 20")
        self.entry4.configure(relief="flat")
       

        self.entry6 = Entry(p_update)
        self.entry6.place(x=755, y=271, width=517, height=32)
        self.entry6.configure(font="-family {Poppins} -size 20")
        self.entry6.configure(relief="flat")
       

        self.entry7 = Entry(p_update)
        self.entry7.place(x=755, y=402, width=517, height=32)
        self.entry7.configure(font="-family {Poppins} -size 20")
        self.entry7.configure(relief="flat")
       

        self.entry8 = Entry(p_update)
        self.entry8.place(x=755, y=535, width=517, height=32)
        self.entry8.configure(font="-family {Poppins} -size 20")
        self.entry8.configure(relief="flat")
        
       

        self.button1 = Button(p_update)
        self.button1.place(x=500, y=652, width=151, height=49)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 25")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""UPDATE""")
        self.button1.configure(command=self.update)

        self.button2 = Button(p_update)
        self.button2.place(x=726, y=652, width=151, height=49)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#CF1E14")
        self.button2.configure(font="-family {Poppins SemiBold} -size 25")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""CLEAR""")
        self.button2.configure(command=self.clearr)


    def update(self):
        city = self.entry3.get()
        pcat = self.entry2.get()  
        state = self.entry4.get()  
        pname = self.entry1.get()  
        phead = self.entry6.get()  
        status = self.entry8.get()  
        phone = self.entry7.get()

        if pname.strip():
            if pcat.strip():
                if phead.strip():
                    if city.strip():
                        if valid_phone(phone):                        
                            if state.strip():
                                if status.strip():                                               
                                    product_id = valll[0]
                                    try:
                                        db = mysql.connector.connect(
                                            host="localhost",
                                            user="root",
                                            password="Herobrinewastaken7",
                                            database="project"
                                        )
                                        cur = db.cursor()
                                        query = """
                                            UPDATE charitylist
                                            SET charity = %s, char_type = %s, Head = %s, city = %s, state = %s, phone = %s, active_status = %s
                                            WHERE char_id = %s
                                        """
                                        values = (pname, pcat, phead, city, state, phone, status, product_id)
                                        cur.execute(query, values)
                                        db.commit()
                                        messagebox.showinfo("Success!", "Product successfully updated in inventory.", parent=p_update)
                                    
                                        # Clear fields and refresh the display
                                        valll.clear()
                                        Inventory.sel.clear()
                                        page3.tree.delete(*page3.tree.get_children())
                                        page3.DisplayData()
                                        p_update.destroy()
                                    except mysql.connector.Error as err:
                                        messagebox.showerror("Database Error", f"Error: {err}", parent=p_update)
                                    finally:
                                        db.close()
                                else:
                                    messagebox.showerror("Oops!", "Invalid Status.", parent=p_update)
                            else:
                                messagebox.showerror("Oops!", "Please enter State.", parent=p_update)
                        else:
                            messagebox.showerror("Oops!", "Please enter valid phone no.", parent=p_update)
                    else:
                        messagebox.showerror("Oops!", "Please enter City.", parent=p_update)
                else:
                    messagebox.showerror("Oops!", "Please enter product sub-category.", parent=p_update)
            else:
                messagebox.showerror("Oops!", "Please enter product category.", parent=p_update)
        else:
            messagebox.showerror("Oops!", "Please enter charity name", parent=p_update)
    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry6.delete(0, END)
        self.entry7.delete(0, END)
        self.entry8.delete(0, END)

    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    


class Employee:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Employee Management")

        self.label1 = Label(emp)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/employee.png")
        self.label1.configure(image=self.img)

        self.message = Label(emp)
        self.message.place(x=55,y=40, width=100, height=25)
        self.message.configure(font="-family {Poppins} -size 10")
        self.message.configure(foreground="#000000")
        self.message.configure(background="#ffffff")
        self.message.configure(text="""ADMIN""")
        self.message.configure(anchor="w")

        self.clock = Label(emp)
        self.clock.place(x=1131,y=71, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.entry1 = Entry(emp)
        self.entry1.place(relx=0.040, rely=0.286, width=240, height=28)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        self.button1 = Button(emp)
        self.button1.place(relx=0.229, rely=0.289, width=76, height=23)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 10")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Search""")
        self.button1.configure(command=self.search_emp)

        self.button2 = Button(emp)
        self.button2.place(relx=0.035, rely=0.106, width=76, height=23)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#CF1E14")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Logout""")
        self.button2.configure(command=self.Logout)

        self.button3 = Button(emp)
        self.button3.place(relx=0.052, rely=0.432, width=306, height=28)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#CF1E14")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#CF1E14")
        self.button3.configure(font="-family {Poppins SemiBold} -size 12")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""ADD EMPLOYEE""")
        self.button3.configure(command=self.add_emp)

        self.button4 = Button(emp)
        self.button4.place(relx=0.052, rely=0.5, width=306, height=28)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#CF1E14")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#ffffff")
        self.button4.configure(background="#CF1E14")
        self.button4.configure(font="-family {Poppins SemiBold} -size 12")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""UPDATE EMPLOYEE""")
        self.button4.configure(command=self.update_emp)

        self.button5 = Button(emp)
        self.button5.place(relx=0.052, rely=0.57, width=306, height=28)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#CF1E14")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#ffffff")
        self.button5.configure(background="#CF1E14")
        self.button5.configure(font="-family {Poppins SemiBold} -size 12")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""DELETE EMPLOYEE""")
        self.button5.configure(command=self.delete_emp)

        self.button6 = Button(emp)
        self.button6.place(relx=0.135, rely=0.885, width=76, height=23)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#CF1E14")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#CF1E14")
        self.button6.configure(font="-family {Poppins SemiBold} -size 12")
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""EXIT""")
        self.button6.configure(command=self.Exit)

        self.scrollbarx = Scrollbar(emp, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(emp, orient=VERTICAL)
        self.tree = ttk.Treeview(emp)
        self.tree.place(relx=0.307, rely=0.203, width=880, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
        self.scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)

        self.tree.configure(
            columns=(
                "Employee ID",
                "Employee Name",
                "Contact No.",
                "Address",
                "Aadhar No.",
                "Password",
                "Designation"
            )
        )

        self.tree.heading("Employee ID", text="Employee ID", anchor=W)
        self.tree.heading("Employee Name", text="Employee Name", anchor=W)
        self.tree.heading("Contact No.", text="Contact No.", anchor=W)
        self.tree.heading("Address", text="Address", anchor=W)
        self.tree.heading("Aadhar No.", text="Aadhar No.", anchor=W)
        self.tree.heading("Password", text="Password", anchor=W)
        self.tree.heading("Designation", text="Designation", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=80)
        self.tree.column("#2", stretch=NO, minwidth=0, width=260)
        self.tree.column("#3", stretch=NO, minwidth=0, width=100)
        self.tree.column("#4", stretch=NO, minwidth=0, width=198)
        self.tree.column("#5", stretch=NO, minwidth=0, width=80)
        self.tree.column("#6", stretch=NO, minwidth=0, width=80)
        self.tree.column("#7", stretch=NO, minwidth=0, width=80)

        self.DisplayData()

    def DisplayData(self):
        cur.execute("SELECT * FROM employee")
        fetch = cur.fetchall()
        for data in fetch:
            self.tree.insert("", "end", values=(data))

    def search_emp(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        to_search = self.entry1.get()
        for search in val:
            if search==to_search:
                self.tree.selection_set(val[val.index(search)-1])
                self.tree.focus(val[val.index(search)-1])
                messagebox.showinfo("Success!!", "Employee ID: {} found.".format(self.entry1.get()), parent=emp)
                break
        else: 
            messagebox.showerror("Oops!!", "Employee ID: {} not found.".format(self.entry1.get()), parent=emp)
    
    sel = []
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def delete_emp(self):
        val = []
        to_delete = []

        if len(self.sel)!=0:
            sure = messagebox.askyesno("Confirm", "Are you sure you want to delete selected employee(s)?", parent=emp)
            if sure == True:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)
                        
                
                for j in range(len(val)):
                    if j%7==0:
                        to_delete.append(val[j])
                        
                
                flag = 1

                for k in to_delete:
                    if k=="EMP0000":
                        flag = 0
                        break
                    else:
                        
                        delete = "DELETE FROM employee WHERE emp_id = %s"
                        cur.execute(delete,(k,))
                        db.commit()

                if flag==1:
                    messagebox.showinfo("Success!!", "Employee(s) deleted from database.", parent=emp)
                    self.sel.clear()
                    self.tree.delete(*self.tree.get_children())
                    self.DisplayData()
                else:
                    messagebox.showerror("Error!!","Cannot delete master admin.")
        else:
            messagebox.showerror("Error!!","Please select an employee.", parent=emp)

    def update_emp(self):
        
        if len(self.sel)==1:
            global e_update
            e_update = Toplevel()
            page8 = Update_Employee(e_update)
            
            e_update.protocol("WM_DELETE_WINDOW", self.ex2)
            global vall
            vall = []
            for i in self.sel:
                for j in self.tree.item(i)["values"]:
                    vall.append(j)
            
            page8.entry1.insert(0, vall[1])
            page8.entry2.insert(0, vall[2])
            page8.entry3.insert(0, vall[4])
            page8.entry4.insert(0, vall[6])
            page8.entry5.insert(0, vall[3])
            page8.entry6.insert(0, vall[5])
            e_update.mainloop()
        elif len(self.sel)==0:
            messagebox.showerror("Error","Please select an employee to update.")
        else:
            messagebox.showerror("Error","Can only update one employee at a time.")

        


    def add_emp(self):
        global e_add
        e_add = Toplevel()
        page6 = add_employee(e_add)
        page6.time()
        e_add.protocol("WM_DELETE_WINDOW", self.ex)
        e_add.mainloop()


    def ex(self):
        e_add.destroy()
        self.tree.delete(*self.tree.get_children())
        self.DisplayData()   

    def ex2(self):
        e_update.destroy()
        self.tree.delete(*self.tree.get_children())
        self.DisplayData()  



    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def Exit(self):
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=emp)
        if sure == True:
            emp.destroy()
            adm.deiconify()


    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            emp.destroy()
            root.deiconify()
            
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)


class add_employee:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Add Employee")

        self.label1 = Label(e_add)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/add_employee.png")
        self.label1.configure(image=self.img)

        self.r1 = e_add.register(self.testint)
        self.r2 = e_add.register(self.testchar)

        self.entry1 = Entry(e_add)
        self.entry1.place(x=97,y=269, width=520, height=31)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")
        

        self.entry2 = Entry(e_add)
        self.entry2.place(x=97,y=403, width=520, height=31)
        self.entry2.configure(font="-family {Poppins} -size 12")
        self.entry2.configure(relief="flat")
        self.entry2.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.entry3 = Entry(e_add)
        self.entry3.place(x=97,y=537, width=520, height=31)
        self.entry3.configure(font="-family {Poppins} -size 12")
        self.entry3.configure(relief="flat")
        self.entry3.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.entry4 = Entry(e_add)
        self.entry4.place(x=756,y=269, width=520, height=31)
        self.entry4.configure(font="-family {Poppins} -size 12")
        self.entry4.configure(relief="flat")
        self.entry4.configure(validate="key", validatecommand=(self.r2, "%P"))

        self.entry5 = Entry(e_add)
        self.entry5.place(x=756,y=403, width=520, height=31)
        self.entry5.configure(font="-family {Poppins} -size 12")
        self.entry5.configure(relief="flat")

        self.entry6 = Entry(e_add)
        self.entry6.place(x=756,y=537, width=520, height=31)
        self.entry6.configure(font="-family {Poppins} -size 12")
        self.entry6.configure(relief="flat")
        self.entry6.configure(show="*")

        self.button1 = Button(e_add)
        self.button1.place(x=928,y=654, width=170, height=48)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#FE4343")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#FE4343")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""ADD""")
        self.button1.configure(command=self.add)

        self.button2 = Button(e_add)
        self.button2.place(x=1141,y=654, width=170, height=48)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#FE4343")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#FE4343")
        self.button2.configure(font="-family {Poppins SemiBold} -size 14")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""CLEAR""")
        self.button2.configure(command=self.clearr)



    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def testchar(self, val):
        if val.isalpha():
            return True
        elif val == "":
            return True
        return False

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    
    def add(self):
        ename = self.entry1.get()
        econtact = self.entry2.get()
        eaddhar = self.entry3.get()
        edes = self.entry4.get()
        eadd = self.entry5.get()
        epass = self.entry6.get()

        if ename.strip():
            if valid_phone(econtact):
                if valid_aadhar(eaddhar):
                    if edes:
                        if eadd:
                            if epass:
                                emp_id = random_emp_id(7)
                                insert = (
                                "INSERT INTO employee (emp_id, name, contact_num, address, aadhar_num, password, designation) "
                                "VALUES (%s, %s, %s, %s, %s, %s, %s)"
                                )
                                cur.execute(insert, (emp_id, ename, econtact, eadd, eaddhar, epass, edes))  # %s placeholders used here
                                db.commit()
                                messagebox.showinfo("Success!!", "Employee ID: {} successfully added in database.".format(emp_id), parent=e_add)
                                page5.tree.delete(*page5.tree.get_children())
                                page5.DisplayData()
                                Employee.sel.clear()
                                e_add.destroy()
                                
                            else:
                                messagebox.showerror("Oops!", "Please enter a password.", parent=e_add)
                        else:
                            messagebox.showerror("Oops!", "Please enter address.", parent=e_add)
                    else:
                        messagebox.showerror("Oops!", "Please enter designation.", parent=e_add)
                else:
                    messagebox.showerror("Oops!", "Invalid Aadhar number.", parent=e_add)
            else:
                messagebox.showerror("Oops!", "Invalid phone number.", parent=e_add)
        else:
            messagebox.showerror("Oops!", "Please enter employee name.", parent=e_add)

    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)


class Update_Employee:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Update Employee")

        self.label1 = Label(e_update)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/update_employee.png")
        self.label1.configure(image=self.img)

        self.r1 = e_update.register(self.testint)
        self.r2 = e_update.register(self.testchar)

        self.entry1 = Entry(e_update)
        self.entry1.place(x=97,y=269, width=520, height=31)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")
        

        self.entry2 = Entry(e_update)
        self.entry2.place(x=97,y=403, width=520, height=31)
        self.entry2.configure(font="-family {Poppins} -size 12")
        self.entry2.configure(relief="flat")
        self.entry2.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.entry3 = Entry(e_update)
        self.entry3.place(x=97,y=537, width=520, height=31)
        self.entry3.configure(font="-family {Poppins} -size 12")
        self.entry3.configure(relief="flat")
        self.entry3.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.entry4 = Entry(e_update)
        self.entry4.place(x=756,y=269, width=520, height=31)
        self.entry4.configure(font="-family {Poppins} -size 12")
        self.entry4.configure(relief="flat")
        self.entry4.configure(validate="key", validatecommand=(self.r2, "%P"))

        self.entry5 = Entry(e_update)
        self.entry5.place(x=756,y=403, width=520, height=31)
        self.entry5.configure(font="-family {Poppins} -size 12")
        self.entry5.configure(relief="flat")

        self.entry6 = Entry(e_update)
        self.entry6.place(x=756,y=537, width=520, height=31)
        self.entry6.configure(font="-family {Poppins} -size 12")
        self.entry6.configure(relief="flat")
        self.entry6.configure(show="*")


        self.button1 = Button(e_update)
        self.button1.place(x=928,y=654, width=170, height=48)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#FE4343")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#FE4343")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""UPDATE""")
        self.button1.configure(command=self.update)

        self.button2 = Button(e_update)
        self.button2.place(x=1141,y=654, width=170, height=48)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#FE4343")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#FE4343")
        self.button2.configure(font="-family {Poppins SemiBold} -size 14")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""CLEAR""")
        self.button2.configure(command=self.clearr)

    def update(self):
        ename = self.entry1.get()
        econtact = self.entry2.get()
        eaddhar = self.entry3.get()
        edes = self.entry4.get()
        eadd = self.entry5.get()
        epass = self.entry6.get()

        if ename.strip():
            if valid_phone(econtact):
                if valid_aadhar(eaddhar):
                    if edes:
                        if eadd:
                            if epass:
                                emp_id = vall[0]
                                update_query = (
                                "UPDATE employee SET name = %s, contact_num = %s, address = %s, aadhar_num = %s, password = %s, designation = %s WHERE emp_id = %s"
                                )
                                cur.execute(update_query, (ename, econtact, eadd, eaddhar, epass, edes, emp_id))
                                db.commit()
                                messagebox.showinfo("Success!!", "Employee ID: {} successfully updated in database.".format(emp_id), parent=e_update)
                                vall.clear()
                                page5.tree.delete(*page5.tree.get_children())
                                page5.DisplayData()
                                Employee.sel.clear()
                                e_update.destroy()
                            else:
                                messagebox.showerror("Oops!", "Please enter a password.", parent=e_add)
                        else:
                            messagebox.showerror("Oops!", "Please enter address.", parent=e_add)
                    else:
                        messagebox.showerror("Oops!", "Please enter designation.", parent=e_add)
                else:
                    messagebox.showerror("Oops!", "Invalid Aadhar number.", parent=e_add)
            else:
                messagebox.showerror("Oops!", "Invalid phone number.", parent=e_add)
        else:
            messagebox.showerror("Oops!", "Please enter employee name.", parent=e_add)


    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)



    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def testchar(self, val):
        if val.isalpha():
            return True
        elif val == "":
            return True
        return False



        

class Invoice:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Invoices")

        self.label1 = Label(invoice)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/invoices.png")
        self.label1.configure(image=self.img)

        self.message = Label(invoice)
        self.message.place(x=152,y=77, width=136, height=30)
        self.message.configure(font="-family {Poppins} -size 10")
        self.message.configure(foreground="#000000")
        self.message.configure(background="#ffffff")
        self.message.configure(text="""ADMIN""")
        self.message.configure(anchor="w")

        self.clock = Label(invoice)
        self.clock.place(x=56,y=45, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.entry1 = Entry(invoice)
        self.entry1.place(relx=0.040, rely=0.286, width=240, height=28)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        self.button1 = Button(invoice)
        self.button1.place(relx=0.229, rely=0.289, width=76, height=23)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 10")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Search""")
        self.button1.configure(command=self.search_inv)

        self.button2 = Button(invoice)
        self.button2.place(x=58,y=83, width=76, height=23)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#CF1E14")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Logout""")
        self.button2.configure(command=self.Logout)

        self.button3 = Button(invoice)
        self.button3.place(relx=0.052, rely=0.432, width=306, height=28)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#CF1E14")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#CF1E14")
        self.button3.configure(font="-family {Poppins SemiBold} -size 12")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""DELETE INVOICE""")
        self.button3.configure(command=self.delete_invoice)

        self.button4 = Button(invoice)
        self.button4.place(relx=0.135, rely=0.885, width=76, height=23)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#CF1E14")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#ffffff")
        self.button4.configure(background="#CF1E14")
        self.button4.configure(font="-family {Poppins SemiBold} -size 12")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""EXIT""")
        self.button4.configure(command=self.Exit)

        self.scrollbarx = Scrollbar(invoice, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(invoice, orient=VERTICAL)
        self.tree = ttk.Treeview(invoice)
        self.tree.place(relx=0.307, rely=0.203, width=880, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.tree.bind("<Double-1>", self.double_tap)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
        self.scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)

        self.tree.configure(
            columns=(
                "Bill Number",
                "Date",
                "Customer Name",
                "Customer Phone No.",
            )
        )

        self.tree.heading("Bill Number", text="Bill Number", anchor=W)
        self.tree.heading("Date", text="Date", anchor=W)
        self.tree.heading("Customer Name", text="Customer Name", anchor=W)
        self.tree.heading("Customer Phone No.", text="Customer Phone No.", anchor=W)
        

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=219)
        self.tree.column("#2", stretch=NO, minwidth=0, width=219)
        self.tree.column("#3", stretch=NO, minwidth=0, width=219)
        self.tree.column("#4", stretch=NO, minwidth=0, width=219)
        

        self.DisplayData()


    def DisplayData(self):
        cur.execute("SELECT number,tdate,customer_name,customer_no FROM bill")
        fetch = cur.fetchall()
        for data in fetch:
            self.tree.insert("", "end", values=(data))

    sel = []
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def double_tap(self, Event):
        item = self.tree.identify('item', Event.x, Event.y)
        global bill_num
        bill_num = self.tree.item(item)['values'][0]
        

        global bill
        bill = Toplevel()
        pg = open_bill(bill)
        #bill.protocol("WM_DELETE_WINDOW", exitt)
        bill.mainloop()

        


    def delete_invoice(self):
        val = []
        to_delete = []

        if len(self.sel)!=0:
            sure = messagebox.askyesno("Confirm", "Are you sure you want to delete selected invoice(s)?", parent=invoice)
            if sure == True:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)
                
                for j in range(len(val)):
                    if j%5==0:
                        to_delete.append(val[j])
                
                for k in to_delete:
                    #delete = "DELETE FROM bill WHERE bill_no = ?"
                    cur.execute("DELETE FROM bill WHERE number = %s",(k,))
                    db.commit()

                messagebox.showinfo("Success!!", "Invoice(s) deleted from database.", parent=invoice)
                self.sel.clear()
                self.tree.delete(*self.tree.get_children())

                self.DisplayData()
        else:
            messagebox.showerror("Error!!","Please select an invoice", parent=invoice)

    def search_inv(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        to_search = self.entry1.get()
        for search in val:
            if search==to_search:
                self.tree.selection_set(val[val.index(search)-1])
                self.tree.focus(val[val.index(search)-1])
                messagebox.showinfo("Success!!", "Bill Number: {} found.".format(self.entry1.get()), parent=invoice)
                break
        else: 
            messagebox.showerror("Oops!!", "Bill NUmber: {} not found.".format(self.entry1.get()), parent=invoice)


    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            invoice.destroy()
            root.deiconify()
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def Exit(self):
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=invoice)
        if sure == True:
            invoice.destroy()
            adm.deiconify()


class open_bill:
    def __init__(self, top=None):
        
        top.geometry("765x488")
        top.resizable(0, 0)
        top.title("Bill")

        self.label1 = Label(bill)
        self.label1.place(relx=0, rely=0, width=765, height=488)
        self.img = PhotoImage(file="./images/bill.png")
        self.label1.configure(image=self.img)
        
        self.name_message = Text(bill)
        self.name_message.place(relx=0.178, rely=0.205, width=176, height=30)
        self.name_message.configure(font="-family {Podkova} -size 10")
        self.name_message.configure(borderwidth=0)
        self.name_message.configure(background="#ffffff")

        self.num_message = Text(bill)
        self.num_message.place(relx=0.854, rely=0.205, width=90, height=30)
        self.num_message.configure(font="-family {Podkova} -size 10")
        self.num_message.configure(borderwidth=0)
        self.num_message.configure(background="#ffffff")

        self.bill_message = Text(bill)
        self.bill_message.place(relx=0.150, rely=0.243, width=176, height=26)
        self.bill_message.configure(font="-family {Podkova} -size 10")
        self.bill_message.configure(borderwidth=0)
        self.bill_message.configure(background="#ffffff")

        self.bill_date_message = Text(bill)
        self.bill_date_message.place(relx=0.780, rely=0.243, width=90, height=26)
        self.bill_date_message.configure(font="-family {Podkova} -size 10")
        self.bill_date_message.configure(borderwidth=0)
        self.bill_date_message.configure(background="#ffffff")


        self.Scrolledtext1 = tkst.ScrolledText(top)
        self.Scrolledtext1.place(relx=0.044, rely=0.41, width=695, height=284)
        self.Scrolledtext1.configure(borderwidth=0)
        self.Scrolledtext1.configure(font="-family {Podkova} -size 8")
        self.Scrolledtext1.configure(state="disabled")

        #find_bill = "SELECT * FROM bill WHERE bill_no = ?"
        cur.execute("SELECT * FROM bill WHERE number = %s",(bill_num,))

        results = cur.fetchall()
        print(results)
        if results:
            self.name_message.insert(END, results[0][2])
            self.name_message.configure(state="disabled")
    
            self.num_message.insert(END, results[0][3])
            self.num_message.configure(state="disabled")
    
            self.bill_message.insert(END, results[0][0])
            self.bill_message.configure(state="disabled")

            self.bill_date_message.insert(END, results[0][1])
            self.bill_date_message.configure(state="disabled")

            cur.execute("select dnt_no from order_info where bill_no = %s",(results[0][0],))
            test=cur.fetchall()
            cur.execute("select charity,type,donation from donations where dnt_id = %s",(test[0][0],))
            test2=cur.fetchall()
            print(test2)
            for i in test2:
                for j in i:
                    self.Scrolledtext1.configure(state="normal")
                    self.Scrolledtext1.insert(END, j)
                    self.Scrolledtext1.insert(END, "\t\t\t\t\t\t  ")
                    self.Scrolledtext1.configure(state="disabled")
                self.Scrolledtext1.configure(state="normal")
                self.Scrolledtext1.insert(END, "\n")
                self.Scrolledtext1.configure(state="disabled")
                

page1 = login_page(root)
root.bind("<Return>", login_page.login)
root.mainloop()
