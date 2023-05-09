import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My 1st app")
        button= QPushButton('Нажми на меня если можешь')
        button.setCheckable(True)
        button.clicked.connect(self.clicked_button)
        button.clicked.connect(self.the_button_was_toggled)

        self.setFixedSize(QSize(400,300))
        self.setCentralWidget(button)
    def clicked_button(self):
        print("Это сильно!")
    def the_button_was_toggled(self, checked):
        print("Checked?", checked)

class MainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_toggled)
        # button.setChecked(self.button_is_checked)

        self.setCentralWidget(button)

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked

        print(self.button_is_checked)

class MainWindow3(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)

        # Также меняем заголовок окна.
        self.setWindowTitle("My Oneshot App")

import sys
from random import choice
window_titles = [
            'My App',
            'My App',
            'Still My App',
            'Still My App',
            'What on earth',
            'What on earth',
            'This is surprising',
            'This is surprising',
            'Something went wrong'
        ]
class MainWindow4(QMainWindow):
    def __init__(self):
        super().__init__()
        

        self.n_times_clicked = 0

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(self.the_window_title_changed)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        print("Setting title:  %s" % new_window_title)
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)

        if window_title == 'Something went wrong':
            self.button.setDisabled(True)



app=QApplication(sys.argv)

window=MainWindow4()
window.show()

app.exec()


# Приложение не доберётся сюда, пока вы не выйдете и цикл
# событий не остановится.