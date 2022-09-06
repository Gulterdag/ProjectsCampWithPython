import turtle
import time
import random

hiz = 0.100

screen = turtle.Screen()
screen.screensize(600, 600)
screen.title('Çılgın Yılan İş Başında')
screen.bgcolor('blue')
screen.tracer(0)

yılan = turtle.Turtle()
yılan.speed(0)
yılan.shape('square')
yılan.color('red')
yılan.penup()
yılan.goto(0, 100)
yılan.direction = "stop"

renkler = ['yellow', 'red', 'blue']
renk = random.sample(renkler, 1)[0]

yemek = turtle.Turtle()
yemek.speed(0)
yemek.shape('circle')
yemek.shapesize(0.80,0.80)
yemek.color('red')
yemek.penup()
yemek.goto(0,0)

kuyruklar = []
puan = 0

yaz = turtle.Turtle()
yaz.speed(0)
yaz.shape("square")
yaz.color("black")
yaz.penup()
yaz.hideturtle()
yaz.goto(0, 260)
yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))


def move():
    if yılan.direction == "up":
        y = yılan.ycor()
        yılan.sety(y + 20)
    if yılan.direction == "down":
        y = yılan.ycor()
        yılan.sety(y - 20)
    if yılan.direction == "right":
        x = yılan.xcor()
        yılan.setx(x + 20)
    if yılan.direction == "left":
        x = yılan.xcor()
        yılan.setx(x - 20)


def go_up():
    if yılan.direction != "down":
        yılan.direction = "up"


def go_down():
    if yılan.direction != "up":
        yılan.direction = "down"


def go_right():
    if yılan.direction != "left":
        yılan.direction = "right"


def go_left():
    if yılan.direction != "right":
        yılan.direction = "left"


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")


while True:
    screen.update()

    if yılan.xcor() > 300 or yılan.xcor() < -300 or yılan.ycor() > 300 or yılan.ycor() < -300:
      time.sleep(1)
      yılan.goto(0, 0)
      yılan.direction = "stop"

      for kuyruk in kuyruklar:
         kuyruk.goto(1000, 1000)

      kuyruklar = []
      puan = 0
      yaz.clear()
      yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))

      hiz = 0.10

    if yılan.distance(yemek) < 20:
      x = random.randint(-250, 250)
      y = random.randint(-250, 250)
      yemek.goto(x, y)

      puan = puan + 10
      yaz.clear()
      yaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))

      hiz = hiz - 0.005

      yeni_kuyruk = turtle.Turtle()
      yeni_kuyruk.speed(0)
      yeni_kuyruk.shape("square")
      yeni_kuyruk.color("black")
      yeni_kuyruk.penup()
      kuyruklar.append(yeni_kuyruk)

    for index in range(len(kuyruklar) - 1, 0, -1):
      x = kuyruklar[index - 1].xcor()
      y = kuyruklar[index - 1].ycor()
      kuyruklar[index].goto(x, y)

    if len(kuyruklar) > 0:
      x = yılan.xcor()
      y = yılan.ycor()
      kuyruklar[0].goto(x, y)

    move()

    for segment in kuyruklar:
      if segment.distance(yılan) < 20:
         time.sleep(1)
         yılan.goto(0, 0)
         yılan.direction = "stop"
         for segment in kuyruklar:
            segment.goto(1000, 1000)
         kuyruklar = []
         puan = 0
         yaz.clear()
         yaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))
         hiz = 0.15

    time.sleep(hiz)