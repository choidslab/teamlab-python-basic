for i in range(10):
    try:
        print(i, 10 // i)
    except ZeroDivisionError as e:
        print(e)


# Error 종류

"""
IndexError 
NameError
ZeroDivisionError
ValueError
FileNotFoundError
등등
"""


# try ~ except ~ finally

try:
    for i in range(0, 10):
        result = 10 // i
        print(i, "------", result)
except ZeroDivisionError:
    print("Not divided by 0")
finally:
    print("종료되었습니다.")

# raise 구문
# 필요에 따라 강제로 Exception 발생을 위한 키워드

# while True:
#     value = input("변환할 정수 값을 입력: ")
#     for digit in value:
#         if digit not in "0123456789":
#             raise ValueError("숫자값을 입력하지 않으셨습니다.")
#     print("정수값으로 변환된 숫자 -", int(value))

# Assert 구문
# 특정 조건에 만족하지 않을 경우 예외 발생
# assert 예외조건

def get_binary_number(decimal_number):
    assert isinstance(decimal_number, int)
    return bin(decimal_number)

print(get_binary_number("a"))




