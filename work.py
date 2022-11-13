from tkinter import *
from tkinter import ttk
import datetime
import pickle

root = Tk()
root.title('Doko tekistil')
#root.iconbitmap()
root.geometry("300x500")

# Creating a list
number = [
	"10",
	"20",
	"30",
	"40",
	"50",
	"60",
	"70",
	"80",
	"90",
	"100"	
]

todaydate = datetime.datetime.now()
format_date = todaydate.strftime("%a, %m,%d ,%Y ")



label_1 = Label(root, text="Guluk urun cikis")
label_1.pack()

date_l= Label(root, text=format_date)
date_l.pack(pady=5, anchor=W)



frame_1 = Frame(root)
frame_1.pack(pady=10)

label_2 = Label(frame_1, text='8:00-10:00')
label_2.grid(row=0,column=0)

entry_1 = Entry(frame_1, width=8)
entry_1.grid(row=1, column=0,pady=5,padx=5)

label_3 = Label(frame_1, text='10:15-13:00')
label_3.grid(row=0,column=1, padx = 10)

entry_2 = Entry(frame_1, width=8)
entry_2.grid(row=1, column=1,pady=5,padx=5)

label_4 = Label(frame_1, text='14:00-16:00')
label_4.grid(row=0,column=2, padx = 10)

entry_3 = Entry(frame_1, width=8)
entry_3.grid(row=1, column=2,pady=5,padx=5)

label_5 = Label(frame_1, text='16:15-18:30')
label_5.grid(row=0,column=3)

entry_4 = Entry(frame_1, width=8)
entry_4.grid(row=1, column=3,pady=5,padx=5)

def save():
	stuff = entry_1.get()
	filename = "datfile/dat_stuff"

	# Open file
	output_file = open(filename, 'wb')

	# Add data to the file
	pickle.dump(stuff, output_file)

	# rec_label.config(text="8:00-10:00" + entry_1.get())
	entry_1.delete(0, END)
	save()
	
def show():
	filename = "datfile/dat_stuff"

	# Open file
	input_file = open(filename, 'rb')

	# Load the data from file to a variable
	stuff = pickle.load(input_file)
	rec_label.config(text=stuff)

# Save button
save_btn = Button(root, text='Kid et', font=("Helvatica", 15), command=save)
save_btn.pack(pady=20)

show_btn = Button(root, text='toplam Goster', font=("Helvatica", 15), command=show)
show_btn.pack(pady=20)



# show record Label
rec_label= Label(root, text="", font=('Helvtica', 20))
rec_label.pack( pady=20)



root.mainloop()
