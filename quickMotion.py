import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation
import threading #for concurrency

def showDisplacementTimeGraph(frame, object, displacement:list[float], times:list[float]) -> None:

    plt.cla()
    plt.xlabel("times, seconds")
    plt.ylabel("vertical displacemet, metres")

    plt.plot(times, displacement)

    #now we need to update the values

    object["time"] += object["time_interval"] #update the time
    #update the acceleration
    object["a"] = ((-object["k"]*object["u"] + -9.81*10) / 10)
    object["u"] += (object["a"]*object["time_interval"]) #0.2 seconds is the time between frames
    object["y"] += (object["u"]*object["time_interval"]+ 0.5*object["a"]*(object["time_interval"]**2))#new y value

    displacement.append(object["y"])
    times.append(object["time"])

#now we need to think about vertical

def showVelocityTimeGraph(frame, physicsObject, velocity, times):

    plt.cla()

    plt.xlabel("time, seconds")
    plt.ylabel("vertical velocity, m/s")

    plt.plot(times, velocity)

    physicsObject["a"] = ((-physicsObject["k"]*physicsObject["u"] + -9.81*10) / 10)
    physicsObject["u"] += (physicsObject["a"]*physicsObject["time_interval"]) #0.2 seconds is the time between frames
    physicsObject["u"] += (physicsObject["a"]*physicsObject["time_interval"])
    physicsObject["time"] += physicsObject["time_interval"]

    velocity.append(physicsObject["u"])
    times.append(physicsObject["time"])


def drawGraphs(intialVerticalVelocity, K:int):

    physicsObject = {"y":0.0, 
                    "time":0.0,
                    "time_interval":0.05,
                    "u":intialVerticalVelocity,
                    "a":-9.81,
                    "k":K} #intial velocity
    
    displacement = [physicsObject["y"]]
    times = [physicsObject["time"]]

    ani = FuncAnimation(plt.figure(), showDisplacementTimeGraph, frames=110, interval=50, fargs=(physicsObject, displacement, times), repeat=False)

    plt.show()

    physicsObject["time"] = 0 #reset
    physicsObject["y"] = 0.0
    physicsObject["u"] = intialVerticalVelocity
    physicsObject["a"] = -9.81

    velocity = [physicsObject["u"]]
    times = [physicsObject["time"]]

    ani2 = FuncAnimation(plt.figure(), showVelocityTimeGraph, frames=100, interval=50, fargs=(physicsObject, velocity, times), repeat=False)

    plt.show()

if __name__ == "__main__":
     #if this is the entry point of the script, this will be set to __main__, id not, will be file name
     #sort of like a header guard
     drawGraphs(30, 3)