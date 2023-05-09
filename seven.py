from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.nrows = 9
        self.ncols = 9
        self.click_count = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Button Grid")

        # Создаем матрицу кнопок
        self.buttons = [[QPushButton(self) for j in range(self.ncols)] for i in range(self.nrows)]
        for i in range(self.nrows):
            for j in range(self.ncols):
                button = self.buttons[i][j]
                button.setGeometry(j*50, i*50, 50, 50)
                button.clicked.connect(self.on_button_clicked)

        self.setGeometry(100, 100, self.ncols*50, self.nrows*50)
        self.show()

    def on_button_clicked(self):
        sender = self.sender()
        if sender.text() == "":
            sender.setStyleSheet("background-color: red")
            sender.setText("X")
        else:
            sender.setStyleSheet("")
            sender.setText("")
        self.click_count += 1
        print("Количество нажатий:", self.click_count)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
