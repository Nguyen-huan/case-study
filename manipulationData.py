from student import *


def read_account(path):
    f = open(path, "r", encoding="utf-8")
    list_account = []
    for line in f:
        items = line.split("|")
        account = {
            "username": items[0],
            "password": items[1]
        }
        list_account.append(account)
    return list_account


def check_account(lst_acc, username, password):
    check = False
    for i in lst_acc:
        if i["username"] == username and i["password"] == password:
            check = True
    return check


def read_data_student(path):
    f = open(path, "r", encoding="utf-8")
    list_students = ListStudent([])
    for line in f:
        items = line.split(",")
        code = str(items[0])
        name = items[1]
        age = int(items[2])
        gender = True if items[3] == "True" else False
        address = items[4]
        math_point = float(items[5])
        physics_point = float(items[6])
        chem_point = float(items[7])
        student = Student(code, name, age, gender, address, math_point, physics_point, chem_point, )
        list_students.add_new(student)
    return list_students


def write_new_line(path, student):
    string = student.__str__()
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{string}\n")


def remove_line(path, index):
    with open(path, 'r', encoding="utf-8") as file:
        lines = file.readlines()
    del lines[index]
    with open(path, 'w', encoding="utf-8") as file:
        file.writelines(lines)


def update_line(path, index):
    with open(path, 'r', encoding="utf-8") as file:
        lines = file.readlines()
    del lines[index]
    with open(path, 'w', encoding="utf-8") as file:
        file.writelines(lines)


def update(path, index):
    with open(path, 'r') as file:
        data = file.readlines()
    data[index] = "huân "
    with open(path, 'w', encoding="utf-8") as file:
        file.writelines(data)


def write_down_file(path, list_student):
    with open(path, 'w') as file:
        for student in list_student:
            file.writelines(student.__str__()+"\n")

# remove_line("data/list_students.txt", 7)
# read_data_student("data/list_students.txt")
