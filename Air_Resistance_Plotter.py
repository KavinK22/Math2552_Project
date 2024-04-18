import numpy as np
import matplotlib.pyplot as plt
#class modelling Projectiles for projectile motion
class Projectile:
    def __init__(self, k, g = 10, v0 = 0, y0 = 0):
        self.k = k #coefficient of air resistance
        self.g = g #gravity
        self.v0 = v0 #initial velocity
        self.y0 = y0 #initial position
    def euler_approximation(self, end, start = 0, h = 0.1): # uses euler's method to approximate velocity and position
        #initializing velocity, position, and time arrays
        v = np.zeros(int((end - start) / h))
        y = np.zeros(int((end - start) / h))
        t = np.zeros(int((end - start) / h))
        v[0] = self.v0
        y[0] = self.y0
        t[0] = start
        #approximation
        for i in range(1, int((end - start) / h)):
            if (v[i - 1] > 0):
                a = -self.g - self.k * v[i - 1]**2
            else: 
                a = -self.g + self.k * v[i - 1]**2
            print(a)
            v[i] = v[i - 1] + h * a
            y[i] = y[i - 1] + h * (v[i] + v[i - 1]) / 2
            t[i] = t[i - 1] + h
        return v, y, t #returns array of velocity, position, and time values
def plot_vyt(v, y, t, plt_type): #plots vt, yt, or vy graphs
    if (plt_type == "vt"):
        #Time v Velocity Graph
        plt.plot(t, v)
        plt.xlabel('Time')
        plt.ylabel('Velocity')
        plt.title("Velocity vs Time (Euler's Method)")
        plt.grid(True)
        plt.show()
    elif (plt_type == "yt"):
        #Time v Position Graph
        plt.plot(t, y)
        plt.xlabel('Time')
        plt.ylabel('Position')
        plt.title("Position vs Time (Euler's Method)")
        plt.grid(True)
        plt.show()
    elif (plt_type == "vy"):  
        #Position v Velocity Graph
        plt.plot(y, v)
        plt.xlabel('Position')
        plt.ylabel('Velocity')
        plt.title("Velocity vs Position (Euler's Method)")
        plt.grid(True)
        plt.show()

    
p1 = Projectile(0.1)
v, y, t = p1.euler_approximation(10)
print(v)
print(t)
plot_vyt(v, y, t, "vt")
