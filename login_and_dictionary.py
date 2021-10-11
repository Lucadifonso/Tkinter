from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("300x150")
window.title("LOGIN")


users = { 'user1' : 'pass1',
          'user2' : 'pass2',
          'user3' : 'pass3',
          'user4' : 'pass4',
          'user5' : 'pass5'
          }


def log_in():
    username = user_entry.get()
    password = pass_entry.get()
    check = 0



    for k,v in users.items():
        if k == username and v == password:
            messagebox.showinfo("Congratulations", "You do have an account",)
            check = 1
            break

    if check == 0:
        messagebox.showerror("ERROR", "Dang!!! You do not have an account")




user_label = Label(window,text="enter username")
user_label.pack(anchor="c")
user_entry = Entry(window)
user_entry.pack(anchor="c")

pass_label = Label(window, text="enter password")
pass_label.pack(anchor="c")
pass_entry = Entry(window)
pass_entry.pack(anchor="c")

button = Button(window, text="Log In", command=log_in)
button.pack(anchor="c")

window.mainloop()