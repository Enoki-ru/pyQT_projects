import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon, QAction
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Приложение')
        self.setWindowIcon(QIcon('./img/icon1.png'))
        self.setGeometry(100,100,500,300)
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        menu_bar=self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        edit_menu = menu_bar.addMenu('&Edit')
        help_menu = menu_bar.addMenu('&Help')

        file_menu.addAction('New', lambda: self.text_edit.clear())
        file_menu.addAction('Open', lambda: print('Open'))
        file_menu.addAction('Exit', self.destroy)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage('v1.0')

        self.show()

app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()