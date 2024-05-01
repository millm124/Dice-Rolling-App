import sys


from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QLabel,
    QMainWindow,
    QPushButton,
    QSlider,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
)

from random import randint


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Dice Rolling App")


        layout = QVBoxLayout()


        # Slider
        dice_num = QLabel("Number of Dice Rolled")
       
        self.num_slider = QSlider(Qt.Orientation.Horizontal)
        self.num_slider.setRange(1, 100)
        self.num_slider.setSingleStep(1)
        self.num_slider.valueChanged.connect(self.value_changed)
        self.slider_output = QLabel("1")
        space = QLabel("")


        slider_layout = QHBoxLayout()
        slider_layout.addWidget(self.num_slider)
        slider_layout.addWidget(space)
        slider_layout.addWidget(self.slider_output)


        # Operation Combo Box
        operation = QLabel("Operation Used")


        self.operation_box = QComboBox()
        self.operation_box.addItems(["Addition", "Multiplication"])


        # Sides Combo Box
        sides = QLabel("Sides of Dice")


        self.side_box = QComboBox()
        self.side_box.addItems(["4", "6", "8", "10", "12", "20", "100"])


        # Roll Button
        roll_button = QPushButton(text = "Roll", parent=self)
        roll_button.setFixedSize(200, 60)
        roll_button.clicked.connect(self.roll)


        blank = QLabel("100, 100, 100, 100, 100, 100, 100, 100, 100, 100")


        total_value = self.side_box.currentText()
        self.display_label = QLabel("Total: " + str(total_value))
       
       
        layout.addWidget(dice_num)
        layout.addLayout(slider_layout)
        layout.addWidget(self.num_slider)
        layout.addWidget(self.slider_output)
        layout.addWidget(operation)
        layout.addWidget(self.operation_box)
        layout.addWidget(sides)
        layout.addWidget(self.side_box)
        layout.addWidget(roll_button, alignment = Qt.AlignmentFlag.AlignHCenter)
        layout.setContentsMargins(5, 10, 5, 10)
        layout.addWidget(blank)
        layout.addWidget(self.display_label)


        widget = QWidget()
        widget.setLayout(layout)


        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


    def roll(self):
       
        sides = self.side_box.currentText()
        sides = int(sides)

        output_slider = self.num_slider.value()
       


        for i in range(output_slider):
            dice_rolls = randint(1, sides)
            print(str(dice_rolls))



    def value_changed(self):
        slider_value = self.num_slider.value()
        self.slider_output.setText(str(slider_value))




app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()

