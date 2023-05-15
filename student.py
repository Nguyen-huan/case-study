import random


class Student:
    def __init__(self, code, name, age, gender, address, math_point, phy_point, chem_point):
        self.code = code
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.math_point = math_point
        self.phy_point = phy_point
        self.chem_point = chem_point
        self.GPA = round((math_point + phy_point + chem_point) / 3, 2)

    def update_student(self, student):
        self.name = student.name
        self.age = student.age
        self.gender = student.gender
        self.address = student.address
        self.math_point = student.math_point
        self.phy_point = student.phy_point
        self.chem_point = student.chem_point
        self.GPA = student.GPA

    def get_code(self):
        return self.code

    def show(self):
        show_str = f"{self.code}, {self.name}, {str(self.age)}, {self.gender}, {self.address}, {str(self.math_point)}, {str(self.phy_point)}, {str(self.chem_point)}"
        print(show_str)

    def return_list_value(self):
        list_items = []
        list_items.append(str(self.code))
        list_items.append(self.name)
        list_items.append(self.age)
        list_items.append(self.gender)
        list_items.append(self.address)
        list_items.append(self.math_point)
        list_items.append(self.phy_point)
        list_items.append(self.chem_point)
        list_items.append(self.GPA)
        return list_items

    def __str__(self):
        return f"{self.code},{self.name},{self.age},{self.gender},{self.address},{self.math_point},{self.phy_point},{self.chem_point},{self.GPA},"


class ListStudent:
    def __init__(self, lst_student=[]):
        self.lst_student = lst_student

    def add_new(self, student):
        self.lst_student.append(student)
        return student

    def remove_student(self, student):
        self.lst_student.remove(student)

    def show(self):
        for student in self.lst_student:
            student.show()

    def find_student_code(self, code):
        for index in range(len(self.lst_student)):
            if self.lst_student[index].code == code:
                return index
        return -1

    def update_list(self, code, new_value):
        for student in self.lst_student:
            if student.code == code:
                student.update_student(new_value)

    def __len__(self):
        return len(self.lst_student)

    def get_list(self):
        return self.lst_student
