import tkinter as tk
from manipulationData import *
from tkinter import messagebox
import tkinter.ttk as tk2
import random

mainColor = "blue"
dangColor = "red"

my_font = ("Helvetica", 12)
tittleFont = ("Verdana", 30, "bold")
fontNormal = ("Verdana", 15,)
fontBtn = ("Verdana", 15, "bold")
fontSmall = ("Verdana", 10,)
fontInput = ("Verdana", 12,)


def enter_btn_blue(e):
    btn = e.widget
    btn.configure(bg=mainColor, fg="white", )


def enter_btn_red(e):
    btn = e.widget
    btn.configure(bg=dangColor, fg="white", )


def leave_btn(e):
    btn = e.widget
    btn.configure(bg="white", fg="blue", )


# exit app when click yes in form wd_cancel
def exit():
    loginScreen.withdraw()
    wd_cancel.withdraw()


# show or hide password
def check_pass(e):
    global show
    # global valueCheck
    if not show:
        inputPassword["show"] = ""
        # valueCheck = tk.PhotoImage(file=r"image/hide1.png")
        # btnDisplay["image"] = valueCheck
        btnDisplay["text"] = "Hide"
        show = True
    else:
        inputPassword["show"] = "*"
        # valueCheck = tk.PhotoImage(file=r"image/show1.png")
        # btnDisplay["image"] = valueCheck
        btnDisplay["text"] = "Show"
        show = False


# btn cancel form login
def click_cancel(e):
    wd_cancel.deiconify()


# read data account
def click_login(e):
    if len(inputUserName.get()) == 0 or len(inputPassword.get()) == 0:
        messagebox.showwarning("Login Failure", "username and Password is not emtry")
    else:
        list_account = read_account("data/account.txt")
        check = check_account(list_account, inputUserName.get(), inputPassword.get())
        if check:
            loginScreen.withdraw()
            messagebox.showinfo("Login Successfully", "Login Successfully - Click \"OK\" to continue")
            main.deiconify()
        else:
            messagebox.showerror("Login Failure", "Username or Password is not matched")


# check male
def check_male():
    print(cb1.get())


def check_valid_integer(*args):
    check = True
    for value in args:
        if not value.isdigit():
            messagebox.showerror("Error type input AGE", "Incorrect data type!")
            check = False
            break
    return check


def check_valid_decimal(*args):
    try:
        lst_value = []
        for value in args:
            value = float(value)
            lst_value.append(value)
        return lst_value[0], lst_value[1], lst_value[2]
    except ValueError:
        messagebox.showerror("Error type input", "Incorrect data type!")
        return False


def check_blank(*args):
    check = False
    for value in args:
        if value == "":
            messagebox.showerror("Error entry", "Fields is not entry!")
            check = True
            break
    return check


# add new Student
def add_new_student(e):
    global list_students
    if list_students.find_student_code(input_code.get()) != -1:
        messagebox.showerror("Error", f"Code {input_code.get()} is exist!")
        return
    code = str(random.randint(1000000, 9999999)) + str(random.randint(10, 100))
    if not check_blank(input_name.get(), input_age.get(), input_address.get(), input_chem_point.get(),
                       input_phys_point.get(), input_math_point.get()):
        name = input_name.get()
        if check_valid_integer(input_age.get()):
            age = input_age.get()
            gender = cb1.get()
            address = input_address.get()
            math_point, phys_point, chem_point = check_valid_decimal(input_math_point.get(), input_phys_point.get(),
                                                                     input_chem_point.get())
            student = Student(code, name, age, gender, address, math_point, phys_point, chem_point)
            messagebox.showinfo("Successfully", "Add student success!")
            list_students.add_new(student)
            write_new_line("data/list_students.txt", student)
            tree.insert(parent="", index=student.code, text=str(len(list_students.get_list())),
                        values=(student.return_list_value()), )
            reset("")
    else:
        return


def clear_input():
    input_name.delete(0, tk.END)
    input_age.delete(0, tk.END)
    cb1.set(0)
    input_address.delete(0, tk.END)
    input_math_point.delete(0, tk.END)
    input_phys_point.delete(0, tk.END)
    input_chem_point.delete(0, tk.END)


