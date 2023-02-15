import sys


def divide(a, b):
    return a / b


try:
    divide(3, 0)
except:
    print("Unexpected error:", sys.exc_info()[0])
    print("오류가 발생하여 예외처리 하였습니다.")


try:
    file = open("notexistfile", "r")
except FileNotFoundError as error:
    print(error)
    print("오류가 발생하여 예외처리 하였습니다.")
finally:
    print("최종적으로 실행되는 내용입니다.")
