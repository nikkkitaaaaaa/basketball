import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
import subprocess





class LoadingPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game Loading Page")
        self.setGeometry(100, 100, 800, 600)  # Set the window size
        self.setWindowOpacity(0.9)  # Set the opacity (0.0 to 1.0)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Add label
        game_label = QLabel("Basketball Game")
        font = game_label.font()
        font.setBold(True)
        font.setPointSize(42)
        game_label.setFont(font)
        layout.addWidget(game_label, alignment=Qt.AlignTop | Qt.AlignHCenter)


        # Add background image
        pixmap = QPixmap("image1.png")
        background_label = QLabel(self)
        background_label.setPixmap(pixmap)
        background_label.setGeometry(0, 0, 1920, 1080)  # Set the size of the label to cover the window

        # Add buttons
        play_button = QPushButton("Play")
        play_button.setStyleSheet("font-size: 36px; font-weight: bold; background-color: rgba(255, 255, 255, 50);")
        play_button.setMaximumWidth(200)  # Set maximum width for the play button
        layout.addWidget(play_button, alignment=Qt.AlignTop | Qt.AlignCenter)

        # Add exit button
        exit_button = QPushButton("Exit")
        exit_button.setStyleSheet("font-size: 36px; font-weight: bold; background-color: rgba(255, 255, 255, 50);")
        exit_button.setMaximumWidth(200)  # Set maximum width for the exit button
        layout.addWidget(exit_button, alignment=Qt.AlignTop | Qt.AlignCenter)

        # Set layout
        self.setLayout(layout)

        # Connect button signals to slots
        play_button.clicked.connect(self.start_game)
        exit_button.clicked.connect(self.exit_game)

    def start_game(self):
        # Implement the functionality to start the game
        print("Starting the game...")
        # Close the current window
        
        

        
       
        

        

            


    def exit_game(self):
        # Implement the functionality to exit the application
        print("Exiting the application...")
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoadingPage()
    window.show()
    sys.exit(app.exec_())
