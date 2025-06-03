import traceback

a = 1
b = 0

try:
    print(f'{a} + {b} = {a+b}')
    print(f'{a} / {b} = {a / b}')
except ZeroDivisionError as e:
    print('오류발생:', e)
    print(traceback.format_exc())
