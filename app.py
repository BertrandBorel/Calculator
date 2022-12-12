# Calculator with Python

# Importations
from tkinter import *
# for square root :
from math import sqrt 


# initialization
root = Tk()

# title
root.title("Calculator")
# size
root.geometry("500x500")
root.maxsize(345,400)
root.minsize(345,400)

# background
root.config(bg = "grey")

# variables for saving input
input_str = ""
input_int = 0

# Label
label1 = Label(root, text="Calculator", bg = "grey", fg="white", font=("Arial"))
label1.grid(row=0, column=1)

# Input 
user_input = Entry(root, textvariable="", width=15)
user_input.grid(row=1, column=1, padx = 5, pady=5)



# if a button is clicked :
def button_click(number):
    result.delete(0, END)
    current = user_input.get()
    user_input.delete(0, END)
    user_input.insert(0, str(current) + str(number))


# clear the input
def clear():
    user_input.delete(0, END)
    result.delete(0, END)

# function for addition 
def addition():
    number_1 = user_input.get()
    if number_1 == "":
        number_1 = resultat
    global num_1 
    global operation
    operation = "+"
    num_1 = int(number_1)
    user_input.delete(0, END)

# function for substraction 
def substraction():
    number_1 = user_input.get()
    if number_1 == "":
        number_1 = resultat
    global num_1 
    global operation
    operation = "-"
    num_1 = int(number_1)
    user_input.delete(0, END)
 
# function for multiplication
def multiplication():
    number_1 = user_input.get()
    if number_1 == "":
        number_1 = resultat
    global num_1 
    global operation
    operation = "*"
    num_1 = int(number_1)
    user_input.delete(0, END)

# function for division
def division():
    number_1 = user_input.get()
    if number_1 == "":
        number_1 = resultat
    global num_1 
    global operation
    operation = "/"
    num_1 = int(number_1)
    user_input.delete(0, END)

#function for power
def power():
    number_1 = user_input.get()
    if number_1 == "":
        number_1 = resultat
    global num_1 
    global operation
    operation = "**"
    num_1 = int(number_1)
    user_input.delete(0, END)

# function for square root
def square_root():
    number_1 = user_input.get()
    if number_1 == "":
        number_1 = resultat
    global num_1 
    global operation
    operation = "sqrt"
    num_1 = int(number_1)
    resultat = sqrt(num_1)
    result.insert(END, resultat)
    user_input.delete(0, END)

# function for the result of operations
def equal():
    number_2 = user_input.get()
    num_2 = int(number_2)
    user_input.delete(0, END)
    global resultat
    if operation == "+":
        resultat = num_1 + num_2
    elif operation == "-":
        resultat = num_1 - num_2
    elif operation == "*":
        resultat = num_1 * num_2
    elif operation == "/":
        resultat = num_1 / num_2
    elif operation == "**":
        resultat = num_1 ** num_2
    result.insert(END, resultat)
    
   




# Add button 1 :
button1 = Button(root, text = "1", command=lambda : button_click(1), width=15  )
button1.grid(row=2, column=0,  )

# Add button 2 :
button2 = Button(root, text = "2", command=lambda : button_click(2), width=15  )
button2.grid(row=2, column=1,  )

# Add button 3 :
button3 = Button(root, text = "3", command=lambda : button_click(3), width=15  )
button3.grid(row=2, column=2,  )

# Add button 4 :
button4 = Button(root, text = "4", command=lambda : button_click(4), width=15  )
button4.grid(row=3, column=0,  )

# Add button 5 :
button5 = Button(root, text = "5", command=lambda : button_click(5), width=15  )
button5.grid(row=3, column=1,  )

# Add button 6 :
button6 = Button(root, text = "6", command=lambda : button_click(6), width=15  )
button6.grid(row=3, column=2,  )

# Add button 7 :
button7 = Button(root, text = "7", command=lambda : button_click(7), width=15  )
button7.grid(row=4, column=0,  )

# Add button 8 :
button8 = Button(root, text = "8", command=lambda : button_click(8), width=15  )
button8.grid(row=4, column=1,  )

# Add button 9 :
button9 = Button(root, text = "9", command=lambda : button_click(9), width=15  )
button9.grid(row=4, column=2,  )

# Add button dot
button_dot = Button(root, text = ".", command=lambda : button_click(), width=15  )
button_dot.grid(row=5, column=0,  )

# Add button 0 :
button0 = Button(root, text = "0", command=lambda : button_click(0), width=15  )
button0.grid(row=5, column=1,  )

# Add button clear
button_clear = Button(root, text = "clear", command=clear, width=15  )
button_clear.grid(row=5, column=2,  ) 

# Label 2 = "Operations"
label2 = Label(root, text="Operations :", bg = "grey", fg="white", font=("Arial"))
label2.grid(row=6, column=1)

# Addition :
button_add = Button(root, text = "+", command=addition, width=15  )
button_add.grid(row=7, column=0)


# Substraction :
button_sub = Button(root, text = "-", command=substraction, width=15  )
button_sub.grid(row=7, column=1)

# Multiplication 
button_mult = Button(root, text = "*", command=multiplication, width=15  )
button_mult.grid(row=7, column=2)

# Division
button_div = Button(root, text = "/", command=division, width=15  )
button_div.grid(row=8, column=0)

# Square root
button_sr = Button(root, text = "square root", command=square_root, width=15  )
button_sr.grid(row=8, column=1)

# power
button_pow = Button(root, text = "power", command=power, width=15  )
button_pow.grid(row=8, column=2)

# Result
button_result = Button(root, text = "=", command=equal, width=15  )
button_result.grid(row=9, column=1)

# Label Result
label3 = Label(root, text="Result :", bg = "grey", fg="white", font=("Arial"))
label3.grid(row=10, column=1, pady = 5)

# Result
result = Entry(root )
result.grid(row=11, column=1, )


# display
root.mainloop()