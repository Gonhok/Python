# UDPPingerClient.py
from socket import *
import time

# Create a UDP socket 
# Notice the use of SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Set origin offset time(0.0S)
orgtime = time.time()

for i in range(10):
    #make message/프로그램 실행 후 메시지 생성 시 시간. 실제 송신시각과
    #오차가 있을 수 있다.
    message = 'Ping '+'%-3d'%(i+1)+ '%f'%(time.time()-orgtime)
    clientSocket.sendto(message.encode('utf-8'),('155.230.27.79',12000))
    #offset for RTT
    stime = time.time()
    #receive modified message from server & timeout detect
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        rttime = time.time() - stime
        clientSocket.settimeout(1)
    except timeout:
        print ('Request timed out')
        continue
    print(modifiedMessage.decode('utf-8') + '\t>>RTT : %f'%rttime)

clientSocket.close()
