import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from in_game_windowlvl2 import Game_window_lvl2
from in_game_window_lvl1 import Game_window


class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui files/main_menu_window.ui", self)
        self.new_game_button.clicked.connect(self.open_new_game)
        self.close_button.clicked.connect(self.close)

    def close(self):
        QMainWindow.close(self)

    def open_new_game(self):
        shahid.show()
        QMainWindow.close(self)


class To_lvl(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui files/to_lvl.ui", self)
        self.to_lvl1_button.clicked.connect(self.to_lvl1)
        self.to_lvl2_button.clicked.connect(self.to_lvl2)

    def to_lvl1(self):
        alah.show()
        QMainWindow.close(self)

    def to_lvl2(self):
        kashmir.show()
        QMainWindow.close(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_Window()
    ex.show()
    shahid = To_lvl()
    kashmir = Game_window_lvl2()
    alah = Game_window()
    sys.exit(app.exec_())