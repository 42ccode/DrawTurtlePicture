import turtle
import colorsys

# 设置画布
screen = turtle.Screen()
screen.bgcolor('black')
screen.title('绘制曼荼罗')

# 创建画笔对象
t = turtle.Turtle()
t.speed(0)  # 设置最快速度
t.width(2)  # 设置画笔宽度

# 曼荼罗颜色
n = 36
h = 0
turtle.tracer(50)
for i in range(100):
    c = colorsys.hsv_to_rgb(h, 1.0, 1.0)
    h += 1/n
    t.color(c)
    t.begin_fill()
    for j in range(2):
        t.forward(i * 3)
        t.right(60)
        t.forward(i * 3)
        t.right(120)
    t.end_fill()
    t.right(10)

turtle.done()
