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

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()
        widgets = [
            QSlider,
            QComboBox,
            QComboBox,
            QPushButton,

        ]

        num_slider = QSlider
        num_slider.setRange(1, 100)

        operation_box = QComboBox
        operation_box.addItems(["Addition", "Multiplication", "Subtraction (L-R)", "ubtraction (R-L)", "division (L-R)", "division (R-L)"])

        side_box = QComboBox
        side_box.addItems(["4", "6", "8", "10", "12", "20", "100"])

        roll_button = QPushButton(text = "Roll")


        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()