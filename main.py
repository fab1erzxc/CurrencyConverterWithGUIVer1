import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title('Currency Converter')
root.geometry('500x500')

# Create tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)

# Create frames
currency_frame = Frame(my_notebook, width=480, height=480)
conversion_frame = Frame(my_notebook, width=480, height=480)

currency_frame.pack(fill="both", expand=1)
conversion_frame.pack(fill="both", expand=1)

# Add tabs
my_notebook.add(currency_frame, text="Currencies")
my_notebook.add(conversion_frame, text="Convert")

# disable 2nd tab
my_notebook.tab(1, state="disabled")


#######################
# CURRENCY STUFF
#######################

def lock():
    if not home_entry.get() or not conversion_entry.get() or not rate_entry.get():
        messagebox.showwarning("Warning!", "You didn't fill out all the fields!")
    else:
        # disable entry boxes
        home_entry.config(state="disabled")
        conversion_entry.config(state="disabled")
        rate_entry.config(state="disabled")
        # enable 2nd tab
        my_notebook.tab(1, state="normal")
        # change tab fields
        amount_label.config(text=f"Amount of {home_entry.get()} to convert to {conversion_entry.get()}")
        converted_label.config(text=f"Equals this many {conversion_entry.get()}")
        convert_button.config(text=f"Convert from {home_entry.get()}")


def unlock():
    # enable entry boxes
    home_entry.config(state="normal")
    conversion_entry.config(state="normal")
    rate_entry.config(state="normal")
    # disable 2nd tab
    my_notebook.tab(1, state="disabled")


home = LabelFrame(currency_frame, text="Your home currency")
home.pack(pady=20)

# Home currency entry box
home_entry = Entry(home, font=("Helvetica", 24))
home_entry.pack(pady=10, padx=10)

# Conversion currency frame
conversion = LabelFrame(currency_frame, text="Conversion currency")
conversion.pack(pady=20)

# Convert to label
conversion_label = LabelFrame(conversion, text="Currency to convert to...")
conversion_label.pack(pady=10)

# convert to entry
conversion_entry = Entry(conversion, font=("Helvetica", 24))
conversion_entry.pack(pady=10, padx=10)

# rate label
rate_label = LabelFrame(conversion, text="Current conversion rate...")
rate_label.pack(pady=10)

# rate entry
rate_entry = Entry(conversion, font=("Helvetica", 24))
rate_entry.pack(pady=10, padx=10)

# Button frame
button_frame = Frame(currency_frame)
button_frame.pack(pady=20)

# create buttons
lock_button = Button(button_frame, text="Lock", command=lock)
lock_button.grid(row=0, column=0, padx=10)

unlock_button = Button(button_frame, text="Unlock", command=unlock)
unlock_button.grid(row=0, column=1, padx=10)


#######################
# CONVERT STUFF
#######################

def convert():
    # clear converted entry box
    converted_entry.delete(0, END)

    # convert
    convert = float(rate_entry.get()) * float(amount_entry.get())
    # 2 decimals
    convert = round(convert, 2)
    # add commas
    convert = '{:,}'.format(convert)
    # update entry box
    converted_entry.insert(0, convert)


def clear():
    amount_entry.delete(0, END)
    converted_entry.delete(0, END)


amount_label = LabelFrame(conversion_frame, text="Amount to convert")
amount_label.pack(pady=20)

# entry box for amount
amount_entry = Entry(amount_label, font=("Helvetica", 24))
amount_entry.pack(pady=10, padx=10)

# convert button
convert_button = Button(amount_label, text="Convert", command=convert)
convert_button.pack(pady=20)

# equals frame
converted_label = LabelFrame(conversion_frame, text="Converted currency")
converted_label.pack(pady=20)

# converted entry
converted_entry = Entry(converted_label, font=("Helvetica", 24), bd=0, bg="systembuttonface")
converted_entry.pack(pady=10, padx=10)

# clear button
clear_button = Button(conversion_frame, text="Clear", command=clear)
clear_button.pack(pady=20)

# fake label for spacing
spacer = Label(conversion_frame, text="", width=69)
spacer.pack()

root.mainloop()

# from_currency = str(input("Enter in the currency you'd like to convert from: ")).upper()
# to_currency = str(input("Enter in the currency you'd like to convert to: ")).upper()
# amount = float(input("Enter in the amount of money: "))
# response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")
# print(f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")
