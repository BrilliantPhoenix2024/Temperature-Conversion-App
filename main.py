import tkinter as tk

window = tk.Tk()

lbl_farenhite = tk.Label(
    master=window,
    text='Farenhite:',
)

ent_farenhite = tk.Entry(
    master=window
)

btn_calc = tk.Button(
    master=window,
    text='Calc',
)

lbl_farenhite.grid(row=0, column=0)
ent_farenhite.grid(row=0, column=1)
btn_calc.grid(row=0, column=2)


window.mainloop()