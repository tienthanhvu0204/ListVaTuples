import turtle as t
import random

screen = t.Screen ()
screen.setup (1000, 800)
screen.title ("Rùa chạy đua")

# Tạo biến guess bật cửa sổ để người dùng nhập vào dự đoán
guess = screen.textinput (title = "Dự đoán rùa màu nào chiến thắng?", prompt = "Nhập vào màu rùa chiến thắng. \n\
(đỏ, xanh dương, xanh lá, nâu, vàng, tím)")

# tạo list color lưu màu các con rùa
color = ["red", "blue", "green", "brown", "yellow", "pink"]

# tạo list lưu y_position của các con rùa ở vị trí xuất phát
yPosition = [100, 50, 0, -50, -100, -150]
xPosition = -400

# List lưu các vận tốc ngẫu nhiên cho rùa
speed = [10, 20, 25, 15, 30, 5]

# list lưu các con rùa
allTurtle = []
run = True

# Thiết lập vị trí ban đầu cho rùa
for turtle in range (0, 6):
    turtles = t.Turtle (shape = "turtle")
    turtles.penup ()
    turtles.goto (x = xPosition, y = yPosition [turtle])
    turtles.color (color[turtle])

    allTurtle.append (turtles)

# Xây dựng hàm di chuyển về đích của
# mỗi con rùa, khoảng cách di chuyển được
# chọn ngẫu nhiên trong các giá trị
# được lưu trong list phía trên
def random_walk(turtles):
    global run
    for turtle in turtles:
        turtle.forward(random.choice(speed))
        # Kiểm tra điều kiện cán đích
        # Khi 1 con cán đích thì dừng lại
        if turtle.xcor() > 400:
            run = False

while run:
    random_walk (allTurtle)


t.done ()
screen.exitonclick ()
