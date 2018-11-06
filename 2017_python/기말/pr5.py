from tkinter import*
global balance
global rate

wn = Tk()
wn.title('tk')
wn.geometry('435x150')

ba = Label(wn, text = 'Balance:')
ra = Label(wn, text = 'Rate:')

balance= 0
rate= 0

bal = Label(wn, text = '%d'%balance)
rat = Label(wn, text = '%d'%rate)

def Deposit():
    global balance
    bal.configure(text = '%d'%(balance+int(e1.get())))
    balance = balance+int(e1.get())
    
def Withdraw():
    global balance
    bal.configure(text = '%d'%(balance-int(e2.get())))
    balance = balance-int(e2.get())

def Interest():
    rat.configure(text = '%d'%(balance*float(e3.get())))

e1 = Entry(wn)
e2 = Entry(wn)
e3 = Entry(wn)

btn1 = Button(wn, text = 'Deposit', command = Deposit)
btn2 = Button(wn, text = 'Withdraw', command = Withdraw)
btn3 = Button(wn, text = 'Interest rate', command = Interest)


ba.grid(column = 1, row = 0)
bal.grid(column = 1, row = 1)
ra.grid(column = 1, row = 2)
rat.grid(column = 1, row = 3)
e1.grid(column = 0, row = 4)
e2.grid(column = 1, row = 4)
e3.grid(column = 2, row = 4)
btn1.grid(column = 0, row = 5)
btn2.grid(column = 1, row = 5)
btn3.grid(column = 2, row = 5)