def reset(e):
    input_code["state"] = "normal"
    input_code.delete(0, tk.END)
    input_code["state"] = "disable"
    input_name.delete(0, tk.END)
    input_age.delete(0, tk.END)
    cb1.set(0)
    input_address.delete(0, tk.END)
    input_math_point.delete(0, tk.END)
    input_phys_point.delete(0, tk.END)
    input_chem_point.delete(0, tk.END)
    selected_items = tree.selection()
    for item in selected_items:
        tree.selection_remove(item)


# get_data
def get_data(event):
    selected_items = tree.selection()
    if len(selected_items) == 0:
        return
    selected_item = selected_items[0]
    item_values = tree.item(selected_item)["values"]
    clear_input()
    input_code["state"] = "normal"
    input_code.delete(0, tk.END)
    input_code.insert(0, item_values[0])
    input_code["state"] = "disable"
    input_name.insert(0, item_values[1])
    input_age.insert(0, item_values[2])
    cb1.set(True if item_values[3] == "True" else False)
    input_address.insert(0, item_values[4])
    input_math_point.insert(0, item_values[5])
    input_phys_point.insert(0, item_values[6])
    input_chem_point.insert(0, item_values[7])


# delete student
def agree_delete():
    if len(tree.selection()) == 0:
        messagebox.showerror("Error", "You must select a row on table to delete")
        return
    else:
        global list_students
        index_found = list_students.find_student_code(input_code.get())
        if index_found != -1:
            list_students.remove_student(ls_type_list[index_found])
            remove_line("data/list_students.txt", index_found)
            tree.delete(tree.selection()[0])
            wd_remove_student.withdraw()
            messagebox.showinfo("Success", "Delete student successfully")
            main.deiconify()
            return
        else:
            messagebox.showerror("Error", f"student code {input_code.get()} is not exist!")


# refuse delete
def refuse_delete():
    main.deiconify()
    wd_remove_student.withdraw()


# window remove student start
def close_wdst():
    wd_remove_student.withdraw()
    main.deiconify()


wd_remove_student = tk.Tk()
wd_remove_student.title("Remove Student")
wd_remove_student.geometry("415x85")
wd_remove_student.withdraw()
wd_remove_student.protocol("WM_DELETE_WINDOW", close_wdst)


# window remove student end


def delete_student(e):
    if len(tree.selection()) == 0:
        messagebox.showerror("Error", "You must select a row on table to delete")
        return
    else:
        wd_remove_student.deiconify()
        wd_notification(wd_remove_student, f"Are you sure you want to delete student code \'{input_code.get()}\'",
                        "Yes", "No", agree_delete, refuse_delete)
        main.withdraw()


def update_student(e):
    global list_students
    if input_code.get() == "":
        messagebox.showerror("Error", "You must one row in table")
        return
    else:
        index_found = list_students.find_student_code(input_code.get())
        if index_found == -1:
            messagebox.showerror("Error", f"student code {input_code.get()} is not exist!")
            return
        else:
            if not check_blank(input_name.get(), input_age.get(), input_address.get(), input_chem_point.get(),
                               input_phys_point.get(), input_math_point.get()):
                name = input_name.get()
                if check_valid_integer(input_age.get()):
                    age = input_age.get()
                    gender = cb1.get()
                    address = input_address.get()
                    math_point, phys_point, chem_point = check_valid_decimal(input_math_point.get(),
                                                                             input_phys_point.get(),
                                                                             input_chem_point.get())
                    new_values = Student(input_code.get(), name, age, gender, address, math_point, phys_point,
                                         chem_point)
                    list_students.update_list(input_code.get(), new_values)
                    selected_items = tree.selection()
                    tree.item(selected_items[0], values=new_values.return_list_value())
                    write_down_file("data/list_students.txt", list_students.get_list())
                    messagebox.showinfo("Update", f"Update student code {input_code.get()} successfully!")
                    reset("")


def check_student():
    index_found = list_students.find_student_code(input_code_find.get())
    if index_found == -1:
        messagebox.showerror("Error", f"student code {input_code_find.get()} is not exist!")
        return
    else:
        selected_items = tree.get_children()[index_found]
        # Chọn hàng có ID là item_id trong TreeView widget
        tree.selection_set(selected_items)
        wd_find.withdraw()
        # tree.focus(selected_items)


