import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# function บวก
def add(obj1,obj2):
  return obj1+obj2
# function ลบ
def subtract(obj1,obj2):
  return obj1-obj2
# function คูณ
def multiply(obj1,obj2):
  return obj1 * obj2
#function หาร
def divide(obj1,obj2):
  return obj1 / obj2
#function รับ พวกเครื่องหมายมา เพื่อใช้ในการหาค่า
def add_to_cal(symbol):
  current = e1.get()
  e1.delete(0,tk.END)
  e1.insert(0,current+str(symbol))
# function เครียร์ ค่าที่รับมา
def clear_entry():
  e1.delete(0,tk.END)
# function ลบค่า ด้านหลังสุด
def delete_last():
  current = e1.get()
  e1.delete(0,tk.END)
  e1.insert(0,current[:-1])
# function คำนวณ 
def calculate():
  try:
    expression = e1.get()
    expression = expression.replace('X','*') # แทน ค่า X เปลี่ยนเป็น * 
    result = eval(expression)
    e1.delete(0,tk.END)
    e1.insert(0,str(result))
  except Exception as e:
    messagebox.showerror("Error","Invalid input ")

  
root = tk.Tk()

label1 = tk.Label(root,text="Calculator")
label1.pack()

e1 = tk.Entry(root)
e1.pack()

b1 = tk.Button(root,text="(",command=lambda:add_to_cal("("))
b1.pack(side="left")

b2 = tk.Button(root,text=")",command=lambda:add_to_cal(")"))
b2.pack(side="left")

b3 = tk.Button(root,text="C",command=clear_entry)
b3.pack(side="left")

b4 = tk.Button(root,text="/",command=lambda:add_to_cal("/"))
b4.pack(side="left")

b5 = tk.Button(root,text="7",command=lambda:add_to_cal("7"))
b5.pack(side="left")

b6 = tk.Button(root,text="8",command=lambda:add_to_cal("8"))
b6.pack(side="left")

b7 = tk.Button(root,text="9",command=lambda:add_to_cal("9"))
b7.pack(side="left")

b8 = tk.Button(root,text="X",command=lambda:add_to_cal("X"))
b8.pack(side="left")

b9 = tk.Button(root,text="4",command=lambda:add_to_cal("4"))
b9.pack(side="left")

b10 = tk.Button(root,text="5",command=lambda:add_to_cal("5"))
b10.pack(side="left")

b11 = tk.Button(root,text="6",command=lambda:add_to_cal("6"))
b11.pack(side="left")

b11 = tk.Button(root,text="+",command=lambda:add_to_cal("+"))
b11.pack(side="left")

b12 = tk.Button(root,text="1",command=lambda:add_to_cal("1"))
b12.pack(side="left")

b13 = tk.Button(root,text="2",command=lambda:add_to_cal("2"))
b13.pack(side="left")

b14 = tk.Button(root,text="3",command=lambda:add_to_cal("3"))
b14.pack(side="left")

b15 = tk.Button(root,text="-",command=lambda:add_to_cal("-"))
b15.pack(side="left")

b16 = tk.Button(root,text="0",command=lambda:add_to_cal("0"))
b16.pack(side="left")

b17 = tk.Button(root,text=".",command=lambda:add_to_cal("."))
b17.pack(side="left")

b18 = tk.Button(root,text="<-",command=delete_last)
b18.pack(side="left")

b19 = tk.Button(root,text="=",command=calculate)
b19.pack(side="left")





root.mainloop()