#==================imports===================
import mysql.connector 
import re
import webbrowser
import random
import string
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from time import strftime
from datetime import date
from tkinter import scrolledtext as tkst
 
#============================================

root = Tk()

root.geometry("1366x768")
root.title("Retail Manager")


user = StringVar()
passwd = StringVar()
fname = StringVar()
lname = StringVar()
new_user = StringVar()
new_passwd = StringVar()
donation= StringVar()
total_money=[]
serial_no=[]
l=0
cust_name = StringVar()
cust_num = StringVar()
cust_new_bill = StringVar()
cust_new_dnt=StringVar()
cust_search_bill = StringVar()
bill_date = StringVar()


db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Herobrinewastaken7"
)
print(db) 

cur = db.cursor()   

def random_bill_number(stringLength):
    lettersAndDigits = string.ascii_letters.upper() + string.digits
    strr=''.join(random.choice(lettersAndDigits) for i in range(stringLength-2))
    return ('BB'+strr)

def random_donation_number(stringLength):
    lettersAndDigits = string.ascii_letters.upper() + string.digits
    strr=''.join(random.choice(lettersAndDigits) for i in range(stringLength-2))
    return ('DD'+strr)


def valid_phone(phn):
    if re.match(r"[789]\d{9}$", phn):
        return True
    return False

def login(Event=None):
    global username
    username = user.get()
    password = passwd.get()

    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Herobrinewastaken7"
    )
    cur = db.cursor()  
    cur.execute("USE project")
    cur.execute("SELECT * FROM employee WHERE emp_id = %s AND password = %s", (username, password))
    results = cur.fetchall()
    if results:
        messagebox.showinfo("Login Page", "The login is successful")
        cust_new_dnt.set(random_donation_number(8))
        page1.entry1.delete(0, END)
        page1.entry2.delete(0, END)
        root.withdraw()
        global manager
        global page2
        manager = Toplevel()
        page2 = bill_window(manager)
        page2.time()
        manager.protocol("WM_DELETE_WINDOW", exitt)
        manager.mainloop()

    else:
        messagebox.showerror("Error", "Incorrect username or password.")
        page1.entry2.delete(0, END)



def logout():
    sure = messagebox.askyesno("Logout", "Are you sure you want to logout?", parent=manager)
    if sure == True:
        manager.destroy()
        root.deiconify()
        page1.entry1.delete(0, END)
        page1.entry2.delete(0, END)

