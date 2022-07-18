import tkinter as tk

window = tk.Tk()

farenhite_val = tk.StringVar()

lbl_result = tk.Label(
    master=window,
    text='Enter your number...'
)


def convert_farenhit_to_celsius(*args):
    farenhit_input = farenhite_val.get()
    try:                           # Convert to celsius
        farenhite_value = float(farenhit_input)
        lbl_result['text'] = (farenhite_value-32)*5/9
    except ValueError:
        if farenhit_input != '':    # if user input is not Valid
            lbl_result['text'] = 'Invalid input.Please enter a Number.'
        else:                      # if user input is Empty
            lbl_result['text'] = 'Your input is Empty.Please enter a Number.' 
              
              
lbl_farenhite = tk.Label(
    master=window,
    text='Farenhite:',
)

ent_farenhite = tk.Entry(
    master=window,
    width=50,
    textvariable=farenhite_val,
)

btn_calc = tk.Button(
    master=window,
    text='Calc',
    command=convert_farenhit_to_celsius,
)

lbl_farenhite.grid(row=0, column=0, padx=10, pady=10)
ent_farenhite.grid(row=0, column=1)
btn_calc.grid(row=0, column=2, padx=10, pady=10)

lbl_celsius = tk.Label(
    master=window,
    text='Celsius:',
)


lbl_celsius.grid(row=1, column=0, pady=(10, 20))
lbl_result.grid(row=1, column=1, pady=(10, 20))

window.bind('<Return>', convert_farenhit_to_celsius)
window.title("Atefeh's first app")
window.mainloop()