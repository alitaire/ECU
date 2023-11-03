import tkinter as tk
from math import cos, sin, radians

class MyCanvas(tk.Canvas):
    def __init__(self, parent, max_unit):
        super().__init__(parent, width=700, height=700)
        self.maxUnit = max_unit
        self.pack()
        self.draw()

    def draw(self):
        self.delete("all")

        radius = 0.95 * (min(self.winfo_width(), self.winfo_height()) / 2)
        centerX = self.winfo_width() / 2
        centerY = self.winfo_height() / 2

        # Draw the black background circle
        self.create_oval(centerX - radius, centerY - radius, centerX + radius, centerY + radius, outline="black", fill="black")

        # Draw the outer circle
        self.create_oval(centerX - radius, centerY - radius, centerX + radius, centerY + radius, outline="gray", width=8)

        # Draw graduations on the outer circle
        angle_start = -5 * 3.14159 / 4
        for speed in range(0, self.maxUnit + 1, 2):
            angle = angle_start + radians(speed / self.maxUnit * 240)
            x1 = centerX + cos(angle) * radius * 0.92
            y1 = centerY + sin(angle) * radius * 0.92
            x1bis = centerX + cos(angle) * radius * 0.80 # Used to display speed values
            y1bis = centerY + sin(angle) * radius * 0.80 # Used to display speed values
            x2 = centerX + cos(angle) * radius * 0.95
            y2 = centerY + sin(angle) * radius * 0.95

            if speed % 20 == 0:
                self.create_line(x1, y1, x2, y2, fill="white", width=3)
                delta = radius * 0.03
                self.create_text(x1bis, y1bis + delta, text=str(speed), fill="white", font=("Helvetica", 20))
            elif speed % 10 == 0:
                self.create_line(x1, y1, x2, y2, fill="white", width=2)
            else:
                self.create_line(x1, y1, x2, y2, fill="gray")

        # Draw the inner circle
        self.create_oval(centerX - radius * 0.6, centerY - radius * 0.6, centerX + radius * 0.6, centerY + radius * 0.6, outline="gray", width=8)

        # Draw graduations on the inner circle
        for speed in range(0, self.maxUnit + 1, 2):
            angle = angle_start + radians(speed / self.maxUnit * 240)
            x1 = centerX + cos(angle) * radius * 0.62
            y1 = centerY + sin(angle) * radius * 0.62
            x2 = centerX + cos(angle) * radius * 0.66
            y2 = centerY + sin(angle) * radius * 0.66

            if speed % 20 == 0:
                self.create_line(x1, y1, x2, y2, fill="white", width=3)
            elif speed % 10 == 0:
                self.create_line(x1, y1, x2, y2, fill="white", width=2)
            else:
                self.create_line(x1, y1, x2, y2, fill="gray")

        self.create_text(centerX - 20, self.winfo_height() * 0.65, text="Unit", fill="white", font=("Helvetica", 20))

        # Draw the needle
        speed = 120  # Change this value to set the speed
        angle = angle_start + radians(speed / self.maxUnit * 240)
        x1 = centerX + cos(angle) * radius * 0.93
        y1 = centerY + sin(angle) * radius * 0.93
        x2 = centerX + cos(angle - 0.4) * radius * 0.1
        y2 = centerY + sin(angle - 0.4) * radius * 0.1
        x3 = centerX + cos(angle + 0.4) * radius * 0.1
        y3 = centerY + sin(angle + 0.4) * radius * 0.1

        self.create_polygon(x1, y1, x2, y2, x3, y3, outline="red", fill="red")

        self.after(1000, self.draw)  # Update the display periodically

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tkinter Example")
    app = MyCanvas(root, max_unit=240)
    app.draw()
    root.mainloop()
