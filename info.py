from tkinter import *
from tkinter import ttk
from tkinter.tix import *

def info():
	fonLabel = ("Verdana", 13, "italic")
	fonHeader = ("Times New Roman", 30 ,"bold italic")
	top = Toplevel()
	top.geometry("1920x1080")
	top.state('zoomed')
	top.configure(bg='#000000')
	p1 = PhotoImage(file='bar1.png')
	top.iconphoto(False,p1)

	screen = Frame(top,width=800, height=800, bg='black')
	screen.grid(row=0, column=0, padx=10, pady=5)


	header = Message(screen, text="⚜️ ALGORITHM INFORMATION ⚜️", font=fonHeader,aspect=1000,bg='black',fg='medium sea green')
	header.grid(row=0, column=0, padx=10, pady=10, sticky="")

	bubble = Message(screen, text="BUBBLE SORT :- \nBubble sort is a simple sorting algorithm. This sorting algorithm is comparison-based algorithm in which each pair of adjacent elements is compared and the elements are swapped if they are not in order. This algorithm is not suitable for large data sets.\n\n Time Complexity :- \n Worst Case :-     O(n^2) \n Average Case :- O(n^2) \n Best Case :-      O(n) \n\n Space Complexity :- O(1)",font=fonLabel,aspect=1000,bg='black',fg='red')
	bubble.grid(row=1, column=0, padx=10, pady=10,sticky=W)

	insertion = Message(screen, text="INSERTION SORT :-   \nThis is an in-place comparison-based sorting algorithm. Here, a sub-list is maintained which is always sorted. For example, the lower part of an array is maintained to be sorted. An element which is to be 'insert'ed in this sorted sub-list, has to find its appropriate place and then it has to be inserted there. Hence the name, insertion sort.The array is searched sequentially and unsorted items are moved and inserted into the sorted sub-list (in the same array). This algorithm is not suitable for large data sets. \n\n Time Complexity :- \n Worst Case :-    O(n^2) \n Average Case :- O(n^2) \n Best Case :-      O(n) \n\n Space Complexity :- O(1)",font=fonLabel,aspect=1000,bg='black',fg='green2')
	insertion.grid(row=2, column=0, padx=10, pady=10,sticky=W)

	merges = Message(screen, text= "MERGE SORT :- \nMerge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. \n\n Time Complexity :-  \n Worst Case :-    O(nlog(n)) \n Average Case :- O(nlog(n)) \n Best Case :-      O(nlog(n)) \n\n Space Complexity :- O(n)",font=fonLabel,aspect=1000,bg='black',fg='magenta2')
	merges.grid(row=3, column=0, padx=10, pady=10,sticky=W)

	# 📊