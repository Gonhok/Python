try:
    result = 5/0
except ZeroDivisionError:
    print('zderror')
except:
    print('error')
else:
    print('no error')
