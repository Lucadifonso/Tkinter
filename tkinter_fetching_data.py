from tkinter import *

# name contact and address

window = Tk()
window.title("Give me your information")
window.geometry("300x150")

def do():
    name = name_entry.get()
    phone = phone_entry.get()

    window_2 = Tk()
    window_2.title("Fetched information")
    window_2.geometry("300x150")
    label_fetched_name = Label(window_2,text=("Name: "+name))
    label_fetched_name.pack(anchor="c")
    label_fetched_contact = Label(window_2, text=("Phone: "+ phone))
    label_fetched_contact.pack(anchor="c")

    window.destroy()

    window_2.mainloop()




name_label = Label(window, text="Insert is your name: ", fg="red", font="courier")
name_label.pack(anchor="c")
name_entry = Entry(window)
name_entry.pack(anchor="c")
phone_label = Label(window, text="Insert is your phone number: ", fg="red", font="courier")
phone_label.pack(anchor="c")
phone_entry = Entry(window)
phone_entry.pack(anchor="c")


# adding a button

Button_1 = Button(window, text="Send the info",command = do)
Button_1.pack(anchor="c")


# put window in a loop
window.mainloop()