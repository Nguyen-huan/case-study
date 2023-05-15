# from tkinter import *
# from tkinter import ttk
#
# root = Tk()
#
# # Tạo Treeview
# treeview = ttk.Treeview(root, columns=("name", "age", "gender"), selectmode="extended")
# treeview.heading("#0", text="ID")
# treeview.heading("name", text="Name")
# treeview.heading("age", text="Age")
# treeview.heading("gender", text="Gender")
# treeview.column("#0", width=50)
# treeview.column("name", width=100)
# treeview.column("age", width=50)
# treeview.column("gender", width=50)
# treeview.pack()
#
# # Thêm item
# treeview.insert("", "end", text="001", values=("John Doe", "25", "Male"))
# treeview.insert("", "end", text="002", values=("Jane Smith", "30", "Female"))
#
#
# def get_selected_item(event):
#     # Lấy danh sách các item được chọn
#     selected_items = treeview.selection()
#     # Nếu không có item nào được chọn thì không làm gì cả
#     if len(selected_items) == 0:
#         return
#
#     # Lấy thông tin của item đầu tiên được chọn
#     selected_item = selected_items[0]
#     item_text = treeview.item(selected_item)["text"]
#     item_values = treeview.item(selected_item)["values"]
#
#     # Hiển thị thông tin của item được chọn
#     print(f"Selected item: {item_text}")
#     print(f"Values: {item_values}")
#
#
# # Gán sự kiện selection cho Treeview
# treeview.bind("<<TreeviewSelect>>", get_selected_item)
#
# root.mainloop()
#
#
#
#
#
import tkinter as tk
import tkinter.ttk as ttk

# Tạo một cửa sổ
window = tk.Tk()
window.geometry("300x200")

# Tạo một TreeView widget
tree = ttk.Treeview(window)

# Thêm các cột vào TreeView
tree["columns"] = ("Name", "Age", "Gender")

# Đặt tên cho các cột
tree.column("#0", width=0, stretch=tk.NO)
tree.column("Name", anchor=tk.CENTER, width=100)
tree.column("Age", anchor=tk.CENTER, width=50)
tree.column("Gender", anchor=tk.CENTER, width=50)

# Đặt tiêu đề cho các cột
tree.heading("#0", text="", anchor=tk.CENTER)
tree.heading("Name", text="Name", anchor=tk.CENTER)
tree.heading("Age", text="Age", anchor=tk.CENTER)
tree.heading("Gender", text="Gender", anchor=tk.CENTER)

# Thêm các hàng vào TreeView
tree.insert("", tk.END, text="1", values=("Alice", 25, "Female"))
tree.insert("", tk.END, text="2", values=("Bob", 30, "Male"))
tree.insert("", tk.END, text="3", values=("Charlie", 35, "Male"))

# Đặt trọng tâm vào hàng thứ 2 (index = 1)
tree.focus(tree.get_children()[1])

# Hiển thị TreeView widget
tree.pack()

window.mainloop()
