from future.moves.tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Data Management System")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(0,0)
        self.root.iconbitmap('sdms.ico')

        title = Label(self.root, text="Student Data Management System", bd=10, relief=GROOVE,
                      font=("impact", 30, "bold"), bg="#273746", fg="white")
        title.pack(side=TOP, fill=X)

        # *************** All Variables *************** #
        self.rollNoVar = StringVar()
        self.nameVar = StringVar()
        self.emailVar = StringVar()
        self.genderVar = StringVar()
        self.dobVar = StringVar()
        self.contactVar = StringVar()

        self.searchBy = StringVar()
        self.searchText = StringVar()

        # *************** Manage Frame *************** #
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE)
        Manage_Frame.place(x=20, y=110, width=450, height=580)

        # Title (Heading)
        manage_title = Label(Manage_Frame, text="Manage Students", font=("times new roman", 30, "bold")).grid(row=0, columnspan=2, pady=20)

        # Roll Number
        rollNo_lbl = Label(Manage_Frame, text="Roll Number",
                           font=("times new roman", 18, "bold")).grid(row=1, column=0, pady=10, padx=20, sticky='w')
        rollNo_entry = Entry(Manage_Frame, textvariable=self.rollNoVar, font=("times new roman", 14, "bold"), bd=5,
                             relief=GROOVE).grid(row=1, column=1, pady=10, padx=20, sticky='w')

        # Name
        name_lbl = Label(Manage_Frame, text="Name",
                         font=("times new roman", 18, "bold")).grid(row=2, column=0, pady=10, padx=20, sticky='w')
        name_entry = Entry(Manage_Frame, textvariable=self.nameVar, font=("times new roman", 14, "bold"), bd=5,
                           relief=GROOVE).grid(row=2, column=1, pady=10, padx=20, sticky='w')

        # Email
        email_lbl = Label(Manage_Frame, text="Email",
                          font=("times new roman", 18, "bold")).grid(row=3, column=0, pady=10, padx=20, sticky='w')
        email_entry = Entry(Manage_Frame, textvariable=self.emailVar, font=("times new roman", 14, "bold"), bd=5,
                            relief=GROOVE).grid(row=3, column=1, pady=10, padx=20, sticky='w')

        # Gender
        gender_lbl = Label(Manage_Frame, text="Gender",
                           font=("times new roman", 18, "bold")).grid(row=4, column=0, pady=10, padx=20, sticky='w')
        gender_combo = ttk.Combobox(Manage_Frame, textvariable=self.genderVar, font=("times new roman", 13, "bold"),
                                    state="readonly")
        gender_combo['values'] = ("Male", "Female", "Other")
        gender_combo.grid(row=4, column=1, pady=10, padx=20, sticky='w')

        # D.O.B
        dob_lbl = Label(Manage_Frame, text="D.O.B",
                        font=("times new roman", 18, "bold")).grid(row=5, column=0, pady=10, padx=20, sticky='w')
        dob_entry = Entry(Manage_Frame, textvariable=self.dobVar, font=("times new roman", 14, "bold"), bd=5,
                          relief=GROOVE).grid(row=5, column=1, pady=10, padx=20, sticky='w')

        # Contact
        contact_lbl = Label(Manage_Frame, text="Contact",
                            font=("times new roman", 18, "bold")).grid(row=6, column=0, pady=10, padx=20, sticky='w')
        contact_entry = Entry(Manage_Frame, textvariable=self.contactVar, font=("times new roman", 14, "bold"), bd=5,
                              relief=GROOVE).grid(row=6, column=1, pady=10, padx=20, sticky='w')

        # Address
        address_lbl = Label(Manage_Frame, text="Address",
                            font=("times new roman", 18, "bold")).grid(row=7, column=0, pady=10, padx=20, sticky='w')
        self.address_txt = Text(Manage_Frame, width=20, height=2, font=("times new roman", 14, "bold"), bd=5,
                                relief=GROOVE)
        self.address_txt.grid(row=7, column=1, pady=10, padx=20, sticky='w')
        # 'self.' is used with Text because "textvariable=self." is not allowed

        # ******** Button Frame ******** #
        Button_Frame = Frame(Manage_Frame, bd=5, relief=RIDGE, bg="lightgrey")
        Button_Frame.place(x=25, y=500, width=395)

        # Buttons
        add_button = Button(Button_Frame, text="Add", command=self.add, width=10, height=2, bg="#BFC9CA", fg="black").grid(row=0, column=0,
                                                                                                 padx=8, pady=8)
        update_button = Button(Button_Frame, command=self.update, text="Update", width=10, height=2, bg="#BFC9CA", fg="black").grid(row=0,
                                                                                                          column=2,
                                                                                                          padx=8,
                                                                                                          pady=8)
        delete_button = Button(Button_Frame, command=self.delete, text="Delete", width=10, height=2, bg="#BFC9CA", fg="black").grid(row=0,
                                                                                                          column=3,
                                                                                                          padx=8,
                                                                                                          pady=8)
        clear_button = Button(Button_Frame, command=self.clear, text="Clear", width=10, height=2, bg="#BFC9CA", fg="black").grid(row=0, column=4,
                                                                                                       padx=8, pady=8)

        # *************** Detail Frame *************** #
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE)
        Detail_Frame.place(x=490, y=110, width=850, height=580)

        search_lbl = Label(Detail_Frame, text="Search By",
                           font=("times new roman", 20, "bold")).grid(row=0, column=0, pady=10, padx=20, sticky='w')
        search_combo = ttk.Combobox(Detail_Frame, textvariable=self.searchBy, width=10,
                                    font=("times new roman", 14, "bold"), state="readonly")
        search_combo['values'] = ("RollNo", "Name", "Contact")
        search_combo.grid(row=0, column=1, pady=10, padx=20)

        search_txt = Entry(Detail_Frame, textvariable=self.searchText, font=("times new roman", 14, "bold"), bd=3,
                           relief=GROOVE).grid(row=0, column=2, pady=10, padx=20, sticky='w')
        search_button = Button(Detail_Frame, command=self.search, text="Search", width=12).grid(row=0, column=3,
                                                                                                pady=10, padx=10)
        showall_button = Button(Detail_Frame, command=self.fetch, text="Show All", width=12).grid(row=0, column=4,
                                                                                                  pady=10, padx=10)

        # ******** Table Frame ******** #
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE)
        Table_Frame.place(x=6, y=70, width=830, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(Table_Frame,
                                          columns=("rollNo", "name", "email", "gender", "dob", "contact", "address"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("rollNo", text="Roll Number")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="D.O.B")
        self.student_table.heading("contact", text="Contact")
        self.student_table.heading("address", text="Address")

        self.student_table['show'] = 'headings'
        self.student_table.column("rollNo", width=30)
        self.student_table.column("name", width=45)
        self.student_table.column("email", width=130)
        self.student_table.column("gender", width=5)
        self.student_table.column("dob", width=20)
        self.student_table.column("contact", width=20)
        self.student_table.column("address", width=150)
        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        # It is a type of event handling
        self.fetch()

    def add(self):
        if self.rollNoVar.get() == "" or self.nameVar.get() == "" or self.emailVar.get() == "" or self.genderVar.get() == "" or self.dobVar.get() == "" or self.contactVar.get() == "":
            messagebox.showerror("Error !", "All fields are required !")
        else:
            con = pymysql.connect(host="localhost", user="root", password="uokcsi2012", database="sdms")
            cur = con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",
                        (self.rollNoVar.get(),
                         self.nameVar.get(),
                         self.emailVar.get(),
                         self.genderVar.get(),
                         self.dobVar.get(),
                         self.contactVar.get(),
                         self.address_txt.get('1.0', END)
                         ))
            con.commit()
            self.fetch()
            self.clear()
            con.close()
            messagebox.showinfo("Success!", "Record has been inserted !")

    def fetch(self):
        con = pymysql.connect(host="localhost", user="root", password="uokcsi2012", database="sdms")
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.rollNoVar.set("")
        self.nameVar.set("")
        self.emailVar.set("")
        self.genderVar.set("")
        self.dobVar.set("")
        self.contactVar.set("")
        self.address_txt.delete("1.0", END)

    def get_cursor(self, event):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.rollNoVar.set(row[0])
        self.nameVar.set(row[1])
        self.emailVar.set(row[2])
        self.genderVar.set(row[3])
        self.dobVar.set(row[4])
        self.contactVar.set(row[5])
        self.address_txt.delete("1.0", END)
        self.address_txt.insert(END, row[6])

    def update(self):
        con = pymysql.connect(host="localhost", user="root", password="uokcsi2012", database="sdms")
        cur = con.cursor()
        cur.execute("update students set name=%s, email=%s, gender=%s, dob=%s, contact=%s, address=%s where rollNo=%s",
                    (self.nameVar.get(),
                     self.emailVar.get(),
                     self.genderVar.get(),
                     self.dobVar.get(),
                     self.contactVar.get(),
                     self.address_txt.get('1.0', END),
                     self.rollNoVar.get()
                     ))
        con.commit()
        self.fetch()
        self.clear()
        con.close()

    def delete(self):
        con = pymysql.connect(host="localhost", user="root", password="uokcsi2012", database="sdms")
        cur = con.cursor()
        cur.execute("delete from students where rollNo=%s", self.rollNoVar.get())
        con.commit()
        con.close()
        self.fetch()
        self.clear()

    def search(self):
        con = pymysql.connect(host="localhost", user="root", password="uokcsi2012", database="sdms")
        cur = con.cursor()
        cur.execute(
            "select * from students where " + str(self.searchBy.get()) + " LIKE '%" + str(self.searchText.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            con.commit()
        con.close()


root = Tk()
obj = Student(root)
root.mainloop()