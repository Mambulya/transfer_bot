import tkinter as tk
from tkinter import messagebox

"""
        Refinement of transfer_py with GUI
        FINAL PROGRAM FORM
"""

# creating a window
WIN = tk.Tk()
WIN.title("transfer bot")

ICON = tk.PhotoImage(file='icon.png')
WIN.iconphoto(False, ICON)

WIN.geometry("800x400+475+310")
WIN.config(bg='#F6F7F9')

### a level arm
var = tk.IntVar()
scale = tk.Scale(WIN, variable=var, from_=1, to=10,
                 highlightbackground='black',
                 label="Max количество цифр после запятой:",
                 orient=tk.HORIZONTAL,
                 length=230)
scale.place(x=520,y=200)


def mycom():
    import transfer_bot_oop as bot
    number = bot.Transfer_bot(output_ten_number.get(), output_lit_number1.get(), output_lit_number.get(), scale.get())
    try:
        messagebox.showinfo("Error", number.answer_error)
    except AttributeError:
        number = number.transform_other_sys()
        answer = tk.Label(WIN, activebackground="red", text=number, fg="red", background='#F6F7F9')
        answer.place(x=610, y=150)



# #   text
label_0 = tk.Label(WIN, text='Hello', font='Calibri 25',
                   bg='#F6F7F9',
                   padx=10,
                   width=950)
# anchor = 'w')
label_1 = tk.Label(WIN, text='I am your transfer bot. I can calculate any number systems. Try! ',
                   font='15',
                   bg='#F6F7F9',
                   padx=10,
                   width=950)
instruction = tk.Label(WIN, text="Введите число:", bg='#F6F7F9')
instruction1 = tk.Label(WIN, text="с.с", bg='#F6F7F9')
result = tk.Label(WIN, text="Result:", bg='#F6F7F9')
result.place(x=610, y=130)
label_0.pack()
label_1.pack()
instruction.place(x=95, y=130)
instruction1.place(x=225, y=130)

# a button
button0 = tk.Button(WIN, text='transfer',
                    bg='#b7c8c8',
                    command=mycom)
# fg = 'white')         colour of text
button0.place(x=400, y=210)

# window folding
WIN.resizable(True, False)
WIN.minsize(600, 400)

# output window
output_ten_number = tk.Entry(WIN, width=20, bg='#b7c8c8')
output_ten_number.place(x=95, y=150)

output_lit_number = tk.Entry(WIN, width=5, bg='#b7c8c8')
output_lit_number.place(x=225, y=150)

output_lit_number1 = tk.Entry(WIN, width=5, bg='#b7c8c8')
output_lit_number1.place(x=700, y=150)

WIN.mainloop()
### ALLSOFT-28622655