class login_page:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("CHARITY MANAGEMENT EMPLOYEE WINDOW")

        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/employee_login.png")
        self.label1.configure(image=self.img)

        self.entry1 = Entry(root)
        self.entry1.place(x=144, y=308, width=374, height=24)
        self.entry1.configure(font="-family {Poppins} -size 15")
        self.entry1.configure(relief="flat")
        self.entry1.configure(textvariable=user)

        self.entry2 = Entry(root)
        self.entry2.place(x=144, y=436, width=374, height=24)
        self.entry2.configure(font="-family {Poppins} -size 15")
        self.entry2.configure(relief="flat")
        self.entry2.configure(show="*")
        self.entry2.configure(textvariable=passwd)

        self.button1 = Button(root)
        self.button1.place(x=155, y=563, width=250, height=43)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#FF4D00")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#FF4D00")
        self.button1.configure(font="-family {Poppins SemiBold} -size 25")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""LOGIN""")
        self.button1.configure(command=login)


class Item:
    def __init__(self, type, charity, donation):
        self.type = type
        self.charity = charity
        self.donation = donation

class Cart:
    def __init__(self):
        self.items = []
        self.dictionary = {}

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self):
        self.items.pop()

    def remove_items(self):
        self.items.clear()

    def total(self):
        total=0.0
        for i in total_money:
            total = total + i 
        return total

    def isEmpty(self):
        if len(self.items)==0:
            return True
        
    def allCart(self):
        for i in self.items:
            if (i.type in self.dictionary):
                self.dictionary[i.type] += i.qty
            else:
                self.dictionary.update({i.type:i.qty})
    

def exitt():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=manager)
    if sure == True:
        manager.destroy()
        root.destroy()


class bill_window:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("CHARITY HELP MANAGEMENT EMPLOYEE WINDOW")

        self.label = Label(manager)
        self.label.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/bill_window.png")
        self.label.configure(image=self.img)

        self.message = Label(manager)
        self.message.place(x=61, y=53, width=88, height=21)
        self.message.configure(font="-family {Poppins} -size 10")
        self.message.configure(foreground="#000000")
        self.message.configure(background="#ffffff")
        self.message.configure(text=username)
        self.message.configure(anchor="w")

        self.clock = Label(manager)
        self.clock.place(x=54, y=133, width=104, height=26)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.entry1 = Entry(manager)
        self.entry1.place(x=749, y=182, width=193, height=18)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")
        self.entry1.configure(textvariable=cust_name)

        self.entry2 = Entry(manager)
        self.entry2.place(x=1123, y=182, width=179, height=18)
        self.entry2.configure(font="-family {Poppins} -size 12")
        self.entry2.configure(relief="flat")
        self.entry2.configure(textvariable=cust_num)

        self.button1 = Button(manager)
        self.button1.place(x=185, y=53, width=83, height=21)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 12")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Logout""")
        self.button1.configure(command=logout)

        self.button2 = Button(manager)
        self.button2.place(x=436, y=589, width=83, height=21)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#CF1E14")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Reset""")
        self.button2.configure(command=self.reset_dbms)
        

        self.button3 = Button(manager)
        self.button3.place(x=67, y=679, width=83, height=21)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#CF1E14")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#CF1E14")
        self.button3.configure(font="-family {Poppins SemiBold} -size 12")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""Total""")
        self.button3.configure(command=self.total_bill)

        self.button4 = Button(manager)
        self.button4.place(x=186, y=679, width=83, height=21)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#CF1E14")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#ffffff")
        self.button4.configure(background="#CF1E14")
        self.button4.configure(font="-family {Poppins SemiBold} -size 12")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""Generate""")
        self.button4.configure(command=self.gen_bill)

        self.button5 = Button(manager)
        self.button5.place(x=310, y=679, width=83, height=21)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#CF1E14")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#ffffff")
        self.button5.configure(background="#CF1E14")
        self.button5.configure(font="-family {Poppins SemiBold} -size 12")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""Clear""")
        self.button5.configure(command=self.clear_bill)

        self.button6 = Button(manager)
        self.button6.place(x=436, y=679, width=83, height=21)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#CF1E14")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#CF1E14")
        self.button6.configure(font="-family {Poppins SemiBold} -size 12")
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""Exit""")
        self.button6.configure(command=exitt)

        self.button7 = Button(manager)
        self.button7.place(x=67, y=590, width=83, height=21)
        self.button7.configure(relief="flat")
        self.button7.configure(overrelief="flat")
        self.button7.configure(activebackground="#CF1E14")
        self.button7.configure(cursor="hand2")
        self.button7.configure(foreground="#ffffff")
        self.button7.configure(background="#CF1E14")
        self.button7.configure(font="-family {Poppins SemiBold} -size 12")
        self.button7.configure(borderwidth="0")
        self.button7.configure(text="""Add""")
        self.button7.configure(command=self.add_to_list)
        

        self.button8 = Button(manager)
        self.button8.place(x=186, y=590, width=83, height=21)
        self.button8.configure(relief="flat")
        self.button8.configure(overrelief="flat")
        self.button8.configure(activebackground="#CF1E14")
        self.button8.configure(cursor="hand2")
        self.button8.configure(foreground="#ffffff")
        self.button8.configure(background="#CF1E14")
        self.button8.configure(font="-family {Poppins SemiBold} -size 12")
        self.button8.configure(borderwidth="0")
        self.button8.configure(text="""Clear""")
        self.button8.configure(command=self.clear_selection)

        self.button9 = Button(manager)
        self.button9.place(x=310, y=590, width=83, height=21)
        self.button9.configure(relief="flat")
        self.button9.configure(overrelief="flat")
        self.button9.configure(activebackground="#CF1E14")
        self.button9.configure(cursor="hand2")
        self.button9.configure(foreground="#ffffff")
        self.button9.configure(background="#CF1E14")
        self.button9.configure(font="-family {Poppins SemiBold} -size 12")
        self.button9.configure(borderwidth="0")
        self.button9.configure(text="""Remove""")
        self.button9.configure(command=self.remove_charity)


        text_font = ("Poppins", "8")
        self.combo1 = ttk.Combobox(manager)
        self.combo1.place(x=78, y=311, width=431, height=22)
        
        cur.execute("USE project")
        cur.execute("SELECT city FROM charitylist")
        result1 = cur.fetchall()
        cat = []
        for i in range(len(result1)):
            if(result1[i][0] not in cat):
                cat.append(result1[i][0])
        self.combo1.configure(values=cat)
        self.combo1.configure(state="readonly")
        self.combo1.configure(font="-family {Poppins} -size 10")
        self.combo1.option_add("*TCombobox*Listbox.font", text_font)
        self.combo1.option_add("*TCombobox*Listbox.selectBackground", "#D2463E")


        self.combo2 = ttk.Combobox(manager)
        self.combo2.place(x=78, y=359, width=431, height=22)
        self.combo2.configure(font="-family {Poppins} -size 10")
        self.combo2.option_add("*TCombobox*Listbox.font", text_font) 
        self.combo2.configure(state="disabled")


        self.combo3 = ttk.Combobox(manager)
        self.combo3.place(x=78, y=408, width=431, height=22)
        self.combo3.configure(state="disabled")
        self.combo3.configure(font="-family {Poppins} -size 10")
        self.combo3.option_add("*TCombobox*Listbox.font", text_font)

        self.entry4 = ttk.Entry(manager)
        self.entry4.place(x=78, y=455, width=431, height=22)
        self.entry4.configure(font="-family {Poppins} -size 10")
        self.entry4.configure(foreground="#000000")
        self.entry4.configure(state="disabled")
        self.entry4.configure(textvariable=donation)

        self.Scrolledtext1 = tkst.ScrolledText(top)
        self.Scrolledtext1.place(relx=0.439, rely=0.586, width=685, height=230)
        self.Scrolledtext1.configure(borderwidth=0)
        self.Scrolledtext1.configure(font="-family {Podkova} -size 8")
        self.Scrolledtext1.configure(state="disabled")

        self.combo1.bind("<<ComboboxSelected>>", self.get_category)

    def reset_dbms(self):
        sure = messagebox.askyesno("RESET", "Are you sure you want to RESET the database?", parent=manager)
        if sure == True:
            sure2 = messagebox.askyesno("RESET", "CONFIRM?", parent=manager)
            if sure2 == True:
                cur.execute("TRUNCATE TABLE donations")
                db.commit()
                cur.execute("TRUNCATE TABLE order_info")
                db.commit()
                cur.execute("TRUNCATE TABLE bill")
                db.commit()
                messagebox.showinfo("Success!!", "Database has been reset!", parent=manager)
        
        
    def get_category(self, Event):
        self.combo2.configure(state="readonly")
        self.combo2.set('')
        self.combo3.set('')
        cname=self.combo1.get()
        cur.execute("use project")
        cur.execute("SELECT char_type FROM charitylist WHERE city = '%s'"%(cname))
        result2 = cur.fetchall()
        subcat = []
        for j in range(len(result2)):
            if(result2[j][0] not in subcat):
                subcat.append(result2[j][0])
        
        self.combo2.configure(values=subcat)
        self.combo2.bind("<<ComboboxSelected>>", self.get_subcat)
        self.combo3.configure(state="disabled")

    def get_subcat(self, Event):
        self.combo3.configure(state="readonly")
        self.combo3.set('')
        cur.execute("SELECT charity FROM charitylist WHERE city = '%s' and char_type= '%s'"%(self.combo1.get(), self.combo2.get()))
        result3 = cur.fetchall()
        pro = []
        for k in range(len(result3)):
            pro.append(result3[k][0])

        self.combo3.configure(values=pro)
        self.combo3.bind("<<ComboboxSelected>>", self.money1)

    def money1(self, Event):
        self.entry4.configure(state="normal") 
        self.entry4.configure(foreground="#000000")
                
    cart = Cart()
    def add_to_list(self):
        dnt=donation.get()
        city=self.combo1.get()
        type=self.combo2.get()
        charity=self.combo3.get()
        self.Scrolledtext1.configure(state="normal")
        strr = self.Scrolledtext1.get('1.0', END)
        if strr.find('Total')==-1:
            type = self.combo2.get()
            if(city!=""):
                if (type!=""):
                    if dnt.isdigit()==True:
                        cur.execute("select char_id from charitylist where charity ='%s'"%(self.combo3.get()))
                        charid=cur.fetchall()
                        char_id=charid[0][0]
                        item = Item(type, charity, donation.get())
                        self.cart.add_item(item)
                        total_money.append(int(donation.get()))
                        self.Scrolledtext1.configure(state="normal")   
                        cur.execute("insert into donations (city,type,charity,donation,char_id,dnt_id) values (%s,%s,%s,%s,%s,%s)",(self.combo1.get(),self.combo2.get(),self.combo3.get(),int(dnt),char_id,cust_new_dnt.get()))
                        db.commit()                     
                        bill_text = "{}\t\t\t\t\t\t{}\t\t\t\t\t\t     {}\n".format(type, charity , donation.get())
                        self.Scrolledtext1.insert('insert', bill_text)
                        self.Scrolledtext1.configure(state="disabled")
                    else:
                        messagebox.showerror("Oops!", "Enter a Valid Amount of Money.", parent=manager)
                else:
                    messagebox.showerror("Oops!", "Select a Type of Charity", parent=manager)
            else:
                messagebox.showerror("Oops!", "Enter a city.", parent=manager)
       

    def remove_charity(self):
        if(self.cart.isEmpty()!=True):
            self.Scrolledtext1.configure(state="normal")
            strr = self.Scrolledtext1.get('1.0', END)
            if strr.find('Total')==-1:
                try:
                    poped=total_money.pop()
                    print(poped)
                    self.cart.remove_item()
                    
                except IndexError:
                    messagebox.showerror("Oops!", "List is empty", parent=manager)
                else:
                    self.Scrolledtext1.configure(state="normal")
                    get_all_bill = (self.Scrolledtext1.get('1.0', END).split("\n"))
                    new_string = get_all_bill[:len(get_all_bill)-3]
                    self.Scrolledtext1.delete('1.0', END)
                    for i in range(len(new_string)):
                        self.Scrolledtext1.insert('insert', new_string[i])
                        self.Scrolledtext1.insert('insert','\n')
                    poped=total_money.pop()
                    self.Scrolledtext1.configure(state="disabled")
            else:
                try:
                    self.cart.remove_item()
                    poped=total_money.pop()
                except IndexError:
                    messagebox.showerror("Oops!", "List is empty", parent=manager)
                else:
                    self.Scrolledtext1.delete('1.0', END)
                    new_li = []
                    li = strr.split("\n")
                    for i in range(len(li)):
                        if len(li[i])!=0:
                            if li[i].find('Total')==-1:
                                new_li.append(li[i])
                            else:
                                break
                    new_li.pop()
                    for j in range(len(new_li)-1):
                        self.Scrolledtext1.insert('insert', new_li[j])
                        self.Scrolledtext1.insert('insert','\n')
                    self.Scrolledtext1.configure(state="disabled")
                    poped=total_money.pop()

        else:
            messagebox.showerror("Oops!", "Add a Charity.", parent=manager)

    def wel_bill(self):
        self.name_message = Text(manager)
        self.name_message.place(x=683, y=384, width=176, height=17)
        self.name_message.configure(font="-family {Podkova} -size 10")
        self.name_message.configure(borderwidth=0)
        self.name_message.configure(background="#ffffff")

        self.num_message = Text(manager)
        self.num_message.place(x=1188, y=384, width=90, height=17)
        self.num_message.configure(font="-family {Podkova} -size 10")
        self.num_message.configure(borderwidth=0)
        self.num_message.configure(background="#ffffff")

        self.bill_message = Text(manager)
        self.bill_message.place(x=683, y=408, width=176, height=17)
        self.bill_message.configure(font="-family {Podkova} -size 10")
        self.bill_message.configure(borderwidth=0)
        self.bill_message.configure(background="#ffffff")

        self.bill_date_message = Text(manager)
        self.bill_date_message.place(x=1188, y=408, width=90, height=17)
        self.bill_date_message.configure(font="-family {Podkova} -size 10")
        self.bill_date_message.configure(borderwidth=0)
        self.bill_date_message.configure(background="#ffffff")
    
    def total_bill(self):
        if self.cart.isEmpty():
            messagebox.showerror("Oops!", "Add a Charity.", parent=manager)
        else:
            self.Scrolledtext1.configure(state="normal")
            strr = self.Scrolledtext1.get('1.0', END)
            if strr.find('Total')==-1:
                self.Scrolledtext1.configure(state="normal")
                divider = "\n\n\n"+("─"*82)
                self.Scrolledtext1.insert('insert', divider)
                total = "\nTotal\t\t\t\t\t\t\t\t\t\t\t\tRs. {}".format(sum(total_money))
                self.Scrolledtext1.insert('insert', total)
                divider2 = "\n"+("─"*82)
                self.Scrolledtext1.insert('insert', divider2)
                self.Scrolledtext1.configure(state="disabled")
            else:
                return

    state = 1
    
    def gen_bill(self):

        if self.state == 1:
                
                self.wel_bill()               
                if(cust_name.get()==""):
                    messagebox.showerror("Oops!", "Please enter a name.", parent=manager)
                elif(cust_num.get()==""):
                    messagebox.showerror("Oops!", "Please enter a number.", parent=manager)
                elif valid_phone(cust_num.get())==False:
                    messagebox.showerror("Oops!", "Please enter a valid number.", parent=manager)
                elif(self.cart.isEmpty()):
                     messagebox.showerror("Oops!", "list is empty.", parent=manager)
                else:
                    self.name_message.insert(END, cust_name.get())
                    self.name_message.configure(state="disabled")
            
                    self.num_message.insert(END, cust_num.get())
                    self.num_message.configure(state="disabled")
            
                    cust_new_bill.set(random_bill_number(8))

                    self.bill_message.insert(END, cust_new_bill.get())
                    self.bill_message.configure(state="disabled")
                
                    bill_date.set(str(date.today()))

                    self.bill_date_message.insert(END, bill_date.get())
                    self.bill_date_message.configure(state="disabled")
                    strr = self.Scrolledtext1.get('1.0', END)
                    cur.execute("use project")
                    test1=cust_new_bill.get()
                    print(test1)
                    cur.execute("select char_id from donations where charity='%s'"%(self.combo3.get()))
                    charid2=cur.fetchall()
                    char_id2=charid2[0][0]
                    print(self.cart.total())
                    cur.execute("INSERT INTO order_info (bill_no,dnt_no) VALUES ('%s','%s')"%(cust_new_bill.get(),cust_new_dnt.get()))
                    db.commit()
                    cur.execute("select distinct char_id from donations where dnt_id=('%s')"%(cust_new_dnt.get()))
                    char_id=list(cur.fetchall())
                    for i in char_id:
                        print(i)
                        cur.execute("INSERT INTO bill (number,tdate,customer_name,customer_no,char_id,donation) VALUES ('%s','%s','%s','%s',%s,%s)"%(str(cust_new_bill.get()), str(bill_date.get()), cust_name.get(), cust_num.get(),char_id2,int(self.cart.total())))
                        db.commit()
                    
                    messagebox.showinfo("Success!!", "Bill Generated", parent=manager)
                    self.entry1.configure(state="disabled", disabledbackground="#ffffff", disabledforeground="#000000")
                    self.entry2.configure(state="disabled", disabledbackground="#ffffff", disabledforeground="#000000")
                    self.state = 0
        else:
            return
                    
    def clear_bill(self):
        self.wel_bill()
        self.entry1.configure(state="normal")
        self.entry2.configure(state="normal")
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.name_message.configure(state="normal")
        self.num_message.configure(state="normal")
        self.bill_message.configure(state="normal")
        self.bill_date_message.configure(state="normal")
        self.Scrolledtext1.configure(state="normal")
        self.name_message.delete(1.0, END)
        self.num_message.delete(1.0, END)
        self.bill_message.delete(1.0, END)
        self.bill_date_message.delete(1.0, END)
        self.Scrolledtext1.delete(1.0, END)
        self.name_message.configure(state="disabled")
        self.num_message.configure(state="disabled")
        self.bill_message.configure(state="disabled")
        self.bill_date_message.configure(state="disabled")
        self.Scrolledtext1.configure(state="disabled")
        self.cart.remove_items()
        self.state = 1
        total_money.clear()
        cust_new_dnt.set(random_donation_number(8))


    def clear_selection(self):
        self.entry4.delete(0, END)
        self.combo1.configure(state="normal")
        self.combo2.configure(state="normal")
        self.combo3.configure(state="normal")
        self.combo1.delete(0, END)
        self.combo2.delete(0, END)
        self.combo3.delete(0, END)
        self.combo2.configure(state="disabled")
        self.combo3.configure(state="disabled")
        self.entry4.configure(state="disabled")
        
        
        
        try:
            self.entry4.configure(foreground="#ffffff")
        except AttributeError:
            pass
           
    
        
    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)


page1 = login_page(root)
root.bind("<Return>", login)
root.mainloop()

