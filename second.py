import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
app_names=[
    'Lundy',
    'Mardi',
    'Mercredy',
    'Jeugdi',
    'Samedi',
    'Dimanche',
]
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_clicked=0
        self.setWindowTitle('Приложение')
        self.button= QPushButton('Щелк!')
        self.button.clicked.connect(self.button_clicked)
        self.setCentralWidget(self.button)


    def button_clicked(self):
        print('Clicked')
        self.qname=app_names[self.n_clicked]
        print(self.qname)
        self.n_clicked+=1
        if self.n_clicked == len(app_names):
            self.n_clicked=0
        self.setWindowTitle(self.qname)

app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()