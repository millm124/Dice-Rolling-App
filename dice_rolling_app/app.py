import sys
import controller

from PyQt6.QtGui import QFont, QFontDatabase
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




# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dice Rolling App")

        # Install fonts
        self.set_font("FiraSans-Bold.ttf")
        self.set_font("PTSerif-Regular.ttf")

        layout = QVBoxLayout()

        # Slider
        dice_num = QLabel("Number of Dice Rolled")
        dice_num.setFont(QFont("Fira Sans"))
       
        self.num_slider = QSlider(Qt.Orientation.Horizontal)
        self.num_slider.setRange(1, 100)
        self.num_slider.setSingleStep(1)
        self.num_slider.valueChanged.connect(self.value_changed)

        self.slider_output = QLabel("1")
        self.slider_output.setFont(QFont("PT Serif"))

        # Slider layout
        slider_layout = QHBoxLayout()
        slider_layout.addWidget(self.num_slider)
        slider_layout.addWidget(self.slider_output)

        # Operation Combo Box
        operation = QLabel("Operation Used")
        operation.setFont(QFont("Fira Sans"))

        self.operation_box = QComboBox()
        self.operation_box.addItems(["Addition", "Multiplication"])
        self.operation_box.setFont(QFont("PT Serif"))

        # Sides Combo Box
        sides = QLabel("Sides of Dice")
        sides.setFont(QFont("Fira Sans"))

        self.side_box = QComboBox()
        self.side_box.addItems(["4", "6", "8", "10", "12", "20", "100"])
        self.side_box.setFont(QFont("PT Serif"))

        # Roll Button
        roll_button = QPushButton(text = "Roll", parent=self)
        roll_button.setFixedSize(200, 60)
        roll_button.clicked.connect(self.roll)
        roll_button.setFont(QFont("Fira Sans"))
       
        # Rolls
        self.display_label = QLabel("Rolls: ")
        self.display_label.setWordWrap(True)
        self.display_label.setFont(QFont("Fira Sans"))

        # Total
        self.total_value = QLabel("Total: ")
        self.total_value.setFont(QFont("Fira Sans"))
       
        layout.addWidget(dice_num)
        layout.addLayout(slider_layout)
        layout.addWidget(self.num_slider)
        layout.addWidget(self.slider_output)
        layout.addWidget(operation)
        layout.addWidget(self.operation_box)
        layout.addWidget(sides)
        layout.addWidget(self.side_box)
        layout.addWidget(roll_button, alignment = Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.display_label)
        layout.addWidget(self.total_value)

        widget = QWidget()
        widget.setLayout(layout)
        
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)
        height = self.height()
        self.max_height = height - 100
        self.resize(100, self.max_height)

    def roll(self):


        total = 0
        dice_rolls = ""


        dice_rolled = self.num_slider.value()
        operation = self.operation_box.currentText()
        sides = self.side_box.currentText()
        sides = int(sides)


        dice_rolls, total = controller.calculate_total(dice_rolled, operation, sides)


        self.display_label.setText(dice_rolls)
        height = self.height()
        width = self.width()
        if dice_rolled >= 10:
            height += 25
            if height > self.max_height:
                height = self.max_height
            self.resize(width, height)

        self.total_value.setText("Total: " + str(total))

    def value_changed(self):
        slider_value = self.num_slider.value()
        self.slider_output.setText(str(slider_value))

    def set_font(self, font_name: str) -> None:
        font_dir = "FONTS/"
        font_path = font_dir + font_name
        success = QFontDatabase.addApplicationFont(font_path)

        # If it failed to add font
        if success == -1:
            print(f"{font_name} not loaded.")

app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()
