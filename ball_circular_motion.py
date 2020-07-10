from tkinter import Tk, Canvas
import math
import time


# mark an initial point
class CircularMotion():
    # Create a 300x300 canvas
    def __init__(self, window_title = "Tkinter", width = 300, height = 300):
        self.root = Tk()
        self.root.title(window_title)
        self.canvas = Canvas(self.root, width = width, height = height)
        self.canvas.pack()
    
    def mark_trajectory(self, center_x  = 150, center_y = 150, radius = 100):
        # Center Mark
        self.center_X = center_x
        self.center_Y = center_y
        self.Radius = radius
        radius_of_center_mark = 30
        self.radius_of_rotaing_ball = 10
        # Drawing the center mark
        self.create_circle(center_x, center_y, radius_of_center_mark, fill="orange")
        # Initialing Point of the rotaing ball
        self.ball_center_x = center_x + radius
        self.ball_center_y = center_y
        self.ball = self.create_circle(self.ball_center_x, self.ball_center_y, self.radius_of_rotaing_ball, fill="blue")
        

    def revolution_ball(self):
        current_x = self.ball_center_x
        current_y = self.ball_center_y
        old_point = [current_x, current_y]
        # Drawing the initial line
        initial_line = self.canvas.create_line(current_x, current_y, self.center_X, self.center_Y, fill="red")
        # Drawing the initial radius line
        radius_line = self.canvas.create_line(current_x, current_y, self.center_X, self.center_Y, fill="red")
        while True:
            # if the ball is in range
            if(self.ball_center_x >= self.center_X - self.Radius and self.ball_center_x <= self.center_X + self.Radius):
                # Defining the current position of the ball
                if current_y == self.center_Y:
                    # Upward Part
                    if current_x == self.center_X + self.Radius:
                        flag = -1
                    # Down Part    
                    elif current_x == self.center_X - self.Radius:
                        flag = 1
                
                # Determining the new postion of the ball in circular motion
                current_x = current_x + flag
                current_y = flag * math.sqrt(self.Radius ** 2 - (current_x - self.center_X)**2) + self.center_Y

                # Deleting the previous lines
                self.canvas.delete(self.my_ball)
                self.canvas.delete(radius_line)
                self.ball = self.create_circle(current_x, current_y, self.radius_of_rotaing_ball, fill="blue")

                # Drawing the trajectory
                self.canvas.create_line(old_point[0], old_point[1], current_x, current_y, fill="red")
                old_point[0] = current_x
                old_point[1] = current_y

                # Drawing the line between ball and the center
                radius_line = self.canvas.create_line(current_x, current_y, self.center_X, self.center_Y, fill="red")

                self.root.update()
                time.sleep(0.01)

            else:
                print("Error Ball out of Circle")
                break
            
    # Creating a Circle
    def create_circle(self, x, y, r, **kwargs):
        self.my_ball = self.canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)

ball = CircularMotion(window_title="Ball Circular Motion")
ball.mark_trajectory()
ball.revolution_ball()
ball.root.mainloop()