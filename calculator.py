import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit


class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Калькулятор")
        self.setGeometry(100, 100, 300, 400)

        self.layout = QVBoxLayout()

        self.display = QLineEdit()
        self.display.setFixedHeight(50)
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
                h_layout.addWidget(button)
            self.layout.addLayout(h_layout)

        self.setLayout(self.layout)

    def on_button_click(self):
        button = self.sender()
        text = button.text()
        if text == '=':
            self.calculate_result()
        else:
            self.display.setText(self.display.text() + text)

    def calculate_result(self):
        expression = self.display.text()
        try:
            result = eval(expression)
            self.display.setText(str(result))
        except Exception as e:
            self.display.setText("Error: " + str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec_())
