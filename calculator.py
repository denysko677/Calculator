import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt


class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Калькулятор")
        self.setGeometry(100, 100, 300, 400)

        self.layout = QVBoxLayout()
        self.setStyleSheet("background-color: #f0f0f0;")

        self.display = QLineEdit()
        self.display.setFixedHeight(50)
        self.display.setFont(QFont("Arial", 16))
        self.layout.addWidget(self.display)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for row in buttons:
            h_layout = QVBoxLayout()
            for button_text in row:
                button = QPushButton(button_text)
                button.clicked.connect(self.on_button_click)
                button.setFixedSize(60, 60)
                button.setFont(QFont("Arial", 12))
                button.setStyleSheet("background-color: #ffffff; color: #000000;")
                h_layout.addWidget(button)
            self.layout.addLayout(h_layout)

        self.setLayout(self.layout)

    def on_button_click(self):
        button = self.sender()
        text = button.text()
        if text == '=':
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec_())
