# import numpy as np
import random
from tkinter import *
from tkinter import ttk
from colors import *
from bubble import Bubble
from info import info
from instruction import instruction
from merge_sort import *
from insertion import *


app = Tk()
app.title("AlgoViz")
app.geometry("1920x1080")
app.state('zoomed')
app.configure(bg='#000000')

p1 = PhotoImage(file='bar1.png')
app.iconphoto(False,p1)


fonTitle = ("Times New Roman", 30 ,"bold")
fonLabel = ("Verdana", 15, "bold")
fonCombo = ("Helvetica",15, "bold")
fonBar = ("Helvetica",13, "bold")

algo = StringVar()
algo_options = ['Bubble Sort', 'Merge Sort',
                'Insertion Sort']

speed = StringVar()
speed_options = ["Slow", "Normalized", "Fast"]



def array_generate():
    global array
    size = int(length.get())
    # array = np.random.randint(20,600,size)
    array = random.sample(range(20,600),size)
    barDraw(array, [turquoise for _ in range(len(array))])


def barDraw(array,colorfill):
    canvas.delete("all")
    canvas_h = 550
    canvas_w = 800
    bar_w = canvas_w/(len(array))

    #Referencing from top left corner to Bottom Right corner
    for i, height in enumerate(array):
        y0 = 0
        x0 = (bar_w*i)

        y1 = height
        x1 = (bar_w*(i+1))

        canvas.create_rectangle(x0,y0,x1,y1, fill=colorfill[i])
        canvas.create_text(x0+3,y0, anchor = NW, text=str(array[i]), font=fonBar)

    app.update_idletasks()


def speed():
    if(menu1.get()=="Slow"):
        return 2
    elif(menu1.get()=="Fast"):
        return 0
    else:
        return 0.099


def algo_perform():
    global array
    timediff = speed()
    if(menu2.get()=="Bubble Sort"):
        Bubble(array, barDraw, timediff)
        

    elif(menu2.get()=="Merge Sort"):
        merge_sort(array,0,len(array)-1,barDraw,timediff)
        

    elif(menu2.get()=="Insertion Sort"):
        insertion_sort(array, barDraw, timediff)


canvas = Canvas(app,width=1000, height=700,bg="black", bd=0,highlightthickness=0)
canvas.grid(row=0, column=1, padx=200, pady=60)


screen = Canvas(app,width=600, height=800, bg="grey25")
screen.grid(row=0, column=0, padx=10, pady=5)


title = Label(screen, text="⚜ AlgoViZ ⚜️", font = fonTitle, bg="plum1", fg="DarkOrchid4", borderwidth = 6, relief="sunken")
title.grid(row=0, column = 0, padx=10, pady=10,sticky=W)

instructionButton = Button(screen, command=instruction, text="INSTRUCTIONS", font = fonCombo, bg="yellow green")
instructionButton.grid(row=1, column=0, padx=10, pady=10,sticky=W)


lenlabel = Label(screen, text="Select Length :-",font=fonLabel,bg="grey25",fg='LightGoldenrod1')
lenlabel.grid(row=2, column=0, padx=10, pady=10,sticky=W)


length = Scale(screen, from_=10, to=300, resolution=1, orient=HORIZONTAL, length=300, label="Array Length",troughcolor="grey25",width=10)
length.grid(row=3, column=0, padx=10, pady=10,sticky=W)


label = Label(screen, text="Select Speed :-",font=fonLabel,bg="grey25",fg='LightGoldenrod1')
label.grid(row=4, column=0, padx=10, pady=10,sticky=W)


menu1 = ttk.Combobox(screen, textvariable=algo, values=speed_options, font = fonCombo)
menu1.grid(row=5, column=0, padx=10, pady=10,sticky=W)
menu1.current(0)


label1 = Label(screen, text = "Select Algorithm :-",font=fonLabel, bg="grey25",fg='LightGoldenrod1')
label1.grid(row=6, column=0, padx=10, pady=10, sticky=W)


menu2 = ttk.Combobox(screen, textvariable=speed, values = algo_options, font = fonCombo)
menu2.grid(row=7, column=0, padx=10, pady=10,sticky=W)
menu2.current(0)


button1 = Button(screen, command=array_generate, text="GENERATE ARRAY", font = fonCombo, bg="cyan")
button1.grid(row=8, column=0, padx=10, pady=10,sticky=W)


button2 = Button(screen, command=info, text="INFORMATION", font = fonCombo, bg="yellow")
button2.grid(row=9, column=0, padx=10, pady=10,sticky=W)


button3 = Button(screen, command=algo_perform, text="START", font = fonCombo, bg="steel blue")
button3.grid(row=10, column=0, padx=10, pady=10,sticky=W)





app.mainloop()
