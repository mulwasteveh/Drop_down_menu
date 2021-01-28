from tkinter import *
import tkinter

top = Tk()
top.geometry("400x400")
top.configure(background="#FFFF00")

mb=  Menubutton ( top, text="NAME", relief=RAISED )
mb.grid()
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu

steveVar = IntVar()
mulwaVar = IntVar()

mb.menu.add_checkbutton ( label="STEVE",
                          variable=steveVar )
mb.menu.add_checkbutton ( label="mulwa",
                          variable=mulwaVar )

mb.pack()
top.mainloop()