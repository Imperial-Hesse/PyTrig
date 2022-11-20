from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from matplotlib.pyplot import *
from tkinter import *
from tkinter import ttk
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
import math
###constant core variables###
main_window=tk.Tk()#main window
main_window.geometry("750x250")#resolution
main_window.configure(bg="black")#background color
main_window.attributes('-alpha',0.8)#transparency
###matplotlib parameters###
plt.rcParams['grid.color']="green"
plt.rcParams['axes.facecolor']="black"
plt.rcParams['figure.facecolor']="black"
plt.rcParams['text.color']="green"
plt.rcParams['axes.labelcolor']="green"
plt.rcParams['xtick.color']="green"
plt.rcParams['ytick.color']="green"
fig, ax = plt.subplots()#plot
π=math.pi
a=np.linspace( 0 , 2 * np.pi , 150 )
###conversion functions###
RTD = lambda R : float((180/π)*R) #radian to degree
#functions are interchangeable I;E RTD can take the output from DTR as input and vice versa
DTR = lambda D : float((π/180)*D) #degree to radian
def drawcircle(properties,propertybox):
    ###Clear text box and subplot for new informaon and plot###
    propertybox.delete(1.0,END)
    ax.clear()
    ###math###
    θ = int(round(float(properties[2].split("=")[1])))
    rad=DTR(θ)
    R = float(properties[0].split("=")[1])
    ax.set_ylim([-abs(R*2),R*2])
    ax.set_xlim([-abs(R*2),R*2])
    COS,SIN=R*math.cos(rad),R*math.sin(rad)
    VERSIN=1-COS
    try:
        EXSEC=(1/COS)-1
    except ZeroDivisionError:
        EXSEC=0
    SEC=1/COS
    CVS=1-SIN
    try:
        CSC=1/SIN
    except ZeroDivisionError:
        CSC=0
    EXCSC=(1/SIN)-1
    PTI=round(math.sin(rad)**2+math.cos(rad)**2)
    ###Draw the circle and plot trigonometric functions###
    #ax.plot(x,y,color=properties[1].split("=")[1])
    ax.plot(R*np.cos(a),R*np.sin(a),color=properties[1].split("=")[1])
    ax.scatter(0,0,color="white")
    ###Right triangle###
    ax.plot((0,COS),(0,SIN),color="white")#Starting point on degree
    ax.plot((0,COS),(0,0),color="blue")#Cosine
    ax.plot((0,COS),(SIN,SIN),color="blue")#2nd Cosine line
    ax.plot((COS,COS),(0,SIN),color="red")#Sine
    ax.plot((0,0),(0,SIN),color="red")#2nd Sine line
    if θ<90:#Q1
        tempR=R
        RTAN=math.tan(rad)#real tangent
        TAN=R+math.tan(rad)#tangent for graphing
    elif θ==90:
        tempR=R
        RTAN,TAN=0,0
    elif θ>90 and θ<180:#Q2
        tempR=-R
        RTAN=abs(math.tan(rad))
        TAN=-R+-abs(+math.tan(rad))
    elif θ>180 and θ<270:#Q3
        tempR=-R
        RTAN=-abs(math.tan(rad))
        TAN=-R+-abs(math.tan(rad))
    elif θ==270:
        tempR=-R
        TAN,RTAN=0,0
    elif θ>270:#Q4
        tempR=R
        RTAN=-abs(math.tan(rad))
        TAN=R+abs(math.tan(rad))
    else:
        tempR=R
        TAN,RTAN=0,0
    ax.plot((COS,TAN),(SIN,0),color="brown")#tangent line
    ax.plot((COS,tempR),(0,0),color="green")#versed sine
    ax.plot((tempR,TAN),(0,0),color="pink")#exsecant
    ax.plot((0,TAN),((R/2 if θ>180 else -R/2),(R/2 if θ>180 else -R/2)),color="cyan")#secant
    ax.plot((0,0),(0,(R/2 if θ>180 else -R/2)),color="cyan",linestyle="dashed")#secant dot left
    ax.plot((TAN,TAN),(0,(R/2 if θ>180 else -R/2)),color="cyan",linestyle="dashed")#secant dot right
    ax.plot((0,0),(SIN,R if θ<180 else -R),color="cyan")#co-versed sine
    ax.plot((0,0),(SIN+EXCSC if θ<180 else -R+EXCSC,R if θ<180 else -R),color="green")#ex co-secant
    ax.plot((0,COS),(SIN+EXCSC if θ<180 else -R+EXCSC,SIN),color="brown")#cotangent
    ax.plot((COS,tempR),(SIN,0),color="white")#chord
    if θ<90 or θ<360 and θ>270:
        ax.plot((-R/2,-R/2),(0,SIN+EXCSC if θ<180 else -R+EXCSC),color="pink")
        ax.plot((0,-R/2),(0,0),color="pink",linestyle="dashed")
        ax.plot((0,-R/2),(SIN+EXCSC if θ<180 else -R+EXCSC,SIN+EXCSC if θ<180 else -R+EXCSC),color="pink",linestyle="dashed")
    else:
        ax.plot((R/2,R/2),(0,SIN+EXCSC if θ<180 else -R+EXCSC),color="pink")
        ax.plot((0,R/2),(0,0),color="pink",linestyle="dashed")
        ax.plot((0,R/2),(SIN+EXCSC if θ<180 else -R+EXCSC,SIN+EXCSC if θ<180 else -R+EXCSC),color="pink",linestyle="dashed")
    try:
        COT=1/TAN
    except ZeroDivisionError:
        COT=0
    ax.set_aspect(1)
    canvas.draw()
    ###Update the plot and txt box###
    canvas.get_tk_widget().pack()
    toolbar.update()
    propertybox.insert(INSERT,f"Properties:\nRAD:{DTR(θ)}\nCos:{COS}\nSin:{SIN}\nTan:{RTAN}\nPythagorean Trigonometric Identity Constant: {PTI}\nVersed Sine:{VERSIN}\nExsecant:{EXSEC}\nSecant:{SEC}\nCo-Versed Sine:{CVS}\nExcosecant:{EXCSC}\nCotangent:{COT}")
