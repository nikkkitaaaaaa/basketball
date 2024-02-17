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

        self.time = 0
        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.update1_position)
        self.timer1.start(6) 

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
        
        # Initialize line position
        self.line_x = 320
        self.line_y = 1020
        
        # Timer for animation
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_line_position)
        self.timer.start(1)  # Update every 1 milliseconds
    
    def paintEvent(self, event):
        # Draw the line on the image
        painter = QPainter(self.image)
        painter.setPen(QPen(Qt.black, 6, Qt.SolidLine))
        
        if self.line_x < 1710:
            painter.drawLine(self.line_x, self.line_y, self.line_x + 50, self.line_y)
        else:
            painter.drawLine(self.line_x, self.line_y, self.line_x , self.line_y-50)

        # Draw the projectile
        painter.drawEllipse(315, self.height() - self.line_y, 10, 10)

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
            self.range_label.setText(f"Range = {self.ranges} m")
            self.timer.stop()
             
        self.update()

    def update1_position(self):
        self.time += 0.1  # Increment time
        self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageWithLine("image.png") 
    window.show()
    sys.exit(app.exec_())

