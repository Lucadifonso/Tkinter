from tkinter import *
from tkinter import ttk

def set_entry(*args):
    entry_1_txt.set("CHANGE AFTER FUNCTION")

def chk_button_changed(*args):
    entry_1_txt.set(chk_but_1_txt.get())

def radio_changed(*args):
    entry_1_txt.set(radio_but_1_val.get())

def combo_changed(*args):
    entry_1_txt.set(combo_1_val.get())


root = Tk()
root.title("WIDGET EXAMPLE")
frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(column=0, row=0, sticky=(N, S, W, E))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

label_1_txt = StringVar()
label_1 = ttk.Label(frame, text='Data : ')
label_1.grid(column=1, row=1, sticky=(W, E))

label_1['textvariable'] = label_1_txt
label_1_txt.set("New Data")

entry_1_txt = StringVar()
entry_1 = ttk.Entry(frame, width=20, textvariable=entry_1_txt)
entry_1.grid(column=2, row=1, sticky=(W, S))
entry_1_txt.set(label_1_txt.get())

button_1 = ttk.Button(frame, text="click", command=set_entry)
button_1.grid(column=3, row=1, sticky=(W, E))

button_1['state'] = 'disable'
button_1['state'] = 'enable'

# from here we create the check button

chk_but_1_txt = StringVar()
chk_but_1 = ttk.Checkbutton(frame, text="HAS BEEN CHECKED",
                                command=chk_button_changed,
                                variable=chk_but_1_txt,
                                onvalue="Happy", offvalue="Sad")

chk_but_1.grid(column=4, row=1, sticky=(W, E))

# radio button

radio_but_1_val = StringVar()

red_r_but = ttk.Radiobutton(frame, text="Red",
                            variable=radio_but_1_val,
                            value="Red",
                            command=radio_changed)
blue_r_but = ttk.Radiobutton(frame, text="Blue",
                            variable=radio_but_1_val,
                            value="Blue",
                            command=radio_changed)
green_r_but = ttk.Radiobutton(frame, text="Green",
                            variable=radio_but_1_val,
                            value="Green",
                            command=radio_changed)

red_r_but.grid(column=2, row=4, sticky=(W, E))
blue_r_but.grid(column=3, row=4, sticky=(W, E))
green_r_but.grid(column=4, row=4, sticky=(W, E))

label_2 = ttk.Label(frame, text="Favorite Colour")
label_2.grid(column=2, row=3, sticky=(W, E))

# combo box - dropdown menu

combo_1_val = StringVar()
combo_1 = ttk.Combobox(frame, textvariable=combo_1_val)
label_3 = ttk.Label(frame, text="Size")
label_3.grid(column=1, row=3, sticky=(W, E))

combo_1['values']= ("small", "medium", "large")
combo_1.grid(column=2, row=3, sticky=(W, E))
combo_1.bind("<<ComboboxSelected>>", combo_changed)




root.mainloop()