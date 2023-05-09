import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtGui import QColor

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        self.nrows = 8
        self.ncols = 8
        self.buttons = [[QPushButton(self) for j in range(self.ncols)] for i in range(self.nrows)]
        self.color = [[0 for j in range(self.ncols)] for i in range(self.nrows)]

        for i in range(self.nrows):
            for j in range(self.ncols):
                self.buttons[i][j].setStyleSheet("background-color: red")
                self.buttons[i][j].clicked.connect(self.changeColor(i, j))
                grid.addWidget(self.buttons[i][j], i, j)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Матрица кнопок')
        self.show()

    def changeColor(self, row, col):
        def inner():
            self.color[row][col] += 1
            self.color[row][col] %= 2
            self.buttons[row][col].setStyleSheet(self.colorToStyle(self.color[row][col]))

            if row > 0:
                self.color[row-1][col] += 1
                self.color[row-1][col] %= 2
                self.buttons[row-1][col].setStyleSheet(self.colorToStyle(self.color[row-1][col]))
            if row < self.nrows-1:
                self.color[row+1][col] += 1
                self.color[row+1][col] %= 2
                self.buttons[row+1][col].setStyleSheet(self.colorToStyle(self.color[row+1][col]))
            if col > 0:
                self.color[row][col-1] += 1
                self.color[row][col-1] %= 2
                self.buttons[row][col-1].setStyleSheet(self.colorToStyle(self.color[row][col-1]))
            if col < self.ncols-1:
                self.color[row][col+1] += 1
                self.color[row][col+1] %= 2
                self.buttons[row][col+1].setStyleSheet(self.colorToStyle(self.color[row][col+1]))

        return inner

    def colorToStyle(self, color):
        if color == 0:
            return "background-color: red"
        elif color == 1:
            return "background-color: green"
        elif color == 2:
            return "background-color: blue"

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
