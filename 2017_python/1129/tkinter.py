#import tkinter => 일일이 tkinter적기 귀찮다
from tkinter import*

wn= Tk()#원래는 tkinter.Tk()
wn.title('Tkinter no1')
wn.geometry('400x400')#+는 왼쪽 위쪽 간격

def test():
    l1.configure(text=e1.get())#configure => l1의 설정을 다시 바꿈.
    #e1.get()으로 entry값 받아옴. int로 쓰고싶으면 casting

l1 = Label(wn, text = 'Na Label eda')
btn1 = Button(wn, text = 'ok', command = test)#함수뒤에 괄호 안적어도되네.
e1 = Entry(wn)#입력처리.

btn2 = Button(wn, text = 'up')
btn3 = Button(wn, text = 'down')
btn4 = Button(wn, text = 'left')
btn5 = Button(wn, text = 'right')

l1.pack()#이거 해야 붙는다. pack은 꼭 뒤에.
e1.pack()
btn1.pack()


#l1.grid(column = 0,row = 4, columnspan=2)#grid랑 pack동시에 안되는둣.

#btn2.grid(column = 0, row = 0, columnspan=2)
#btn3.grid(column = 0, row = 3, columnspan=2)
#btn4.grid(column = 0, row = 2)
#btn5.grid(column = 1, row = 2)


#l1.pack()#이거 해야 붙는다. pack은 꼭 뒤에.
#btn1.pack()
