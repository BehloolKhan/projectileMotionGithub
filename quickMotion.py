import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation

def showAnimatedPoints(frame, object, displacement:list[float], times:list[float]) -> None:

    plt.cla()
    plt.xlabel("times, seconds")
    plt.ylabel("displacemet, metres")

    plt.plot(times, displacement)

    #now we need to update the values

    object["time"] += object["time_interval"] #update the time
    object["u"] += (object["a"]*0.05) #0.2 seconds is the time between frames
    object["y"] += (object["u"]*object["time_interval"]+ 0.5*object["a"]*(object["time_interval"]**2))#new y value

    displacement.append(object["y"])
    times.append(object["time"])

def drawMotion(intialVerticalVelocity):

    physicsObject = {"y":0.0, 
                    "time":0.0,
                    "time_interval":0.05,
                    "u":intialVerticalVelocity,
                    "a":-9.81} #intial velocity
    
    displacement = [physicsObject["y"]]
    times = [physicsObject["time"]]

    ani = FuncAnimation(plt.gcf(), showAnimatedPoints, frames=110, interval=50, fargs=(physicsObject, displacement, times), repeat=False)

    plt.show() #show the animations

if __name__ == "__main__":
     #if this is the entry point of the script, this will be set to __main__, id not, will be file name
     #sort of like a header guard
     drawMotion() 