def on_close_window():
    wd_find.withdraw()


wd_find = tk.Tk()
wd_find.title("Find student with code")
wd_find.geometry("350x50")
wd_find.protocol("WM_DELETE_WINDOW", on_close_window)
lb_find = tk.Label(wd_find, text="Enter code ", font=fontSmall)
lb_find.grid(column=0, row=0, padx=10)

input_code_find = tk.Entry(wd_find, width=15, font=fontInput, highlightthickness=1, highlightcolor="blue",
                           insertbackground="blue", borderwidth=2)
input_code_find.grid(column=1, row=0, padx=10)

btn_find_student = tk.Button(wd_find, text="Check", font=fontSmall, relief="groove", fg=mainColor, width=6,
                             command=check_student)
btn_find_student.grid(row=0, column=2, pady=3, padx=3)
wd_find.withdraw()


def open_wd_find(e):
    wd_find.deiconify()
    input_code_find.focus()


def wd_notification(master, question, yes, no, event_yes, event_no):
    lb_question = tk.Label(master, text=str(question), font=fontSmall)
    lb_question.grid(column=1, row=1, columnspan=2, padx=10, pady=10)

    wdc_btn_no = tk.Button(master, text=str(no), width=5, font=fontSmall, relief="groove", command=event_no)
    wdc_btn_no.grid(column=1, row=2, )
    wdc_btn_no.bind("<Enter>", enter_btn_blue)
    wdc_btn_no.bind("<Leave>", leave_btn)

    wdc_btn_yes = tk.Button(master, text=str(yes), width=5, font=fontSmall, relief="groove", command=event_yes)
    wdc_btn_yes.grid(column=2, row=2, )
    wdc_btn_yes.bind("<Enter>", enter_btn_red)
    wdc_btn_yes.bind("<Leave>", leave_btn)


# window cancel start
wd_cancel = tk.Tk()
wd_cancel.geometry("250x100")
wd_cancel.title("Exit")
wd_cancel.withdraw()
wd_notification(wd_cancel, "Are you sure you want to exit", "Yes", "No", exit, wd_cancel.withdraw)


# window cancel end


def on_tab_pressed(event):
    event.widget.tk_focusNext().focus()


# window login start
loginScreen = tk.Tk()
loginScreen.geometry("430x250")
loginScreen.title("Login")
loginScreen.bind("<Return>", click_login)
lbLogin = tk.Label(loginScreen, text="Login Page", font=tittleFont, fg="blue")
lbLogin.grid(column=1, row=1, columnspan=3)

lbUserName = tk.Label(loginScreen, text="Username", font=fontNormal)
lbUserName.grid(column=1, row=2, padx=10, pady=10)

inputUserName = tk.Entry(loginScreen, width=20, font=fontNormal, highlightthickness=1, highlightcolor="blue",
                         insertbackground="blue", )
inputUserName.grid(column=2, row=2, ipady=4, ipadx=2, padx=10, pady=10, columnspan=2, sticky="w")


lbPassword = tk.Label(loginScreen, text="Password", font=fontNormal)
lbPassword.grid(column=1, row=3, padx=10, pady=10)
inputPassword = tk.Entry(loginScreen, width=15, font=fontNormal, highlightthickness=1, highlightcolor="blue",
                         insertbackground="blue", show="*", )
inputPassword.grid(column=2, row=3, ipady=4, ipadx=2, padx=10, sticky="w")

show = False
# img = ImageTk.PhotoImage(Image.open("Downloads/show.png"))
# icon = tk.PhotoImage(file=r"image/show1.png")
btnDisplay = tk.Label(loginScreen, text="Show", font=fontSmall)
btnDisplay.grid(column=3, row=3, )
btnDisplay.bind("<Button-1>", check_pass)

btnCancel = tk.Button(loginScreen, text="Cancel", font=fontBtn, relief="groove", fg=mainColor)
btnCancel.place(x=50, y=180)
btnCancel.bind("<Enter>", enter_btn_red)
btnCancel.bind("<Leave>", leave_btn)
btnCancel.bind("<Button-1>", click_cancel)

