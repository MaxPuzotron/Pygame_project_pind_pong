# Импорт библиотек
import sqlite3
import PyQt5
import sys
import pygame
import random

# Импорт функций библиотек
from pygame.locals import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Game_window_lvl2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui files/in_game_window_lvl2.ui", self)
        self.game_butoon.clicked.connect(self.game)
        self.clear_bt.clicked.connect(self.clear)

        # подключаем базу данных
        self.con = sqlite3.connect("parametres5.sqlite")
        cur = self.con.cursor()

        # получаем данные и инициализируем их в QLable
        self.result1 = cur.execute("SELECT * FROM left_player").fetchall()
        self.result2 = cur.execute("SELECT * FROM right_player").fetchall()

        self.left_wins.setText(str(self.result1[0][0]))
        self.left_loses.setText(str(self.result1[0][1]))

        self.right_wins.setText(str(self.result2[0][0]))
        self.right_loses.setText(str(self.result2[0][1]))

    # Функция открывающая игру на pygame
    def game(self):
        QMainWindow.close(self)
        self.game_lvl2()

    # Функция обновляющая счет
    def update_score(self, left_win):
        cur = self.con.cursor()
        self.result1 = cur.execute("SELECT * FROM left_player").fetchall()
        self.result2 = cur.execute("SELECT * FROM right_player").fetchall()
        lw = int(self.result1[0][0])
        ll = int(self.result1[0][1])
        rw = int(self.result2[0][0])
        rl = int(self.result2[0][1])
        print(lw, ll, rw, rl)
        print(
            "UPDATE left_player \n SET count_win = " + str(lw + 1) + "\n WHERE count_lose = " + str(
                ll))
        if left_win == 1:
            self.con.execute(
                "UPDATE left_player \n SET count_win = " + str(
                    lw + 1) + "\n WHERE count_lose = " + str(ll))
            self.con.commit()
            self.con.execute(
                "UPDATE right_player \n SET count_lose = " + str(
                    rl + 1) + "\n WHERE count_win = " + str(rw))
            self.con.commit()
        else:
            self.con.execute(
                "UPDATE left_player \n SET count_lose = " + str(
                    ll + 1) + "\n WHERE count_win = " + str(lw))
            self.con.commit()
            self.con.execute(
                "UPDATE right_player \n SET count_win = " + str(
                    rw + 1) + "\n WHERE count_lose = " + str(rl))
            self.con.commit()
        self.left_wins.setText(str(self.result1[0][0]))
        self.left_loses.setText(str(self.result1[0][1]))
        self.right_wins.setText(str(self.result2[0][0]))
        self.right_loses.setText(str(self.result2[0][1]))

    # Функция обнуляющая значение в базе данных и полях вывода
    def clear(self):
        cur = self.con.cursor()
        self.result1 = cur.execute("SELECT * FROM left_player").fetchall()
        self.result2 = cur.execute("SELECT * FROM right_player").fetchall()
        lw = int(self.result1[0][0])
        ll = int(self.result1[0][1])
        rw = int(self.result2[0][0])
        rl = int(self.result2[0][1])
        self.con.execute(
            "UPDATE left_player \n SET count_lose = 0 \n WHERE count_win =" + str(lw))
        self.con.execute(
            "UPDATE left_player \n SET count_win = 0 \n WHERE count_lose = 0")
        self.con.commit()
        self.con.execute(
            "UPDATE right_player \n SET count_win = 0 \n WHERE count_lose = " + str(rl))
        self.con.execute(
            "UPDATE right_player \n SET count_lose = 0 \n WHERE count_win = 0")
        self.con.commit()
        self.left_wins.setText(str(self.result1[0][0]))
        self.left_loses.setText(str(self.result1[0][1]))
        self.right_wins.setText(str(self.result2[0][0]))
        self.right_loses.setText(str(self.result2[0][1]))

    # Функция в которой находится игра на pygame
    def game_lvl2(self):
        run = 1
        while run == 1:
            winsize = [800, 600]
            black = [0, 0, 0]
            blue = [255, 255, 255]
            maxx = 780
            minx = 20
            maxy = 580
            miny = 0
            true = 1
            false = 0
            left = 1
            right = 0
            paddlestep = 4
            paddleleftxy = [5, 200]
            paddlerightxy = [775, 200]
            gameover = true
            ballxy = [200, 200]
            ballspeed = 4
            balldy = 1
            balldx = 1
            ballservice = true
            service = left
            scoreleft = 0
            scoreright = 0
            ballcludge = 0
            left_win = 0
            right_win = 0
            pygame.init()
            clock = pygame.time.Clock()
            screen = pygame.display.set_mode(winsize)
            pygame.display.set_caption('Ping Pong')
            screen.fill(black)
            paddle = pygame.image.load('sprites/paddle.png').convert()
            paddleerase = pygame.image.load('sprites/erase.png').convert()
            ball = pygame.image.load('sprites/1.png').convert()
            ballerase = pygame.image.load('sprites/ball.png').convert()
            while gameover == true:
                font = pygame.font.SysFont("Arial", 20)
                text_surface = font.render("Ping Pong", true, blue)
                screen.blit(text_surface, (80, 40))
                text_surface = font.render(
                    "Для управления левым игроком используйте клавиши 'A' и 'Z'.", true,
                    blue)
                screen.blit(text_surface, (80, 120))
                text_surface = font.render(
                    "Для управления правым игроком используйте клавиши вверх и вниз.",
                    true, blue)
                screen.blit(text_surface, (80, 160))
                text_surface = font.render("Нажмите 'S', чтобы шар начал двигаться", true, blue)
                screen.blit(text_surface, (80, 200))
                text_surface = font.render(
                    "'P' - пауза, 'R' - продолжить, 'N'- старт игры, 'Q' - выход из игры", true,
                    blue)
                screen.blit(text_surface, (80, 240))
                text_surface = font.render(
                    "Для игры должна стоять английская раскладка(для игроков на Macos).", true,
                    blue)
                screen.blit(text_surface, (80, 280))
                text_surface = font.render("Игра идёт до 6 очков", true,
                                           blue)
                screen.blit(text_surface, (80, 320))
                text_surface = font.render("Вы готовы играть в пинг понг.", true,
                                           blue)
                screen.blit(text_surface, (80, 360))
                pygame.display.update()
                anim = [pygame.image.load('images/1.png'), pygame.image.load('images/2.png'),
                        pygame.image.load('images/3.png'), pygame.image.load('images/4.png'),
                        pygame.image.load('images/5.png'), pygame.image.load('images/6.png')]
                anim_count = 0
                for i in range(13):
                    screen.blit(anim[anim_count], (350, 400))
                    if anim_count == 5:
                        anim_count = 0
                    else:
                        anim_count += 1
                    pygame.display.update()
                    clock.tick(10)
                while True:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            exit()
                            break
                    pressed_keys = pygame.key.get_pressed()
                    if pressed_keys[K_n]:
                        gameover = false
                        screen.fill(black)
                        break
                    elif pressed_keys[K_q]:
                        run = 0
                        break
                        exit()
                    clock.tick(20)
            while not gameover:
                screen.blit(paddleerase, paddleleftxy)
                screen.blit(paddleerase, paddlerightxy)
                screen.blit(ballerase, ballxy)
                font = pygame.font.SysFont("Arial", 45)
                if scoreleft > 5:
                    gameover = True
                    left_win = 1
                    self.update_score(left_win)
                if scoreright > 5:
                    gameover = True
                    left_win = 0
                    self.update_score(left_win)
                text_surface1 = font.render(str(scoreleft), true, blue)
                textleft = screen.blit(text_surface1, (40, 40))
                text_surface1 = font.render(str(scoreright), true, blue)
                textright = screen.blit(text_surface1, (700, 40))
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[K_a]:
                    if paddleleftxy[1] > miny:
                        paddleleftxy[1] = paddleleftxy[1] - paddlestep
                elif pressed_keys[K_z]:
                    if paddleleftxy[1] < maxy - 80:
                        paddleleftxy[1] = paddleleftxy[1] + paddlestep
                if pressed_keys[K_UP]:
                    if paddlerightxy[1] > miny:
                        paddlerightxy[1] = paddlerightxy[1] - paddlestep
                elif pressed_keys[K_DOWN]:
                    if paddlerightxy[1] < maxy - 80:
                        paddlerightxy[1] = paddlerightxy[1] + paddlestep
                if (pressed_keys[K_s] or pressed_keys[K_l]) and ballservice == true:
                    ballservice = false
                    if service == left:
                        balldx = random.randrange(2, 3)
                        balldy = random.randrange(-3, 3)
                        service = right
                    else:
                        balldx = random.randrange(2, 3)
                        balldy = random.randrange(-3, 3)
                        service == left
                if pressed_keys[K_q]:
                    run = 0
                    exit()
                if pressed_keys[K_p]:
                    gamepaused = true
                    font = pygame.font.SysFont("Arial", 64)
                    paused_surface = font.render("Paused", true, blue)
                    paused_rect = screen.blit(paused_surface, (300, 250))
                    pygame.display.update()
                    while gamepaused == true:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                exit()
                        pressed_keys = pygame.key.get_pressed()

                        if pressed_keys[K_r]:
                            gamepaused = false
                        clock.tick(20)
                    pygame.draw.rect(screen, black, paused_rect)
                if ballservice is not true:
                    if ballxy[0] < (paddleleftxy[0] + 20) and (paddleleftxy[1] - 18) < ballxy[1] < (
                            paddleleftxy[1] + 98):
                        balldx = -balldx
                        if pressed_keys[K_z] or pressed_keys[K_x]:
                            balldy = random.randrange(2, 4)
                        else:
                            balldy = random.randrange(0, 3)
                    elif ballxy[0] > (paddlerightxy[0] - 20) and (paddlerightxy[1] - 18) < ballxy[1] <= (
                            paddlerightxy[1] + 98):
                        if ballcludge == 0:
                            balldx = -balldx
                            if pressed_keys[K_UP] or pressed_keys[K_DOWN]:
                                balldy = random.randrange(2, 4)
                            else:
                                balldy = random.randrange(0, 3)
                            ballcludge = 1
                        else:
                            ballcludge = ballcludge + 1
                            if ballcludge == 4:
                                ballcludge = 0
                    elif ballxy[1] <= miny:
                        balldy = -balldy
                    elif ballxy[1] >= maxy:
                        balldy = -balldy
                    elif ballxy[0] <= minx:
                        ballservice = true
                        service = right
                        scoreright = scoreright + 1
                        pygame.draw.rect(screen, black, textright)
                    elif ballxy[0] >= maxx:
                        ballservice = true
                        service = left
                        scoreleft = scoreleft + 1
                        pygame.draw.rect(screen, black, textleft)
                    ballxy[0] = ballxy[0] + (ballspeed * balldx)
                    ballxy[1] = ballxy[1] + (ballspeed * balldy)
                else:
                    if service == left:
                        ballxy[0] = paddleleftxy[0] + 25
                        ballxy[1] = paddleleftxy[1] + 40
                    elif service == right:
                        ballxy[0] = paddlerightxy[0] - 25
                        ballxy[1] = paddlerightxy[1] + 40
                screen.blit(paddle, paddleleftxy)
                screen.blit(paddle, paddlerightxy)
                screen.blit(ball, ballxy)
                pygame.display.update()
                clock.tick(100)
            while True:
                screen.fill([0, 0, 0])
                font = pygame.font.SysFont("Times new roman", 20)
                text_surface = font.render("Раунд окончен!", true, blue)
                screen.blit(text_surface, (80, 60))
                text_surface = font.render("Поздравляем победителя.", true,
                                           blue)
                screen.blit(text_surface, (80, 90))
                text_surface = font.render(
                    "А проигравшему не отчаиваться, возможно в следующий раз победишь ты.", true,
                    blue)
                screen.blit(text_surface, (80, 120))
                text_surface = font.render("После этого раунда, вы можете сыграть следующий.", true,
                                           blue)
                screen.blit(text_surface, (80, 200))
                text_surface = font.render(
                    "Результат этой игры сохранится и вы сможете его увидеть.", true, blue)
                screen.blit(text_surface, (80, 240))
                text_surface = font.render(
                    "Если вы хотите его обнулить воспользуйтесь соответствующей кнопкой в меню.",
                    true,
                    blue)
                screen.blit(text_surface, (80, 280))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[K_n]:
                    gameover = false
                    screen.fill(black)
                elif pressed_keys[K_q]:
                    run = 0
                    exit()
                clock.tick(20)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Game_window_lvl2()
    ex.show()
    sys.exit(app.exec_())
