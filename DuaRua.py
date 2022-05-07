import time
import turtle as t
import random

screen = t.Screen ()
screen.setup (1000, 800)

# Đặt biến vị trí mốc phía trên bên trái đường đua
X0 = -300
Y0 = 200
distance = 40

# Chuyển về mốc đường đua để vẽ
t.speed (10)
t.penup ()
t.goto (X0, Y0)

# Vẽ đường đua và cột mốc
for i in range (16):
    t. goto (X0 + i*40, Y0)
    t.write (i, font = [13])
    t.rt (90)
    for j in range (10):
        t.fd (5)
        t.pendown ()
        t.fd (30)
        t.penup ()
        t.fd (5)
    t.fd (18)
    t.lt (90)
    t.write (i, font = [13])
t.hideturtle ()

# Tạo các con rùa
allTurtles = []
xPosition = X0
yPosition = [100, 60, 20, -20, -60, -100]
colors = ["red", "green", "blue", "orange", "black", "violet"]

for i in range (6):
    turtle = t.Turtle (shape = "turtle")
    turtle.color (colors[i])
    turtle.penup ()
    turtle.goto (xPosition, yPosition[i])
    # Lưu vào list (các con rùa là biến, lưu vào list)
    allTurtles.append (turtle)

# Tạo biến để làm điều kiện chạy đua
run = True
bxh = []
i = 0
ruaVeDich = []

# Tạo hàm di chuyển về phía trước cho các con rùa
def turtleRun (turtles):
    global run, bxh, i, time0, ruaVeDich
    kq = []
    for turtle in turtles:
        if colors [turtles.index (turtle)] in ruaVeDich:
            continue
        else:
            turtle.fd (random.randint (10, 20))
        if turtle.xcor () >= abs (X0):
            timeEnd = time.time () - time0
            i += 1
            ruaVeDich.append (colors[turtles.index (turtle)])
            kq = ["Turtle number " + str(i) +  ": " + colors [turtles.index (turtle)], "running time: " + str( round (timeEnd, 5)) + " second"]
            bxh.append (kq)
        else:
            continue
        if i == 6:
            run = False
            break
            
# Tạo biến guess bật cửa sổ để người dùng nhập vào dự đoán
guess = screen.textinput (title = "Which turtle will win?", prompt = "input your choice.\n\
(red, green, blue, orange, black, violet)")

# Chạy đua
while True:
    time0 = time.time ()
    for turtle in allTurtles:
        turtle.goto (xPosition, yPosition[allTurtles.index (turtle)])
    while run == True:
        turtleRun (allTurtles)
    print ("Your choice:", guess)
    print ("Ranking:")
    for turtle in bxh:
        print (turtle)
    # print ("Ranking:", bxh)
        # Thông báo kết quả cuộc đua.
    if guess in (bxh [0][0]):
        play = screen.textinput (title = "WIN", prompt = "Congratulations! You win! \nDo you want to play again? (Y/N)")
        if play == "Y" or play == "y":
            guess = screen.textinput (title = "Which turtle will win?", prompt = "input your choice. \n\
(red, green, blue, orange, black, violet)")
            run = True
            i = 0
            bxh = []
            ruaVeDich = []
        else:
            break
    else:
        play = screen.textinput (title = "LOSE", prompt = "Sorry! You lose! \nDo you want to play again? (Y/N)")
        if play == "Y" or play == "y":
            guess = screen.textinput (title = "Which turtle will win?", prompt = "input your choice. \n\
(red, green, blue, orange, black, violet)")
            run = True
            i = 0
            bxh = []
            ruaVeDich = []
        else:
            break
 
t.done ()
# screen.exitonclick ()
    

