import threading

lock = threading.Lock()#lock을 만들어 줘서 print의 개행이 실행 되기 전에
#새로운 스레드가 끼어드는 걸 방지한다.

def test1(id):
    for i in range(1,10):
        lock.acquire()
        print('%d:%d **'%(id,i))
        lock.release()

l1 = [threading.Thread(target=test1, args=(i,)) for i in range(3)]

for temp in l1:
    temp.start()

for temp in l1:
    temp.join()
