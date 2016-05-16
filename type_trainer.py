from tkinter import *
from time import *
import tkinter
import random
import math
import datetime
FONT = (None, 50)

alfabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
new_word = lambda: random.choice(random.choice((alfabet[0:len(alfabet)//10], alfabet)))

root = Tk()
root.title("Клавиатурный тренажер")

# поле для вывода  времени
pole_to_time = Label(font=20, text="у вас 60 сек.")
pole_to_time.pack()
# поле для вывода текста
pole_to_copy = Label(root, text = "старт", font=FONT)
pole_to_copy.pack()
# поле для ввода текста
typing_ground = Entry(root, font=FONT)
typing_ground.pack()

points = Label(root, text = "score: 0", font=FONT)
points.pack()





# если введенное=выведенному на экране  то стираеться и выводиться новое
def equal(ev):

    if pole_to_copy.cget("text") == typing_ground.get():
        typing_ground.delete(0, 'end')
        pole_to_copy['text'] = new_word()
        points['text'] = "score: " + str(int(points['text'].split(': ')[-1]) + 1)
def timer():
    if pole_to_copy.cget("text") == typing_ground.get():
        start_timer=time()
        struct=localtime( start_timer)

        i=5
        while i>-1:
            pole_to_time['text']=i
            i-=1
            sleep(1)
    end_timer=time()





root.bind('<Key>', equal,timer)

root.mainloop()