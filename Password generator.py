from tkinter import *
import random
import string

window = Tk()

window.title("__Password Generator__")
window.config(background="#07b6eb")



num = BooleanVar()
special = BooleanVar()
repeat = BooleanVar()

#Length of Password entry
e = Entry(window,
          width=5,
          borderwidth=5, 
          font=("Sans serif",15),
          background="black",
          foreground="#f2f2eb")
e.grid(row=0,column=2,columnspan=2,padx=10,pady=10)



#result area
result = Entry(window,
               width=30,
               borderwidth=2,
               background="black",
               foreground="green", 
               font=("Sans serif",15))
result.grid(row=7,column=0,columnspan=4,padx=10,pady=10)


#To create gap
labelText=StringVar() #To create gap
labelText.set("")
label_entry=Label(window, 
                  textvariable=labelText, 
                  height=4,
                  background="#07b6eb")
label_entry.grid(row=4, column = 0, columnspan= 2 )




#label  for the length entry box
labelText=StringVar()
labelText.set("Enter Password Length :")
label_entry=Label(window, 
                  textvariable=labelText,
                  background="#07b6eb",
                  foreground="White", 
                  height=2,
                  font=("Sans serif",10))
label_entry.grid(row=0, column = 0, columnspan= 2 )

# Checkboxes
num_box = Checkbutton(window, 
                      text = "Include Numbers",
                      variable = num, 
                      onvalue=True, 
                      offvalue=False, 
                      background="#07b6eb",
                      activebackground="#07b6eb")
special_box = Checkbutton(window, 
                          text="Include Special Character", 
                          variable= special, 
                          onvalue=True, 
                          offvalue=False,
                          background="#07b6eb",
                          activebackground="#07b6eb")
repeat_box = Checkbutton(window, 
                         text="Repeat letters", 
                         variable= repeat, 
                         onvalue=True, 
                         offvalue=False,
                         background="#07b6eb",
                         activebackground="#07b6eb")

num_box.grid(row = 2,column= 1, columnspan=4)
special_box.grid(row = 3,column= 1, columnspan=4)
repeat_box.grid(row = 4,column= 1, columnspan=4)
#

numbers = num.get()
special_char= special.get()
repeat_letters= repeat.get()



def generate_password(length):
    global numbers
    global special_char
    global repeat_letters

    char_used = string.ascii_letters

    if numbers:
        char_used += string.digits
    if special_char:
        char_used += string.punctuation
    
    password=""

    meets_criteria = False

    while len(password) < length:
        new_char = random.choice(char_used)
        if not(repeat_letters):
            if new_char in password:
                continue
        password += new_char
    return password

def submit():
    global num
    global special
    global repeat
    global numbers
    global special_char
    global repeat_letters
    global length
    global e
    try:
        length = int(e.get())
    except:
        length = 10
    numbers = num.get()
    special_char= special.get()
    repeat_letters= repeat.get()
    result.delete(0,END)
    result.insert(0, generate_password(length))

generate = Button(window, 
                  text="Generate Password",
                  padx=20,
                  pady=10,
                  width = 30,
                  background="#b81616",
                  foreground="white",
                  font=("Sans serif",10), 
                  command=submit)
generate.grid(row=6, column=0, columnspan=4)


window.mainloop()
