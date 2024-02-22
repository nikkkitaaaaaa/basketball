import sys
from PyQt5.QtWidgets import QApplication,QLabel,QMainWindow,QLineEdit,QPushButton
from PyQt5.QtGui import QPixmap, QPainter, QPen,QFont
from PyQt5.QtCore import Qt, QTimer
import random,math

class game(QMainWindow):
    def __init__(self, image_path):
        super().__init__()
        self.setWindowTitle("BasketBall Game")
        
        # Load the image
        self.image = QPixmap(image_path)
        self.b_image=QPixmap('ball.png')
        # Set window size to match image size
        self.setFixedSize(self.image.size())
        
        # Create QLabel to display the image
        self.image_label = QLabel(self)
        self.image_label.setPixmap(self.image)
        self.image_label.setGeometry(0, 0, self.image.width(), self.image.height())
        
        self.b_image_label = QLabel(self)
        self.b_image_label.setPixmap(self.b_image)
        self.b_image_label.setGeometry(270,940, self.b_image.width(), self.b_image.height())




        self.height_label=QLabel(self)
        self.height_label.setGeometry(1720,450,1800,450)
        self.height=random.randint(25,500)

        self.range_label=QLabel(self)
        self.range_label.setGeometry(777,660,1080,660)
        self.ranges=random.randint(0,200)

        font = self.height_label.font()
        font.setPointSize(18)  # Set the font size to 20
        self.height_label.setFont(font)
        self.height_label.setStyleSheet("color:black;")
        fontr = self.range_label.font()
        fontr.setPointSize(18)  # Set the font size to 20
        self.range_label.setFont(fontr)
        self.range_label.setStyleSheet("color:black;")
        
        #gravity=9.81m/s2
        self.g=9.81

        self.label_initial_velocity = QLabel("Initial Velocity (m/s):", self)
        self.label_initial_velocity.setGeometry(50, 50, 150, 30)
        self.input_initial_velocity = QLineEdit(self)
        self.input_initial_velocity.setGeometry(200, 50, 150, 30)
        self.label_initial_velocity.setStyleSheet("color:white;")
        
        self.label_initial_velocity.font().setPointSize(18)
        self.label_angle = QLabel("Launch Angle (degrees):", self)
        self.label_angle.setGeometry(50, 90, 150, 30)
        self.input_angle = QLineEdit(self)
        fonta=self.label_angle.font()
        self.input_angle.setGeometry(200, 90, 150, 30)
        self.label_angle.setStyleSheet("color:white;")
        fonta.setPointSize(18)
        self.button = QPushButton("Submit", self)
        self.button.setGeometry(200, 130, 100, 30)
        self.button.clicked.connect(self.submit_clicked)

        # Initialize line position
        self.line_x = 320
        self.line_y = 1020
        self.curve_x = 320
        self.curve_y = 1020

        
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
            ans_t=math.degrees(math.atan(2*self.height//self.ranges))
            ans_u=((self.height*2*self.g)//math.sin(ans_t)**2)**0.5
            if self.u==0 and self.thet==0:
                self.u=162
                self.u1=114
                self.u2=123
                self.u3=129
                self.curve_x=320
                self.curve_y=1020
                self.curve_x1=320
                self.curve_y1=1020
                
                self.timer1 = QTimer(self)
                self.timer1.timeout.connect(self.last_anim)
                self.timer1.start(1) 
            else:
                self.u=ans_u
                self.u1=math.cos(ans_t)
                self.u2=math.sin(ans_t)
                self.u3=self.u2+6
                self.curve_x=320
                self.curve_y=1020
                self.curve_x1=320
                self.curve_y1=1020
                self.timer1 = QTimer(self)
                self.timer1.timeout.connect(self.last_anim)
                self.timer1.start(1) 
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    def paintEvent(self, event):
        # Draw the line on the image
        painter = QPainter(self.image)
        painter.setPen(QPen(Qt.white, 4, Qt.DotLine))
        
        if self.line_x < 1710:
            painter.drawLine(self.line_x, self.line_y, self.line_x + 50, self.line_y)
        else:
            painter.drawLine(self.line_x, self.line_y, self.line_x , self.line_y-50)

        self.image_label.setPixmap(self.image)

    


    

    def last_anim(self):
        
        paintd = QPainter(self.image)
        paintd.setPen(QPen(Qt.white, 4, Qt.DotLine))
        
        k1=(self.curve_x1,self.curve_y1)
        k = [self.curve_x,self.curve_y]


        for t in range(0,23,1):
            # Calculate coordinates for the curve
            self.curve_x = 320+self.u1*t*0.5
            self.curve_y = 1020-(self.u2 * t*0.5 - 0.5 * self.g * (t*0.5) ** 2)
            self.curve_x1 = 320+self.u1*t*0.5
            self.curve_y1 = 1020-(self.u3 * t*0.5 - 0.5 * self.g * (t*0.5) ** 2)
            paintd.drawLine(int(k[0]), int(k[1]), int(self.curve_x), int(self.curve_y))
            self.b_image_label.setGeometry(int(k1[0]), int(k1[1]), int(self.curve_x1), int(self.curve_y1))
            k=(self.curve_x,self.curve_y)
            k1=(self.curve_x1,self.curve_y1)
            self.image_label.setPixmap(self.image)
            self.b_image_label.setPixmap(self.b_image)
            QApplication.processEvents() 
        paintd.drawLine(int(k[0]), int(k[1]),1574,1021)
        self.b_image_label.setGeometry(int(k1[0])-30,int(k1[1]),self.b_image.width(),self.b_image.height()+1475)
        self.b_image_label.setPixmap(self.b_image)
        self.timer1.stop()

     
       

        
        
        


       

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


def main():
    app = QApplication(sys.argv)
    window = game("image.png") 
    window.show()
    sys.exit(app.exec_())


main()
