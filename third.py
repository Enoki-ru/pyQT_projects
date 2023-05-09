import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout,QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('3 программа')
        self.label=QLabel()

        self.input=QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout=QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input)

        container=QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

app=QApplication(sys.argv)
window=MainWindow()
window.show()

app.exec()