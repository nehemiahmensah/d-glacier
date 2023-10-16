import tkinter
from tkinter.ttk import *

def close():
    window.destroy()
window = tkinter.Tk()
window.title("Nii first")
window.winfo_height = 300

label = tkinter.Label(window, text= "Mence")
btn = tkinter.Button(window, text = "Sign Up", bg="blue" , fg= "white",command= close )
window.geometry('500x200')
label.grid(column=1 , row = 0)
btn.place(x = 80, y=50)

combo = Combobox(window)
combo['values'] = (1,2,3,4,5,"Text")
combo.current(5)
combo.grid(column=2, row = 2)

chk_state = bool
chk_state == True
chk = Checkbutton(window, text = "Male", var = chk_state)
chk.grid(column = 4, row = 5)

rad1 = Radiobutton(window, text = "Female", value=1)
rad2 = Radiobutton(window, text = "Male", value = 2)
rad1.grid(column = 5, row = 5)
rad2.place( x =150, y = 145,)



window.mainloop()