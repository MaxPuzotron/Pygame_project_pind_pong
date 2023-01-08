# Импорт библиотек
import sys
import PyQt5

# Импорт функций библиотек
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# Импорт файлов
from in_game_windowlvl2 import Game_window_lvl2
from in_game_window_lvl1 import Game_window_lvl1


# Класс отвечающий за открытие главного окна
class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui files/main_menu_window.ui", self)
        self.new_game_button.clicked.connect(self.open_new_game)
        self.close_button.clicked.connect(self.close)

    # Функция закрытия главного окна
    def close(self):
        QMainWindow.close(self)

    # Функция открытия класса To_lvl
    def open_new_game(self):
        QMainWindow.close(self)
        shahid.show()


# Класс отвечающий за открытие окна меню уровней
class To_lvl(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui files/to_lvl.ui", self)
        self.to_lvl1_button.clicked.connect(self.to_lvl1)
        self.to_lvl2_button.clicked.connect(self.to_lvl2)

    # Функция открывающая окно 1 уровня
    def to_lvl1(self):
        QMainWindow.close(self)
        alah.show()

    # Функция открывающая окно 2 уровня
    def to_lvl2(self):
        QMainWindow.close(self)
        kashmir.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_Window()
    ex.show()
    shahid = To_lvl()
    kashmir = Game_window_lvl2()
    alah = Game_window_lvl1()
    sys.exit(app.exec_())
