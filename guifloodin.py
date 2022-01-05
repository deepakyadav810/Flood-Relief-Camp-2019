from tkinter import *

# Create Object
root = Tk()

# Set geometry
root.geometry('400x500')

# Information List
datas = []

# Add Information
def add():
	global datas
	datas.append([Name.get(),Number.get(),Gender.get(),Room.get(),address.get(1.0, "end-1c")])
	update_book()

# View Information
def view():
	Name.set(datas[int(select.curselection()[0])][0])
	Number.set(datas[int(select.curselection()[0])][1])
	Gender.set(datas[int(select.curselection()[0])][2])
	Room.set(datas[int(select.curselection()[0])][3])
	address.delete(1.0,"end")
	address.insert(1.0, datas[int(select.curselection()[0])][4])
	

# Delete Information
def delete():
	del datas[int(select.curselection()[0])]
	update_book()

def reset():
	Name.set('')
	Number.set('')
	Gender.set('')
	Room.set('')
	address.delete(1.0,"end")

# Update Information
def update_book():
	select.delete(0,END)
	for n,p,a,g,h in datas:
		select.insert(END, n)

# Add Buttons, Label, ListBox
Name = StringVar()
Number = StringVar()
Gender = StringVar()
Room = StringVar()

frame = Frame()
frame.pack(pady=10)

frame1 = Frame()
frame1.pack()

frame2 = Frame()
frame2.pack()

frame3 = Frame()
frame3.pack()

frame4 = Frame()
frame4.pack(pady=10)

Label(frame, text = 'Name', font='arial 12 bold').pack(side=LEFT)
Entry(frame, textvariable = Name,width=50).pack()

Label(frame1, text = 'Phone No.', font='arial 12 bold').pack(side=LEFT)
Entry(frame1, textvariable = Number,width=50).pack()

Label(frame2, text = 'Gender', font='arial 12 bold').pack(side=LEFT)
Entry(frame2, textvariable = Gender ,width=50).pack()

Label(frame3, text = 'Room Alloted', font='arial 12 bold').pack(side=LEFT)
Entry(frame3, textvariable = Room ,width=50).pack()

Label(frame4, text = 'Address', font='arial 12 bold').pack(side=LEFT)
address = Text(frame4,width=37,height=10)
address.pack()

Button(root,text="Add",font="arial 12 bold",command=add).place(x= 100, y=270)
Button(root,text="View",font="arial 12 bold",command=view).place(x= 100, y=310)
Button(root,text="Delete",font="arial 12 bold",command=delete).place(x= 100, y=350)
Button(root,text="Reset",font="arial 12 bold",command=reset).place(x= 100, y=390)

scroll_bar = Scrollbar(root, orient=VERTICAL)
select = Listbox(root, yscrollcommand=scroll_bar.set, height=12)
scroll_bar.config (command=select.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
select.place(x=200,y=260)

# Execute Tkinter
root.mainloop()
