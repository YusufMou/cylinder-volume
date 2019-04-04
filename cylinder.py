# Created by: Yusuf Moussa
# Created on: 01 April 2019
# Created for: ICS3U
# Daily Assignment Unit 4-04
# This is convert levels into grades

from tkinter import *

root = Tk()
root.title("Cylinder volume calculator")
root.geometry("500x300")

Label(root, text="This is a program to calculate the volume of a cylinder").grid(row=1, column=1)

Label(root, text="Enter the radius here: ").grid(row=2, column=1)
er = Entry(root)
er.grid(row=2, column=2)

Label(root, text="Enter the height here: ").grid(row=3, column=1)
eh = Entry(root)
eh.grid(row=3, column=2)

def volume():
    radius = int(er.get()) **2
    height = int(eh.get())
    volume = 3.14 * radius * height
    Label(root, text=str(volume)).grid(row=5, column=1)


vol = Button()
vol ["text"] = "Calculate"
vol ["command"] =volume
vol.grid(row=4, column=1)






root.mainloop()