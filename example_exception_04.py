import traceback

a = 1
b = 1
c = [1, 2, 3]

try:
    print(f'{a} + {b} = {a+b}')
    print(f'{a} / {b} = {a / b}')
    print(c[2])
except ZeroDivisionError as e:
    print('오류발생:', e)
    print(traceback.format_exc())
else:
    print('정상 동작 완료')
