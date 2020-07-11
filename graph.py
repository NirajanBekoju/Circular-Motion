import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate(i):
    data = pd.read_csv('data.csv')
    x = data["time"]
    y = data["displacement"]
    
    plt.cla()
    plt.plot(x, y, label = "Function")
    
    # Set Basic info
    plt.title("Simple Harmonic Motion")
    plt.xlabel("Time(t) --------->")
    plt.ylabel("Displacement(y) in pixel --------->")
    plt.legend(loc = "upper left")
    plt.grid(True, axis='both')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval = 100)

plt.tight_layout()
plt.show()
