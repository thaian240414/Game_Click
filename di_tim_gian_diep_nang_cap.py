from guizero import App, Text, PushButton, Box, info
from random import randint

app = App(title="Đi tìm gián điệp", width=1000, height=1000, bg="white")

text = Text(app, text="Đi tìm gián điệp", size=40, color="black", font="Times New Roman")

box = Box(app, layout="grid")

random_so = randint(1,9)

so_lan_sai = 0

WIDTH = 20
HEIGHT = 10

def thong_bao_1(cell):
    global random_so, so_lan_sai
    if random_so == cell:
        if random_so == 1:
            button1.image = "meomeospy.png"
            button1.resize(200,200)
            info("Thắng rồi", "Bạn đã tìm ra gián điệp, hãy chơi lại")
         

        elif random_so == 2:
            button2.image = "meomeospy.png"
            button2.resize(200,200)
            info("Thắng rồi", "Bạn đã tìm ra gián điệp, hãy chơi lại")
       

        elif random_so == 3:
            button3.image = "meomeospy.png"
            button3.resize(200,200)
            info("Thắng rồi", "Bạn đã tìm ra gián điệp, hãy chơi lại")
            random_so = randint(1,9)


        elif random_so == 4:
            button4.image = "meomeospy.png"
            button4.resize(200,200)
            info("Thắng rồi", "Bạn đã tìm ra gián điệp, hãy chơi lại")
   

        elif random_so == 5:
            button5.image = "meomeospy.png"
            button5.resize(200,200)
            info("Thắng rồi", "Bạn đã tìm ra gián điệp, hãy chơi lại")
     

        elif random_so == 6:
            button6.image = "meomeospy.png"
            button6.resize(200,200)
            info("Thắng rồi", "Bạn đã tìm ra gián điệp, hãy chơi lại")
       


        elif random_so == 7:
            button7.image = "meomeospy.png"
            button7.resize(200,200)


        elif random_so == 8:
            button8.image = "meomeospy.png"
            button8.resize(200,200)
            info("Thắng rồi", "Bạn đã tìm ra gián điệp, hãy chơi lại")
  

        elif random_so == 9:
            button9.image = "meomeospy.png"
            button9.resize(200,200)
            info("Thắng rồi", "Bạn đã tìm ra gián điệp, hãy chơi lại")
            random_so = randint(1,9)
            so_lan_sai = 0

    else:
        info("Sai rồi", "Gián điệp không ở đây, hãy thử lại")
        so_lan_sai += 1
        if so_lan_sai == 3:
            info("Thua rồi", "Bạn đã đoán sai 3 lần! Hãy chơi lại")

def choi_lai():
    global random_so, so_lan_sai
    random_so = randint(1, 9)
    so_lan_sai = 0
    for b in buttons:
        b.text = "?"
        b.image = None
        b.width = WIDTH
        b.height = HEIGHT



button1 = PushButton(box, text="?",grid=[0,0], command= thong_bao_1,args=[1], pady = 30, padx = 30, width=WIDTH, height=HEIGHT)
button2 = PushButton(box, text="?", grid=[1,0], command= thong_bao_1,args=[2], pady = 30, padx = 30, width=WIDTH, height=HEIGHT)
button3 = PushButton(box, text="?", grid=[2,0], command= thong_bao_1,args=[3], pady = 30, padx = 30,  width=WIDTH, height=HEIGHT )
button4 = PushButton(box, text="?", grid=[0,1], command= thong_bao_1,args=[4], pady = 30, padx = 30,  width=WIDTH, height=HEIGHT)
button5 = PushButton(box, text="?",grid=[1,1], command= thong_bao_1,args=[5], pady = 30, padx = 30,  width=WIDTH, height=HEIGHT)
button6 = PushButton(box, text="?", grid=[2,1], command= thong_bao_1,args=[6], pady = 30, padx = 30,  width=WIDTH, height=HEIGHT)
button7 = PushButton(box, text="?",grid=[0,2], command= thong_bao_1,args=[7], pady = 30, padx = 30,  width=WIDTH, height=HEIGHT)
button8 = PushButton(box, text="?",grid=[1,2], command=thong_bao_1,args=[8], pady = 30, padx = 30,  width=WIDTH, height=HEIGHT)
button9 = PushButton(box, text="?",grid=[2,2], command= thong_bao_1,args=[9], pady = 30, padx = 30,  width=WIDTH, height=HEIGHT)


buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

nut_choi_lai = PushButton(app, text="Chơi lại", command=choi_lai, width=50, height=50)

app.display()
