from tkinter import *
from tkinter.ttk import *

##### classes & functions #####

def collatz():
    values = []
    num = int(number.get())
    while num > 1:
        if num % 2 == 0:
            num = num // 2
            values.append(str(num))

        elif num % 2 == 1:
            num = 3 * num + 1
            values.append(str(num))

        elif num == 1:
            values.append("1")

    value = "res = " + str(number.get()) + " " + " ".join(values)
    res.configure(text=value)

    

##### main window #####

root = Tk()
root.geometry("450x350")
root.title("Collatz operation")

##### labels, buttons and entry #####

Label(root, text="Collatz operation", font="Poppins 17 bold").pack()

number = Entry(root)
number.pack(pady=10, ipadx=50)

res = Label(root, text="", font="Poppins 10", width=200)
res.pack()

Button(root, text="calculate", command=collatz).pack(side=BOTTOM)

##### running the window #####

root.mainloop()
