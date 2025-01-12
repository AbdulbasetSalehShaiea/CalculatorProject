from tkinter import *  # Importing Tkinter for GUI
import os  # Importing os to set environment variables for Tcl/Tk

# Set TCL library path
os.environ['TCL_LIBRARY'] = r'C:\Users\abd\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'

# Function to handle button press
def button_press(number):
    """Append the pressed button's value to the equation."""
    global equation_text
    equation_text += str(number)
    equation_label.set(equation_text)

# Function to evaluate the expression
def equals():
    """Evaluate the mathematical expression."""
    try:
        global equation_text
        # Evaluate the expression using eval
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("Cannot divide by zero")
        equation_text = ""

# Function to clear the equation
def clear():
    """Clear the equation text."""
    global equation_text
    equation_label.set("")
    equation_text = ""

# Initialize the main window
window = Tk()
window.title("Calculator Project")
window.geometry("500x500")  # Set the size of the window

# Initialize global variables
equation_text = ""
equation_label = StringVar()  # Bind text to GUI elements

# Display for the calculator
label = Label(window, textvariable=equation_label, font=('consolas', 20), bg='wheat', width=24, height=2)
label.pack()

# Frame for the buttons
frame = Frame(window)
frame.pack()

# Button creation for numbers and operators
buttons = [
    ('1', 0, 0), ('2', 0, 1), ('3', 0, 2), ('+', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('-', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('C', 3, 0), ('0', 3, 1), ('%', 3, 2), ('/', 3, 3),
]

# Loop to add buttons dynamically
for (text, row, col) in buttons:
    if text == 'C':
        Button(frame, text=text, height=4, width=9, font=35, command=clear).grid(row=row, column=col)
    elif text == '=':
        Button(frame, text=text, height=4, width=9, font=35, command=equals).grid(row=row, column=col)
    else:
        Button(frame, text=text, height=4, width=9, font=35, command=lambda t=text: button_press(t)).grid(row=row, column=col)

# Equals button
equal_button = Button(frame, text='=', height=4, width=9, font=35, command=equals)
equal_button.grid(row=4, column=0, columnspan=4)

# Start the GUI event loop
window.mainloop()
