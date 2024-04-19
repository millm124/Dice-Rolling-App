import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSlider,
    QVBoxLayout,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dice Rolling App")

        layout = QVBoxLayout()

        dice_num = QLabel("Number of Dice Rolled")

        self.num_slider = QSlider(Qt.Orientation.Horizontal)
        self.num_slider.setRange(1, 100)
        self.num_slider.setSingleStep(1)

        number = self.num_slider

        operation = QLabel("Operation Used")

        self.operation_box = QComboBox()
        self.operation_box.addItems(["Addition", "Multiplication"])

        sides = QLabel("Sides of Dice")

        self.side_box = QComboBox()
        self.side_box.addItems(["4", "6", "8", "10", "12", "20", "100"])

        roll_button = QPushButton(text = "Roll", parent=self)
        roll_button.setFixedSize(200, 60)
        roll_button.clicked.connect(self.roll)

        self.display_label = QLineEdit("Total: ")

        layout.addWidget(dice_num)
        layout.addWidget(self.num_slider)
        layout.addWidget(number)
        layout.addWidget(operation)
        layout.addWidget(self.operation_box)
        layout.addWidget(sides)
        layout.addWidget(self.side_box)
        layout.addWidget(roll_button, alignment = Qt.AlignmentFlag.AlignHCenter)
        layout.setContentsMargins(5, 10, 5, 10)
        layout.addWidget(self.display_label)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def roll(self):
        
        
        # get info from inputs and do the operation to calculate a total

        # dice_num = self.num_slider
        # operation = self.operation_box.currentText()
        # dice_sides = self.side_box.currentText()
        
        # display total in a line edit

        self.display_label.setText()


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()