def R_change(properties,TH):
    p=properties.get(1.0,END).split("\n")
    p=p[2].split("=")[1]
    #grabs the current value of the radius, re-writes the property box with a replaced value from the slider bar
    p=f"{properties.get(1.0,END).replace(p,str(TH))}"
    properties.delete(1.0,END)
    properties.insert(INSERT,p)
    drawcircle(properties.get(1.0,END).split("\n"),propertybox)
###Internal Widgets###
left_frame=Canvas(main_window)#plot container
canvas = FigureCanvasTkAgg(fig,master=left_frame)
center_frame=Frame(main_window)#center code container
TH=tk.DoubleVar()
R_label=tk.Label(center_frame,text="Theta",fg="green",bg="black")
circlegen = tk.Button(center_frame,bg="black",fg="green",text="generate circle",command=lambda: drawcircle(properties.get(1.0,END).split("\n"),propertybox))#run def to insert code
properties = tk.Text(center_frame,width=50,height=10,fg="green",bg="black")
properties.insert(INSERT,"Radius=1\nColor=blue\nθ=90")
def call_change(TH):
    R_change(properties,TH)
R_slider=Scale(center_frame,from_=0,to=360,bg="black",fg="green",orient='vertical',variable=TH,command=lambda R: call_change(R))
propertybox=tk.Text(center_frame,width=100,fg="green",bg="black",)
toolbar = NavigationToolbar2Tk(canvas,left_frame)
center_frame.configure(bg="black")
left_frame.configure(bg="black")
###Widget Packing###
circlegen.pack(side=TOP)
properties.pack(side=TOP)
R_label.pack(side=LEFT)
R_slider.pack(side=LEFT)
propertybox.pack(side=TOP)
left_frame.pack(side=LEFT)
center_frame.pack(side=TOP)
###Mainloop###
main_window.mainloop()