btnLogin = tk.Button(loginScreen, text="Login", font=fontBtn, relief="groove", fg=mainColor)
btnLogin.place(x=300, y=180)
btnLogin.bind("<Enter>", enter_btn_blue)
btnLogin.bind("<Leave>", leave_btn)
btnLogin.bind("<Button-1>", click_login)
# window login end


# window main start
main = tk.Tk()
main.title("Manager Student")
main.withdraw()
# loginScreen.withdraw()

lf_table = tk.LabelFrame(main, text="Table", font=fontSmall, fg="blue")
lf_table.grid(column=0, row=1, columnspan=2)
tree = tk2.Treeview(lf_table,
                    columns=("Code", "Name", "Age", "Gender", "Address", "Math", "Physics", "Chemistry", "GPA"))
# Thêm tiêu đề cho hai cột
tree.heading("#0", text="STT")
tree.heading("Code", text="Code")
tree.heading("Name", text="Name")
tree.heading("Age", text="Old")
tree.heading("Gender", text="Gender")
tree.heading("Address", text="Address")
tree.heading("Math", text="Math")
tree.heading("Physics", text="Physics")
tree.heading("Chemistry", text="Chemistry", )
tree.heading("GPA", text="GPA")

tree.column("#0", width=50, anchor="center", )
tree.column("Code", width=100, anchor="center")
tree.column("Name", width=100, anchor="center")
tree.column("Age", width=80, anchor="center")
tree.column("Gender", width=100, anchor="center")
tree.column("Address", width=100, anchor="center")
tree.column("Math", width=80, anchor="center")
tree.column("Physics", width=80, anchor="center")
tree.column("Chemistry", width=80, anchor="center")
tree.column("GPA", width=80, anchor="center")
# Đọc dữ liệu danh sách sinh viên
list_students = read_data_student("data/list_students.txt")
ls_type_list = list_students.get_list()
# Thêm dữ liệu vào bảng
for i in range(len(ls_type_list)):
    tree.insert(parent="", index=ls_type_list[i].code, text=str(i + 1),
                values=(ls_type_list[i].return_list_value()), )
tree.pack()
tree.bind("<<TreeviewSelect>>", get_data)
# labelframe input start (right)
lf_input_user = tk.LabelFrame(main, text="Input", font=fontSmall, fg="blue")
lf_input_user.grid(column=0, row=0)

# code
lbCode = tk.Label(lf_input_user, text="Code", font=fontSmall, )
lbCode.grid(row=0, column=0, padx=5, sticky="w", pady=5)
input_code = tk.Entry(lf_input_user, width=15, font=fontInput, highlightthickness=1, highlightcolor="blue",
                      insertbackground="blue", state="readonly", borderwidth=2)
input_code.grid(row=0, column=1, padx=5, sticky="w", pady=5)

# name
lbName = tk.Label(lf_input_user, text="Name", font=fontSmall)
lbName.grid(row=1, column=0, padx=5, sticky="w", pady=5)
input_name = tk.Entry(lf_input_user, width=15, font=fontInput, highlightthickness=1, highlightcolor="blue",
                      insertbackground="blue", borderwidth=2)
input_name.grid(row=1, column=1, padx=5, sticky="w", pady=5)
input_name.bind("<Return>", on_tab_pressed)

# age
lbAge = tk.Label(lf_input_user, text="Age", font=fontSmall)
lbAge.grid(row=2, column=0, padx=5, sticky="w", pady=5)
input_age = tk.Entry(lf_input_user, width=15, font=fontInput, highlightthickness=1, highlightcolor="blue",
                     insertbackground="blue", borderwidth=2)
input_age.grid(row=2, column=1, padx=5, sticky="w", pady=5)
input_age.bind("<Return>", on_tab_pressed)

# gender
lbGender = tk.Label(lf_input_user, text="Gender(M/F)", font=fontSmall)
lbGender.grid(row=3, column=0, padx=5, sticky="w", pady=5)
# input_gender = tk.Entry(lf_input_user, width=15, font=fontInput, highlightthickness=1, highlightcolor="blue",
#                         insertbackground="blue", borderwidth=2)
cb1 = tk.BooleanVar(lf_input_user)
cb1.set(0)
ck_male = tk.Checkbutton(lf_input_user, text="", variable=cb1, onvalue=True, offvalue=False, command=check_male)
ck_male.grid(row=3, column=1, padx=5, sticky="w", pady=5, )

