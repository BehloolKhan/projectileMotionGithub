#import required libraries needed for this simulation

import pygame #for rendering
import tkinter as tk#required for GUI for user to interact with

#libraries to plot projectory of ball graphically and for animations
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

#other dependencies required
import random

#functions and classes needed from files in the same directory
from projectileMotionFile import Ball, mainGameLoop
from quickMotion import drawMotion, showAnimatedPoints

#setting up the main control panel


root = tk.Tk()
root.title("projectile motion simulation")

#setting dimensions of control panel
root.geometry("450x200")

#we r going to use grid method to make everything proportinal
#buttons we will have

#code for setting up the control panel

class controlPanel(tk.Toplevel):
    def __init__(self):

        super().__init__() # call the parent constructor method, doesnt take in any arguments

        #setting up the window

        self.geometry("400x400")
        self.title("control panel")


        tk.Label(self, text="angle of projection").grid(row=0, column=0)
        self.angleOfProjection = tk.Scale(self, from_=0, to=90, width=25, orient="horizontal")
        self.angleOfProjection.grid(row=0, column=1)

        tk.Label(self, text="velocity").grid(row=1, column=0)
        self.velocity = tk.Scale(self, from_=0, to=100, orient="horizontal", width=25)
        self.velocity.grid(row=1, column=1)

        self.submitInfo = tk.Button(self, text="submit all information", command=self.getInfo, width=20)
        self.submitInfo.grid(row=2, column=0)

        self.launchButton = tk.Button(self, command=mainGameLoop, width=25, text="Launch")
        self.launchButton.grid(row=3, column=0)

        self.closeAll = tk.Button(self, command=self.destroyPanel, width=25, text="close control panel")
        self.closeAll.grid(row=4, column=0)


    #method on this object will be the button functions
    def getInfo(self):

        tk.Label(self, text=f"  The angle of projection is {self.angleOfProjection.get()}").grid(row=0, column=2)
        tk.Label(self, text=f"  The velocity is {self.velocity.get()}").grid(row=1, column=2)

        return None
    
    def destroyPanel(self):
        self.destroy() 
        del self #free up some space



#function to call control panel and open it
def openControl():
    #create an instance of a control panel but i do now want the memory location returned
    controlPanel()
    return None


#button to open this control panel
openControlPanel = tk.Button(root, text="open control panel", command=openControl)
openControlPanel.pack()


#now we are going to make code for the animations

displayGraph = tk.Button(root, text="display graph of projectile motion", command=drawMotion)
displayGraph.pack()


root.mainloop()