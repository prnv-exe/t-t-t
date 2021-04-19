from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('tic-tac-toe')
root.config(bg='black')
icon = ImageTk.PhotoImage(Image.open('icon.png'))
root.iconphoto(False, icon)

circle = ImageTk.PhotoImage(Image.open('circle.png'))
cross = ImageTk.PhotoImage(Image.open('cross.jpg'))
blank = ImageTk.PhotoImage(Image.open('black.jpg'))

x =  blank

ci_indicator = True
cr_indicator = False


def change(y):
	global ci_indicator, cr_indicator, circle, cross, label
	if ci_indicator == True:
		y.config(image=circle)
		ci_indicator = False
		cr_indicator = True
		y.config(command=0)
		label.config(text="cross's turn") 
	elif cr_indicator == True:
		y.config(image = cross)
		ci_indicator = True
		cr_indicator= False
		y.config(command=0)
		label.config(text="circle's turn")
	else:
		pass

button_1 = Button(root, text='1', image=x, command = lambda: change(button_1), borderwidth=0)
button_2 = Button(root, image=x, command = lambda: change(button_2), borderwidth=0)
button_3 = Button(root, image=x, command = lambda: change(button_3), borderwidth=0)
button_4 = Button(root, image=x, command = lambda: change(button_4), borderwidth=0)
button_5 = Button(root, image=x, command = lambda: change(button_5), borderwidth=0)
button_6 = Button(root, image=x, command = lambda: change(button_6), borderwidth=0)
button_7 = Button(root, image=x, command = lambda: change(button_7), borderwidth=0)
button_8 = Button(root, image=x, command = lambda: change(button_8), borderwidth=0)
button_9 = Button(root, image=x, command = lambda: change(button_9), borderwidth=0)
label = Label(root, text="circle's turn")


button_1.grid(row=0, column=0)
button_2.grid(row=0, column=1)
button_3.grid(row=0, column=2)
button_4.grid(row=1, column=0)
button_5.grid(row=1, column=1)
button_6.grid(row=1, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
label.grid(row=3, column=0, columnspan=3, ipadx=116)

root.mainloop()
