#파일 이름을 turtle로 저장하면 안됨!

import turtle
wn = turtle.Screen()#window object
wn.title('turtle No1')
wn.setup(400,400)

t1 = turtle.Turtle()
t1.shape('turtle')#circle은 방향성이 애매해서 안하는게 좋다.앞뒤 확실한걸로.
t1.color('red')

def test():
    t1.forward(30)

#squre
for _ in range(4):
    t1.forward(100)
    t1.left(90)


#t1.forward(50)
#t1.forward(-50)#이렇게 하면 backward안써도 된다. 섞어쓰면 오히려 헷갈릴수도.
#t1.left(90)#degree
#t1.right(-90)#left 180
#t1.goto(50,100)#직선으로 움직인다.
#print(t1.distance(0,0))


wn.onkey(test,'Up')#방향키, test라는 함수 실행. window가 받음.
wn.onkey(quit,'q')#quit은 프로그램 종료.
wn.listen()#해줘야 듣는다.

wn.onscreenclick(t1.goto)#goto where clicked position.좌표값을 받는 함수.


wn.mainloop()#pycharm 은 붙여줘야한다.

