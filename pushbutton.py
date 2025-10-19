from guizero import App, Text, PushButton, info

app = App(title="Click", bg="lightblue")



score = 0
up_score = 1
text = Text(app,text="Score: " + str(score), size=60, color="pink")


def click():
    global score
    score += 1
    text.value = "Score: " + str(score)


button_click = PushButton(app, command=click,image="cutedog.png", pady= 1, padx=2, align="right")

def upgrade():
    global up_score
    score += 9
    info("Thông báo", "Bạn đã nâng cấp lên 10")

def click2():
    global score
    score -= 10
    text.value = "Score: " + str(score)


button_click2 = PushButton(app, command=click2,image="money.png", pady= 2, padx=2, align="left")


upgrade = PushButton(app, text="Bấm vào bị trừ mười điểm", command=upgrade)
    




app.display()