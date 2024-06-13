from tkinter import *

window = Tk()

num_1 = 0
num_2 = 0
op = "clear"
ans=0

window.title("__Calculator__")

e = Entry(window,width=20,borderwidth=5, font=("Robota",20))
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)


def add():
    global num_1
    num_1 = float(e.get()) 
    e.delete(0,END) 
    global op
    op = "add"

def sub():
    global num_1
    num_1 = float(e.get()) 
    e.delete(0,END) 
    global op
    op = "sub"

def mul():
    global num_1
    num_1 = float(e.get()) 
    e.delete(0,END) 
    global op
    op = "mul"

def div():
    global num_1
    num_1 = float(e.get()) 
    e.delete(0,END) 
    global op
    op = "div"

def equal():
  global num_1,num_2,ans
  num_2 = (e.get())
  if num_2 == "":
    num_2 = 0
  if op == "add":
    ans = float(num_1) + float(num_2)
  elif op == "sub":
    ans = float(num_1) - float(num_2)
  elif op == "mul":
    ans = float(num_1) * float(num_2)
  elif op == "div":
    ans = float(num_1)/float(num_2)
  e.delete(0,END)
  e.insert(END,"%.2f" % round(ans, 2))

           

def click(num):
    e.insert(END,str(num))

def clear():
    e.delete(0,END)
    global num_1,num_2,ans,op
    num_1=0
    num_2=0
    ans=0
    op=""



def decimal():
  if "." not in str(e.get()):
    e.insert(END,".")
  else:
    print("Error")


button_1 = Button(window, text=1,padx=40,pady=20,command=lambda: click(1))
button_2 = Button(window, text=2,padx=40,pady=20,command=lambda: click(2))
button_3 = Button(window, text=3,padx=40,pady=20,command=lambda: click(3))

button_4 = Button(window, text=4,padx=40,pady=20,command=lambda: click(4))
button_5 = Button(window, text=5,padx=40,pady=20,command=lambda: click(5))
button_6 = Button(window, text=6,padx=40,pady=20,command=lambda: click(6))

button_7 = Button(window, text=7,padx=40,pady=20,command=lambda: click(7))
button_8 = Button(window, text=8,padx=40,pady=20,command=lambda: click(8))
button_9 = Button(window, text=9,padx=40,pady=20,command=lambda: click(9))

button_0 = Button(window, text=0,padx=40,pady=20,command=lambda: click(0))

button_clear = Button(window, text="C",padx=30,pady=12, bg = "#e36052", font=(20),command =clear)
button_equal = Button(window, text="=",padx=40,pady=20,command=equal)

button_mul = Button(window, text="*",padx=40,pady=20,command=mul)
button_div = Button(window, text="/",padx=40,pady=20,command=div)
button_sub = Button(window, text="-",padx=40,pady=20,command=sub)
button_add = Button(window, text="+",padx=40,pady=20,command=add)

button_decimal = Button(window, text=".",padx=40,pady=20,command=decimal)


button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=1)

button_equal.grid(row=4, column=2)
button_clear.grid(row=1, column=3)

button_decimal.grid(row=4, column=0)

button_mul.grid(row=2, column=3)
button_div.grid(row=3, column=3)
button_sub.grid(row=4, column=3)
button_add.grid(row=5, column=3)


window.mainloop()