# Address
lbAddress = tk.Label(lf_input_user, text="Address", font=fontSmall)
lbAddress.grid(row=0, column=2, padx=5, sticky="w", pady=5)
input_address = tk.Entry(lf_input_user, width=15, font=fontInput, highlightthickness=1, highlightcolor="blue",
                         insertbackground="blue", borderwidth=2)
input_address.grid(row=0, column=3, padx=5, sticky="w", pady=5)

# math point
lb_math_point = tk.Label(lf_input_user, text="Math Point", font=fontSmall)
lb_math_point.grid(row=1, column=2, padx=5, sticky="w", pady=5)
input_math_point = tk.Entry(lf_input_user, width=15, font=fontInput, highlightthickness=1, highlightcolor="blue",
                            insertbackground="blue", borderwidth=2)
input_math_point.grid(row=1, column=3, padx=5, sticky="w", pady=5)

# physics point
lb_phys_point = tk.Label(lf_input_user, text="Physics Point", font=fontSmall)
lb_phys_point.grid(row=2, column=2, padx=5, sticky="w", pady=5)
input_phys_point = tk.Entry(lf_input_user, width=15, font=fontInput, highlightthickness=1, highlightcolor="blue",
                            insertbackground="blue", borderwidth=2)
input_phys_point.grid(row=2, column=3, padx=5, sticky="w", pady=5)

# chemistry point
lb_chem_point = tk.Label(lf_input_user, text="Chemistry Point", font=fontSmall)
lb_chem_point.grid(row=3, column=2, padx=5, sticky="w", pady=5)
input_chem_point = tk.Entry(lf_input_user, width=15, font=fontInput, highlightthickness=1, highlightcolor="blue",
                            insertbackground="blue", borderwidth=2)
input_chem_point.grid(row=3, column=3, padx=5, sticky="w", pady=5)
# labelframe input end

# labelframe button start (left)
lf_buttons = tk.LabelFrame(main, text="Option", font=fontSmall, fg="blue")
lf_buttons.grid(row=0, column=1, sticky="w")

# Button them
btn_add = tk.Button(lf_buttons, text="Add New", font=fontSmall, relief="groove", fg=mainColor, width=15)
btn_add.grid(row=0, column=0, pady=3, padx=3)
btn_add.bind("<Enter>", enter_btn_blue)
btn_add.bind("<Leave>", leave_btn)
btn_add.bind("<Button-1>", add_new_student)

# button Cap nhat
btn_update = tk.Button(lf_buttons, text="Update", font=fontSmall, relief="groove", fg=mainColor, width=15)
btn_update.grid(row=1, column=0, pady=3, padx=3)
btn_update.bind("<Enter>", enter_btn_blue)
btn_update.bind("<Leave>", leave_btn)
btn_update.bind("<Button-1>", update_student)

# button Tim Kiem
btn_find = tk.Button(lf_buttons, text="Find", font=fontSmall, relief="groove", fg=mainColor, width=15)
btn_find.grid(row=2, column=0, pady=3, padx=3)
btn_find.bind("<Enter>", enter_btn_blue)
btn_find.bind("<Leave>", leave_btn)
btn_find.bind("<Button-1>", open_wd_find)

# button Xoa
btn_delete = tk.Button(lf_buttons, text="Delete", font=fontSmall, relief="groove", fg=mainColor, width=15)
btn_delete.grid(row=0, column=1, pady=3, padx=3)
btn_delete.bind("<Enter>", enter_btn_red)
btn_delete.bind("<Leave>", leave_btn)
btn_delete.bind("<Button-1>", delete_student)

btn_clear = tk.Button(lf_buttons, text="Clear", font=fontSmall, relief="groove", fg=mainColor, width=15)
btn_clear.grid(row=1, column=1, pady=3, padx=3)
btn_clear.bind("<Enter>", enter_btn_red)
btn_clear.bind("<Leave>", leave_btn)
btn_clear.bind("<Button-1>", reset)

# labelframe button end (left)
# window main end

loginScreen.mainloop()
