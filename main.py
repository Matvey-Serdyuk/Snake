from tkinter import Tk, Canvas, Label, Frame, LEFT, Button
from time import sleep, clock
from threading import Thread
from random import randrange

class Main:
	def __init__(self):
		self.color = "#0f0"
		self.speed = 0.075
		self.times = 0

	def menu(self):
		self.master = Tk()
		self.master.geometry("840x630")
		but = Button(self.master, text="Играть", height=10, width=50, bg="#090", command=self.game_nav)
		but.pack()
		but1 = Button(self.master, text="Настройки", height=10, width=50, bg="#990", command=self.nas_nav)
		but1.pack()
		self.master.mainloop()

	def game_nav(self):
		self.master.destroy()
		self.game()

	def nas_nav(self):
		self.master.destroy()
		self.nas()

	def menu_nav(self):
		self.master.destroy()
		self.move = False
		self.menu()

	def nas(self):
		self.master = Tk()
		self.master.geometry("840x630")
		frame = Frame(self.master)
		frame1 = Frame(self.master)
		frame2 = Frame(self.master)
		but = Button(frame, text="В меню", height=4, width=20, bg="#090", command=self.menu_nav)
		label_color = Label(frame1, text="Изменить цвет змейки")
		but1 = Button(frame1, text="Зеленый", height=4, width=20, bg="#0f0", command=self.green)
		but2 = Button(frame1, text="Красный", height=4, width=20, bg="#f00", command=self.red)
		but3 = Button(frame1, text="Синий", height=4, width=20, bg="#00f", command=self.blue)
		but4 = Button(frame1, text="Желтый", height=4, width=20, bg="#ff0", command=self.yellow)
		but5 = Button(frame1, text="Белый", height=4, width=20, bg="#fff", command=self.white)
		label_speed = Label(frame2, text="Изменить Скорость змейки")
		button = Button(frame2, text="Медленая", height=4, width=20, bg="#0f0", command=self.speed_min)
		button1 = Button(frame2, text="Нормальная", height=4, width=20, bg="#ff0", command=self.speed_norm)
		button2 = Button(frame2, text="Быстрая", height=4, width=20, bg="#f00", command=self.speed_max)
		frame.pack()
		frame1.pack()
		frame2.pack()
		but.pack()
		label_color.pack(padx=10, pady=10)
		but1.pack(side=LEFT, padx=5, pady=5)
		but2.pack(side=LEFT, padx=5, pady=5)
		but3.pack(side=LEFT, padx=5, pady=5)
		but4.pack(side=LEFT, padx=5, pady=5)
		but5.pack(side=LEFT, padx=5, pady=5)
		label_speed.pack(padx=10, pady=10)
		button.pack(side=LEFT, padx=5, pady=5)
		button1.pack(side=LEFT, padx=5, pady=5)
		button2.pack(side=LEFT, padx=5, pady=5)
		self.master.mainloop()

	def green(self):
		self.color = "#0f0"
	def red(self):
		self.color = "#f00"
	def blue(self):
		self.color = "#00f"
	def yellow(self):
		self.color = "#ff0"
	def white(self):
		self.color = "#fff"

	def speed_min(self):
		self.speed = 0.1
	def speed_norm(self):
		self.speed = 0.075
	def speed_max(self):
		self.speed = 0.05

	def game(self):
		self.way = "stop"
		self.move = True
		self.score = 0
		self.master = Tk()
		self.label_score = Label(text=str(self.score))
		but = Button(self.master, text="Меню", bg="#cc0", command=self.menu_nav)
		but.pack()
		self.canvas = Canvas(self.master, width="840", height="630", bg="#111")
		self.head = self.canvas.create_rectangle(390, 270, 420, 300, outline="#000", fill=self.color)
		self.snake = [self.head, self.canvas.create_rectangle(390, 270, 420, 300, outline="#000", fill=self.color)]
		self.add_eat()
		self.canvas.pack()
		self.label_score.pack()
		self.master.bind("<KeyPress>", self.press)
		t = Thread(target=self.worker)
		t.start()
		self.master.mainloop()
		self.move = False

	def press(self, event):
		if (event.keycode == 87 or event.keycode == 38) and self.way != "botton":
			self.way = "top"
		elif (event.keycode == 65 or event.keycode == 37) and self.way != "right":
			self.way = "left"
		elif (event.keycode == 68 or event.keycode == 39) and self.way != "left":
			self.way = "right"
		elif (event.keycode == 83 or event.keycode == 40) and self.way != "top":
			self.way = "botton"

	def worker(self):
		while self.move:
			if self.canvas.coords(self.head) == self.canvas.coords(self.eat):
				self.snake.append(self.canvas.create_rectangle(self.canvas.coords(self.snake[len(self.snake) - 1]), outline="#000", fill=self.color))
				self.canvas.delete(self.eat)
				self.add_eat()
				self.score += 1
				self.label_score.config(text=str(self.score))

			for i in range(len(self.snake)-1, -1, -1):
				if i > 1:
					if self.canvas.coords(self.head) == self.canvas.coords(self.snake[i]):
						print("We lose")
						self.move = False
						break
					self.canvas.coords(self.snake[i], self.canvas.coords(self.snake[i-1]))
				elif i == 1:
					self.canvas.coords(self.snake[i], self.canvas.coords(self.head))
			if self.way == "top":
				if self.speed - (clock() - self.times) > 0:
					sleep(self.speed - (clock() - self.times))
				else:
					sleep(self.speed)
				self.canvas.move(self.head, 0, -30)
			elif self.way == "left":
				if self.speed - (clock() - self.times) > 0:
					sleep(self.speed - (clock() - self.times))
				else:
					sleep(self.speed)
				self.canvas.move(self.head, -30, 0)
			elif self.way == "right":
				if self.speed - (clock() - self.times) > 0:
					sleep(self.speed - (clock() - self.times))
				else:
					sleep(self.speed)
				self.canvas.move(self.head, 30, 0)
			elif self.way == "botton":
				if self.speed - (clock() - self.times) > 0:
					sleep(self.speed - (clock() - self.times))
				else:
					sleep(self.speed)
				self.canvas.move(self.head, 0, 30)
			self.times = clock()
			# left
			if self.canvas.coords(self.head)[2] < 30:
				self.canvas.coords(self.head, (810, self.canvas.coords(self.head)[1], 840, self.canvas.coords(self.head)[3]))
			# top
			elif self.canvas.coords(self.head)[3] < 30:
				self.canvas.coords(self.head, (self.canvas.coords(self.head)[0], 600, self.canvas.coords(self.head)[2], 630))
			# right
			elif self.canvas.coords(self.head)[0] > 810:
				self.canvas.coords(self.head, (0, self.canvas.coords(self.head)[1], 30, self.canvas.coords(self.head)[3]))
			# botton
			elif self.canvas.coords(self.head)[1] > 600:
				self.canvas.coords(self.head, (self.canvas.coords(self.head)[0], 0, self.canvas.coords(self.head)[2], 30))

	def add_eat(self):
		x = randrange(0, 28) * 30
		y = randrange(0, 21) * 30
		self.eat = self.canvas.create_rectangle(x, y, x+30, y+30, outline="#000", fill="#990")


Main().menu()