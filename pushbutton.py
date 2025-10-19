from guizero import App, Text, PushButton, info

app = App(title="Click", bg="lightblue")



score = 0

text = Text(app,text="Score: " + str(score), size=60, color="pink")


def click():
    global score
    score += 1
    text.value = "Score: " + str(score)


button_click = PushButton(app, command=click,image="cutedog.png", pady= 1, padx=2, align="right")


def click2():
    global score
    score -= 10
    text.value = "Score: " + str(score)


button_click2 = PushButton(app, command=click2,image="money.png", pady= 2, padx=2, align="left")






app.display()
