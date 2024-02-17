import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit

class CalculatorModel:
    def evaluate_expression(self, expression):
        try:
            result = eval(expression)
            return str(result)
        except Exception as e:
            return "Error"

class CalculatorView(QWidget):
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
                h_layout.addWidget(button)
            self.layout.addLayout(h_layout)
        self.setLayout(self.layout)

class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.display.textChanged.connect(self.evaluate_expression)
        for button in self.view.findChildren(QPushButton):
            if button.text() != '=':
                button.clicked.connect(self.on_button_click)
        self.view.show()

    def on_button_click(self):
        button = self.sender()
        text = button.text()
        self.view.display.setText(self.view.display.text() + text)

    def evaluate_expression(self):
        expression = self.view.display.text()
        result = self.model.evaluate_expression(expression)
        self.view.display.setText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = CalculatorModel()
    view = CalculatorView()
    controller = CalculatorController(model, view)
    sys.exit(app.exec_())
