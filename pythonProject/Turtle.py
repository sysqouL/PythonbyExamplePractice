# ---------------------------------------
# Turtle graphic
"""
import turtle
turtle.shape("turtle")
for i in range(0, 10):
    turtle.right(36)
    for i in range(0, 5):
        turtle.forward(200)
        turtle.right(72)
turtle.exitonclick()
"""

"""
# scr = turtle.Screen() - для использования сокращенной записи scr вместо turtle.Screen
# scr.bgcolor("yellow") - изменить цвет фона на заданный (по умолчанию белый)
# turtle.penup() - отключает перо, что бы не было видимого следа
# turtle.pendown() - включает перо (по умолчанию вкл)
# turtle.left(120)/right(90) - поворачивает черепаху на лево/право на заданное число градусов
# turtle.pensize(3) - устанавливает толщину пера
# turtle.forward(50) - перемещает черепаху вперед на заданное количество шагов
# turtle.shape("turtle") - изменяет вид черепахи на черепаху (по умолчанию вид стрелки)
# turtle.hideturtle() - скрывает черепаху
# turtle.showturtle() - отображает черепаху
# turtle.begin_fill() - выполняется перед кодом,рисующим фигуру, чтобы она была заполнена
# turtle.end_fill() - после кода, что бы откл заполнение
# turtle.color("black, "red") - определяет цвета заполнения фигур. В данном случае черный контур и красная заливка. До рисования фигуры
# turtle.exitonclick() - закрытие по щелчку
# turtle.position() - выводит координаты черепахи
"""


# ---------------------------------------
"""
# 60 Exercise Квадрат
import turtle
turtle.color("red", "black")
for i in range(0, 4):
    turtle.begin_fill()
    turtle.forward(180)
    turtle.right(90)
turtle.exitonclick()
"""
# ---------------------------------------


# ---------------------------------------
"""
# 61 Exercise Треугольник
import turtle
for i in range(0, 6):
    turtle.forward(180)
    turtle.left(120)
turtle.exitonclick()
"""
# ---------------------------------------


# ---------------------------------------
"""
# 62 Exercise Круг
import turtle
for i in range(0, 72):
    turtle.forward(10)
    turtle.right(10)
turtle.exitonclick()
"""
# ---------------------------------------


# ---------------------------------------
"""
# 62 Exercise 3 Квадрата в ряд
import turtle
turtle.screensize(2000, 1500)
turtle.color("black", "red")
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(90)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(200)

turtle.pendown()
turtle.color("yellow", "green")
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(90)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(200)

turtle.pendown()
turtle.color("black", "violet")
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(90)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.exitonclick()
"""
# ---------------------------------------


# ---------------------------------------
"""
# 64 Exercise Звезда
import turtle
turtle.color("black", "red")
turtle.begin_fill()
for i in range(0, 5):
    turtle.forward(250)
    turtle.left(144)
turtle.end_fill()
turtle.exitonclick()
"""
# ---------------------------------------
