from tkinter import *
from tkinter import ttk

def instruction():
	fonLabel = ("Verdana", 13, "italic")
	fonHeader = ("Times New Roman", 30 ,"bold italic")
	fonTit = ("Times New Roman", 20 ,"bold italic")
	top = Toplevel()
	top.geometry("1920x1080")
	top.state('zoomed')
	top.configure(bg='#000000')
	p1 = PhotoImage(file='bar1.png')
	top.iconphoto(False,p1)

	screen = Frame(top,width=800, height=800, bg='black')
	screen.grid(row=0, column=0, padx=10, pady=5)

	header = Message(screen, text="⚜️ INSTRUCTIONS ⚜️", font=fonHeader,aspect=1000,bg='black',fg='medium sea green')
	header.grid(row=0, column=0, padx=10, pady=10, sticky="")

	info = Message(screen, text="Instruction Related to Buttons :- ",font=fonTit,aspect=1000,bg='black',fg='gold')
	info.grid(row=1, column=0, padx=10, pady=10, sticky=W)

	generate = Message(screen, text="GENERATE Button :- \nClicking this Button Generates an Array of Bars randomly. \n\nINFORMATION Button :- \nClicking this Button shows a window with Information related to the Sorting Algorithms. \n\nSTART Button :- \nClicking this Button Starts the Sorting Process.", font=fonLabel, aspect=1000,bg='black',fg='IndianRed1')
	generate.grid(row=2, column=0, padx=10, pady=10, sticky=W)

	color = Message(screen, text="Color Scheme for Sorting Algorithms :- ",font=fonTit,aspect=1000,bg='black',fg='gold')
	color.grid(row=3, column=0, padx=10, pady=10, sticky=W)

	bubble = Message(screen, text="Bubble Sort :- \nDark Blue :- Swapping is not Required \nYellow :- Swappping is Required \nRed :- Elements are Swapped \nGreen :- Successfully Sorted", font=fonLabel, aspect=1000,bg='black',fg='red')
	bubble.grid(row=4, column=0, padx=10, pady=10, sticky=W)

	insertion = Message(screen, text="Insertion Sort :- \nDark Blue :- Selected Element \nYellow :- Elements needs to be swapped \nRed :- Elents swapped Cuccessfully  \nGreen :- Successfully Sorted", font=fonLabel, aspect=1000,bg='black',fg='green2')
	insertion.grid(row=5, column=0, padx=10, pady=10, sticky=W)

	merge = Message(screen, text="Merge Sort :- \nDark Blue :- Elements Smaller than Middle element \nYellow :- The Middle Element \nRed:- Elements Greater than Middle Element \nGreen :- Successfully Sorted", font=fonLabel, aspect=1000,bg='black',fg='magenta2')
	merge.grid(row=6, column=0, padx=10, stick=W)