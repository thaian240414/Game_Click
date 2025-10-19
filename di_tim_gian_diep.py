from guizero import App, Text, PushButton, Box, info


app = App(title="Đi tìm gián điệp", width=1000, height=1000, bg="white")
 



text = Text(app, text="Đi tìm gián điệp", size=40, color="black", font="Times New Roman")

box = Box(app, layout="grid")

def thong_bao_1():
    info("Sai rồi","Gián điệp không có ở đây hãy thử lại")

WIDTH=20
HEIGHT=10
button1 = PushButton(box, text="?",grid=[0,0], command= thong_bao_1, pady = 30, padx = 30, width=WIDTH, height=HEIGHT)

button2 = PushButton(box, text="?", grid=[1,0], command= thong_bao_1, pady = 30, padx = 30, width=WIDTH, height=HEIGHT)


button3 = PushButton(box, text="?", grid=[2,0], command= thong_bao_1, pady = 30, padx = 30,  width=WIDTH, height=HEIGHT )


button4 = PushButton(box, text="?", grid=[0,1], command= thong_bao_1, pady = 30, padx = 30,  width=WIDTH, height=HEIGHT)


button5 = PushButton(box, text="?",grid=[1,1], command= thong_bao_1, pady = 30, padx = 30,  width=WIDTH, height=HEIGHT)


button6 = PushButton(box, text="?", grid=[2,1], command= thong_bao_1, pady = 30, padx = 30,  width=WIDTH, height=HEIGHT)


button7 = PushButton(box, text="?",grid=[0,2], command= thong_bao_1, pady = 30, padx = 30,  width=WIDTH, height=HEIGHT)


def thong_bao_2():
    button8.image="meomeospy.png"
    button8.resize(200, 200)
    info("Gián điệp", "Bạn đã tìm ra gián điệp")

button8 = PushButton(box, text="?",grid=[1,2], command=thong_bao_2, pady = 30, padx = 30,  width=WIDTH, height=HEIGHT)



button9 = PushButton(box, text="?",grid=[2,2], command= thong_bao_1, pady = 30, padx = 30,  width=WIDTH, height=HEIGHT)



app.display()