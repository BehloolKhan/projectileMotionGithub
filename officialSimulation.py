#import required libraries needed for this simulation

import pygame #for rendering
import tkinter as tk#required for GUI for user to interact with
import math #for numerical calculations
import numpy

#libraries to plot projectory of ball graphically and for animations
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

#other dependencies required
import random

#functions and classes needed from files in the same directory
from projectileMotionFile import Ball, mainGameLoop
from quickMotion import drawGraphs


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

        self.geometry("800x400")
        self.title("control panel")

        self.K = 0 # defulat value for this project


        tk.Label(self, text="angle of projection").grid(row=0, column=0)
        self.angleOfProjectionScale = tk.Scale(self, from_=0, to=90, width=25, orient="horizontal")
        self.angleOfProjectionScale.grid(row=0, column=1)

        tk.Label(self, text="velocity").grid(row=1, column=0)
        self.velocityScale = tk.Scale(self, from_=0, to=100, orient="horizontal", width=25)
        self.velocityScale.grid(row=1, column=1)

        self.submitInfo = tk.Button(self, text="submit all information", command=self.getInfo, width=20)
        self.submitInfo.grid(row=2, column=0)

        self.launchButton = tk.Button(self, command=self.intialiseGameLoop, text="Launch")
        self.launchButton.grid(row=4, column=0)

        self.turnOn = tk.Button(self, text="turn on air resistance", command=self.simulateAirResistance)
        self.turnOn.grid(row=3, column=0)

        self.displayGraph = tk.Button(self, text="display graph of projectile motion", command=self.drawMotionBall)
        self.displayGraph.grid(row=5, column = 0)

        self.closeAll = tk.Button(self, command=self.destroyPanel, text="close control panel")
        self.closeAll.grid(row=6, column=0)


    #methods this object will have are the functions called by buttons

    def simulateAirResistance(self):
        #now we need to think about what need to be displayed
        
        self.airResistanceScale = tk.Scale(self, from_ = 0, to=10, width=25, orient="horizontal")
        self.airResistanceScale.grid(row=3, column=1)

        self.submitResistance = tk.Button(self, text="submit", command=self.setAirResistance)
        self.submitResistance.grid(row=3, column=2)

        self.turnOff = tk.Button(self, text="turn off air resistance", command=self.resetAirResistance)
        self.turnOff.grid(row=4, column=1)

    def setAirResistance(self):
        self.K = self.airResistanceScale.get()

    def resetAirResistance(self):
        self.airResistanceScale.set(0) # reset to 0
        self.setAirResistance()

    def drawMotionBall(self):

        #need to convert angle to radian
        angleRadians = self.angle/180*numpy.pi
        verticalVelocity = self.velocity*math.sin(angleRadians)
        
        drawGraphs(verticalVelocity, self.K)

    def intialiseGameLoop(self):

        mainGameLoop(self.velocity, self.angle, self.K) # main game loop with values it gets

    def getInfo(self):

        #need to get angle of projectiom and velocity, so we add 2 additonal attributes we can add
        self.angle = self.angleOfProjectionScale.get()
        self.velocity = self.velocityScale.get()

        tk.Label(self, text=f"  The angle of projection is {self.angle}").grid(row=0, column=2)
        tk.Label(self, text=f"  The velocity is {self.velocity}").grid(row=1, column=2)

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


root.mainloop()