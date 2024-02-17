import sys
import math
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtCore import Qt, QTimer

class ImageWithLine(QMainWindow):
    def __init__(self, image_path):
        super().__init__()
        self.setWindowTitle("BasketBall Game")
        
        # Load the image
        self.image = QPixmap(image_path)
        
        # Set window size to match image size
        self.setFixedSize(self.image.size())
        
        # Create QLabel to display the image
        self.image_label = QLabel(self)
        self.image_label.setPixmap(self.image)
        self.image_label.setGeometry(0, 0, self.image.width(), self.image.height())
        
        self.height_label=QLabel(self)
        self.height_label.setGeometry(1720,450,1800,450)
        self.height=random.randint(25,500)

        self.range_label=QLabel(self)
        self.range_label.setGeometry(777,660,1080,660)
        self.ranges=random.randint(0,200)

        font = self.height_label.font()
        font.setPointSize(18)  # Set the font size to 20
        self.height_label.setFont(font)

        fontr = self.range_label.font()
        fontr.setPointSize(18)  # Set the font size to 20
        self.range_label.setFont(fontr)
        
        #gravity=9.81m/s2
        self.g=9.81

        self.label_initial_velocity = QLabel("Initial Velocity (m/s):", self)
        self.label_initial_velocity.setGeometry(50, 50, 150, 30)
        self.input_initial_velocity = QLineEdit(self)
        self.input_initial_velocity.setGeometry(200, 50, 150, 30)

        self.label_angle = QLabel("Launch Angle (degrees):", self)
        self.label_angle.setGeometry(50, 90, 150, 30)
        self.input_angle = QLineEdit(self)
        self.input_angle.setGeometry(200, 90, 150, 30)

        self.button = QPushButton("Submit", self)
        self.button.setGeometry(200, 130, 100, 30)
        self.button.clicked.connect(self.submit_clicked)

        # Initialize line position
        self.line_x = 320
        self.line_y = 1020
        
        # Timer for animation
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_line_position)
        self.timer.start(1)  # Update every 1 milliseconds

    def submit_clicked(self):
        try:
            self.u = float(self.input_initial_velocity.text())
            self.thet=float(self.input_angle.text())

            print("initial velocity entered:", self.u)
            print("angle with horizontal ",self.thet)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    def paintEvent(self, event):
        # Draw the line on the image
        painter = QPainter(self.image)
        painter.setPen(QPen(Qt.black, 6, Qt.SolidLine))
        
        if self.line_x < 1710:
            painter.drawLine(self.line_x, self.line_y, self.line_x + 50, self.line_y)
        else:
            painter.drawLine(self.line_x, self.line_y, self.line_x , self.line_y-50)

        self.image_label.setPixmap(self.image)


    previous_point=(320,1020)
    def paint_curve(self):
        paintc=QPainter(self.image)
        paintc.setPen(QPen(Qt.white, 6, Qt.SolidLine))
        #self.curve_y=1080-((320-self.curve_x)*(math.tan(math.radians(self.thet)))-((self.g*((320-self.curve_x)**2))/(2*((self.u)**2)*((math.cos(math.radians(self.thet))**2)))))
        self.curve_x=320+(self.u)*(self.t)
        self.curve_y=1080-(self.u)*(self.t)+(0.5*(self.g)*((self.t)**2))

        previous_point = None
        for value in range(100):
            # Evaluate the equations for x and y coordinates
            x = self.curve_x
            y = self.curve_y

            # Map coordinates to the window size (adjust scale and origin as needed)
            mapped_x = x 
            mapped_y = y

            # Draw the point if it's not the first point
            if previous_point is not None:
                paintc.drawLine(previous_point, (mapped_x, mapped_y))

            # Update the previous point
            previous_point = (mapped_x, mapped_y)


        self.image_label.setPixmap(self.image)
    
    def update_line_position(self):
        # Update line position for animation
        
        if self.line_x >=1660:
            self.line_y-=5
            self.line_x=1710
        else:
            self.line_x+=5
            
        if self.line_y <=330:
            self.height_label.setText(f"Height = {self.height} m")
            self.range_label.setText(f"Range/2 = {self.ranges} m")
            self.timer.stop()
             
        self.update()
    def update_curve(self):
        if (self.curve_x>=1920 or self.curve<=0) or (self.curve_y>=1080 or self.curve_y<=0):
            self.timer.stop()
        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageWithLine("image.png") 
    window.show()
    sys.exit(app.exec_())


