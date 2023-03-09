# 문자열 변수 초기화
string_content = "Hello World!"
print(string_content)

string_content = 'Hello World!'
print(string_content)

string_content = """Hello World!"""
print(string_content)

string_content = '''Hello World!'''
print(string_content)

string_content = "Hello World!\nI'm a console window."
print(string_content)

string_content = """Hello World!
I'm a console window."""
print(string_content)

# 문자열 더하기
string_content = string_content + " Engineeringcode! "
print(string_content)

# 문자열 곱하기
string_content = string_content * 2
print(string_content)

print("length of string_content: " + str(len(string_content)))

print("The character in index 1 of string_content: "+string_content[1])

# 문자열 자르기
sliced_string = string_content[0:5]
print(sliced_string)

sliced_string = string_content[0:-17]
print(sliced_string)

sliced_string = string_content[:]
print(sliced_string)

# 문자열 포맷
number_of_apple = 3
brand_name_of_apple = "Gyeongju"
print("I ate %d apple(s) from %s" % (number_of_apple, brand_name_of_apple))

print("I ate %5d apple(s)" % number_of_apple)
print("I ate {0:>5} apple(s)" .format(number_of_apple))
print("I ate {0:<5} apple(s)" .format(number_of_apple))
print("I ate {0:^5} apple(s)" .format(number_of_apple))
print("I ate {0:0>5} apple(s)" .format(number_of_apple))
print("I ate {0:0<5} apple(s)" .format(number_of_apple))
print("I ate {0:0^5} apple(s)" .format(number_of_apple))
print(f"I ate {number_of_apple} apple(s) from {brand_name_of_apple}")
