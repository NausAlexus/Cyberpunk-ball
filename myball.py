# Импортируем необходимые библиотеки
from tkinter import *
from tkinter import ttk
import time
import random


# Создаём окно меню
root = Tk()
root.title('Cyberpunk Ball')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2.5
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 3
root.wm_geometry("+%d+%d" % (x, y))
root.iconbitmap('images/ico.ico')
root.resizable(False, False)
root.wm_attributes('-topmost', 1) # Чтобы окно игры было всегда поверх других окон
root.image = PhotoImage(file='images/background1.png')
bg_logo = Label(root, image=root.image)
bg_logo.grid(row=0, column=0)

# Создаем игровое поле
def game_word():
    root.destroy()
    window = Tk()
    window.title('Cyberpunk Ball')
    x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2.5
    y = (window.winfo_screenheight() - window.winfo_reqheight()) / 3
    window.wm_geometry("+%d+%d" % (x, y))
    window.geometry('500x400')
    window.iconbitmap('images/ico.ico')
    window.resizable(False, False)
    window.wm_attributes('-topmost', 1)  # Чтобы окно игры было всегда поверх других окон
    canvas = Canvas(window, width=500, height=400, highlightthickness=0)
    canvas.image = PhotoImage(file='images/background2.png')
    canvas.create_image(0, 0, anchor="nw", image=canvas.image)
    canvas.pack()
    window.update()

    # Создаем шарик
    class Ball:
        def __init__(self, canvas, paddle, score, color):
            self.canvas = canvas
            self.paddle = paddle
            self.score = score
            self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
            self.canvas.move(self.id, 245, 100)
            starts = [-2, -1, 1, 2]
            random.shuffle(starts)
            self.x = starts[0]
            self.y = -2
            self.canvas_height = self.canvas.winfo_height()
            self.canvas_width = self.canvas.winfo_width()
            self.hit_bottom = False

        # обрабатываем касание платформы, для этого получаем 4 координаты шарика в переменной pos (левая верхняя и правая нижняя точки)
        def hit_paddle(self, pos):
            paddle_pos = self.canvas.coords(self.paddle.id)
            if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                    self.score.hit()
                    return True
            return False

        # обрабатываем отрисовку шарика
        def draw(self):
            self.canvas.move(self.id, self.x, self.y)
            pos = self.canvas.coords(self.id)
            if pos[1] <= 0:
                self.y = 2
            if pos[3] >= self.canvas_height:
                self.hit_bottom = True
                canvas.create_text(250, 120, text='GAME OVER!', font=('Cyberpunk', 35), fill='red')
            if self.hit_paddle(pos) == True:
                self.y = -2
            if pos[0] <= 0:
                self.x = 2
            if pos[2] >= self.canvas_width:
                self.x = -2

    # Описываем класс Ball, который будет отвечать за шарик
    class Ball:
        def __init__(self, canvas, paddle, score, color):
            self.canvas = canvas
            self.paddle = paddle
            self.score = score
            self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
            self.canvas.move(self.id, 245, 100)
            starts = [-2, -1, 1, 2]
            random.shuffle(starts)
            self.x = starts[0]
            self.y = -2
            self.canvas_height = self.canvas.winfo_height()
            self.canvas_width = self.canvas.winfo_width()
            self.hit_bottom = False

        def hit_paddle(self, pos):
            paddle_pos = self.canvas.coords(self.paddle.id)
            if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                    self.score.hit()
                    return True
            return False

        def draw(self):
            self.canvas.move(self.id, self.x, self.y)
            pos = self.canvas.coords(self.id)
            if pos[1] <= 0:
                self.y = 2
            if pos[3] >= self.canvas_height:
                self.hit_bottom = True
                canvas.create_text(250, 170, text='GAME OVER!', font=('Cyberpunk', 35), fill='red')
            if self.hit_paddle(pos) == True:
                self.y = -2
            if pos[0] <= 0:
                self.x = 2
            if pos[2] >= self.canvas_width:
                self.x = -2

    # Описываем класс Paddle, который отвечает за платформы
    class Paddle:
        def __init__(self, canvas, color):
            self.canvas = canvas
            self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
            start_1 = [40, 60, 90, 120, 150, 180, 200]
            random.shuffle(start_1)
            self.starting_point_x = start_1[0]
            self.canvas.move(self.id, self.starting_point_x, 350)
            self.x = 0
            self.canvas_width = self.canvas.winfo_width()
            self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
            self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
            self.started = False
            self.canvas.bind_all('<KeyPress-Return>', self.start_game)

        def turn_right(self, event):
            self.x = 2

        def turn_left(self, event):
            self.x = -2

        def start_game(self, event):
            self.started = True

        def draw(self):
            self.canvas.move(self.id, self.x, 0)
            pos = self.canvas.coords(self.id)
            if pos[0] <= 0:
                self.x = 0
            elif pos[2] >= self.canvas_width:
                self.x = 0

    #  Описываем класс Score, который отвечает за отображение счетов
    class Score:
        def __init__(self, canvas, color):
            self.score = 0
            self.canvas = canvas
            self.id = canvas.create_text(450, 20, text=self.score, font=('Cyberpunk', 20), fill=color)

        def hit(self):
            self.score += 1
            self.canvas.itemconfig(self.id, text=self.score)

    # создаём объект — зелёный счёт
    score = Score(canvas, '#8716b8')
    # создаём объект — белую платформу
    paddle = Paddle(canvas, '#e31b7f')
    # создаём объект — красный шарик
    ball = Ball(canvas, paddle, score, '#dcfc08')
    # пока шарик не коснулся дна
    while not ball.hit_bottom:
        # если игра началась и платформа может двигаться
        if paddle.started == True:
            # двигаем шарик
            ball.draw()
            # двигаем платформу
            paddle.draw()
        # обновляем наше игровое поле, чтобы всё, что нужно, закончило рисоваться
        window.update_idletasks()
        # обновляем игровое поле, и смотрим за тем, чтобы всё, что должно было быть сделано — было сделано
        window.update()
        # замираем на одну сотую секунды, чтобы движение элементов выглядело плавно
        time.sleep(0.01)
    # если программа дошла досюда, значит, шарик коснулся дна. Ждём 3 секунды, пока игрок прочитает финальную надпись, и завершаем игру
    time.sleep(1)


btn_start_game = Button(width=15, height=1, font=('Cyberpunk', 15), text='START  GAME!', bg='#d4f542', command=game_word)
btn_start_game.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()