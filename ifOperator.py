# if False:
#     print('if')
# elif False:
#     print('elif')
# else:
#     print('else')


# x = 3
# if x == 0:
#     print('if')
# elif x > 0:
#     print('elif')
# else:
#     print('else')


# x = 0
# if x == 0:
#     x += 1
# print(int(5/x))


# y = int(input('Введите число: '))
# if y > 0:
#     y = str(y)+' is more than 0'
# elif y <= 0:
#     y = str(y)+' is less than 0'
# else:
#     y = 'NaN'
# print(y)


# x = float(input('Input number: '))
# if x == 0:
#     x = 1
#     print('x was 0')
# elif type(x) == type(5) or type(x) == type(5.5):
#     print('x is acceptable')
# else:
#     print('In x was not allowed')
#     x = 1
# print(float(100/x))


import time
import os

# On Linux
# while True:
#     print(os.name)
# os.mkdir("/home/ivan/Downloads/Test1")
# os.rmdir("/home/ivan/Downloads/Test1")
# print("The specified directories are removed successfully")
# print("The current working directory is: ", os.getcwd())
# print(os.listdir("/home/ivan/Рабочий стол"))

while True:
    sayt = input('Input website\n')
    if sayt == 'завершить':
        break
    if 'https://' in sayt:
        os.system('google-chrome ' + sayt)
        print('if')
    elif 'www.' in sayt:
        sayt = 'https://'+sayt
        os.system('google-chrome '+sayt)
        print('elif')
    else:
        sayt = 'https://www.'+sayt
        os.system('google-chrome '+sayt)
        print('else')

# os.system('start '+'https://www.youtube.com')
# time.sleep(5)
# os.startfile('C://Program Files/program.exe')
