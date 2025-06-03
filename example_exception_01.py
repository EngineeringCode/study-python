import traceback

a = 1
b = 0

try:
    print(f'{a} + {b} = {a+b}')
    print(f'{a} / {b} = {a / b}')
except:
    print(traceback.format_exc())
