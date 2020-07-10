from tkinter import Tk, Canvas, Frame
import math
import time
from datetime import datetime

COLOR = "brown"
PROJECTION_COLOR = "#666666"
SHOW_PROJECTION_LINE = True
# mark an initial point
class CircularMotion():
    # Create a 300x300 canvas
    def __init__(self, window_title = "Tkinter", window_width = 450, window_height = 400, canvas_width = 300, canvas_height = 300):
        self.root = Tk()
        self.root.title(window_title)
        self.root.geometry(f"{window_width}x{window_height}")
        self.canvas = Canvas(self.root, width = canvas_width, height = canvas_height)
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
  
        # Drawing the shadow line and the projected ball
        self.shadow_line_x = self.center_X + self.Radius + 25
        shadow_line = self.canvas.create_line(self.shadow_line_x, self.center_Y - self.Radius - 10,self.shadow_line_x, self.center_Y + self.Radius + 10)
        ball_shadow = self.create_projection_circle(self.shadow_line_x, self.center_Y, self.radius_of_rotaing_ball, fill=PROJECTION_COLOR)

    def revolution_ball(self, projection = False):
        current_x = self.ball_center_x
        current_y = self.ball_center_y
        old_point = [current_x, current_y]
        # Drawing the initial line
        initial_line = self.canvas.create_line(current_x, current_y, self.center_X, self.center_Y, fill=COLOR)
        # Drawing the initial radius line
        radius_line = self.canvas.create_line(current_x, current_y, self.center_X, self.center_Y, fill=COLOR)
        if(projection):
            # Drawing the Projection Line
            projection_line = self.canvas.create_line(current_x, current_y, self.shadow_line_x, current_y)
        while True:
            # if the ball is in range
            if(self.ball_center_x >= self.center_X - self.Radius and self.ball_center_x <= self.center_X + self.Radius):
                # Defining the current position of the ball
                if current_y == self.center_Y:
                    # Upward Part
                    if current_x == self.center_X + self.Radius:
                        flag = -1
                        now = datetime.now()

                    # Down Part    
                    elif current_x == self.center_X - self.Radius:
                        flag = 1
                        then = datetime.now()
                        seconds_elapsed = str(then - now)
                        print(float(seconds_elapsed[5::]))
                # Determining the new postion of the ball in circular motion
                current_x = current_x + flag
                current_y = flag * math.sqrt(self.Radius ** 2 - (current_x - self.center_X)**2) + self.center_Y

                # Deleting the previous lines
                self.canvas.delete(self.my_ball)
                self.canvas.delete(self.projected_ball)
                self.canvas.delete(radius_line)
                if(projection):
                    self.canvas.delete(projection_line)

                # Creating a new ball
                self.ball = self.create_circle(current_x, current_y, self.radius_of_rotaing_ball, fill="blue")
            
                # Drawing the projection of the ball
                ball_shadow = self.create_projection_circle(self.shadow_line_x, current_y, self.radius_of_rotaing_ball, fill=PROJECTION_COLOR)

                # Drawing the trajectory
                self.canvas.create_line(old_point[0], old_point[1], current_x, current_y, fill=COLOR)
                old_point[0] = current_x
                old_point[1] = current_y

                # Drawing the line between ball and the center
                radius_line = self.canvas.create_line(current_x, current_y, self.center_X, self.center_Y, fill=COLOR)

                if(projection):
                    # Drawing the projection line
                    projection_line = self.canvas.create_line(current_x, current_y, self.shadow_line_x, current_y)

                self.root.update()
                time.sleep(0.01)

            else:
                print("Error Ball out of Circle")
                break


    # Creating a Circle
    def create_circle(self, x, y, r, **kwargs):
        self.my_ball = self.canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)
    
    def create_projection_circle(self, x, y, r, **kwargs):
        self.projected_ball = self.canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)        

    
ball = CircularMotion(window_title="Ball Circular Motion")
ball.mark_trajectory()
ball.revolution_ball(projection=SHOW_PROJECTION_LINE)
ball.root.mainloop()