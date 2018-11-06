import time, threading

def test():#id는 쓰레드 구분을 위한 표준.없어도됨.
    for i in range(1,10):
        time.sleep(1)
        print('# test %d %s'%(i, th1.getName()))

class test1(threading.Thread):#스레드를 상속받아 클래스 생성.
    def run(self):
        for i in range(1,10):
            time.sleep(1)
            print('&&&&&&&')

th1 = threading.Thread(target=test,args=())
th2 = test1()#함수랑 스레드 만드는 법이 다르다.
th1.setName('All Die')
th1.start()
th2.start()
#threading.Tread(target=function,args=(id)).start() // doesn't need thread name

for i in range(1,10):
    time.sleep(0.5)#second
    print('+ main : %d'%i)

th1.join()
th2.join()
