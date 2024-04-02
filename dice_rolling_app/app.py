import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
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

        num_slider = QSlider(Qt.Orientation.Horizontal)
        num_slider.setRange(1, 100)
        num_slider.setSingleStep(1)

        operation = QLabel("Operation Used")

        operation_box = QComboBox()
        operation_box.addItems(["Addition", "Multiplication", "Subtraction (L -> R)", "Subtraction (R -> L)", "Division (L -> R)", "Division (R -> L)"])

        sides = QLabel("Sides of Dice")

        side_box = QComboBox()
        side_box.addItems(["4", "6", "8", "10", "12", "20", "100"])

        roll_button = QPushButton(text = "Roll", parent=self)
        roll_button.setFixedSize(200, 60)

        layout.addWidget(dice_num)
        layout.addWidget(num_slider)
        layout.addWidget(operation)
        layout.addWidget(operation_box)
        layout.addWidget(sides)
        layout.addWidget(side_box)
        layout.addWidget(roll_button, alignment = Qt.AlignmentFlag.AlignHCenter)
        #layout.setContentsMargins(5, 10, 5, 10)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()