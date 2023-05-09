import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QComboBox, QPushButton, QLabel

class Example1(QWidget):
    def __init__(self):
        super().__init__()
        # Добавьте сюда код для первого примера
        label = QLabel("<font color=red size=40>Hello World!</font>")
        label.show()
        window = QPushButton('Hello')
        window.show()  # Важно: окно по умолчанию скрыто.

class Example2(QWidget):
    def __init__(self):
        super().__init__()
        # Добавьте сюда код для второго примера

class Example3(QWidget):
    def __init__(self):
        super().__init__()
        # Добавьте сюда код для третьего примера

class Example4(QWidget):
    def __init__(self):
        super().__init__()
        # Добавьте сюда код для четвертого примера

class Example5(QWidget):
    def __init__(self):
        super().__init__()
        # Добавьте сюда код для пятого примера

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.examples = [Example1(), Example2(), Example3(), Example4(), Example5()]
        self.current_example = None
        self.init_ui()

    def init_ui(self):
        self.combo_box = QComboBox()
        for i in range(1, 6):
            self.combo_box.addItem(str(i))

        self.btn_run = QPushButton("Run")
        self.btn_run.clicked.connect(self.run_example)

        main_widget = QWidget(self)
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.combo_box)
        main_layout.addWidget(self.btn_run)
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)

    def run_example(self):
        example_num = int(self.combo_box.currentText())

        if self.current_example == self.examples[example_num - 1]:
            return

        if self.current_example is not None:
            self.current_example.hide()
        self.current_example = self.examples[example_num - 1]
        self.setCentralWidget(self.current_example)
        self.current_example.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
