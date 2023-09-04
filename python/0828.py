# def test():
#     print("A 지점 통과")
#     yield 1
#     print('B 지점 통과')
#     yield 2
#     print('C 지점 통과')

# output = test()

# print('D 지점 통과')
# a = next(output)
# print(a)
# print('E 지점 통과')
# b = next(output)
# print(b)
# print('F 지점 통과')

# next(output)


# user_input_a = input('정수 입력> ')

# if user_input_a.isdigit():
#     number_input_a = int(user_input_a)

#     print('원의 반지름:', number_input_a)
#     print('원의 둘레:', 2 * 3.14 * number_input_a)
#     print('원의 넓이:', 3.14 * number_input_a * number_input_a ** 2)
# else:
#     print('정수를 입력하지 않았습니다.')

# try:
#     user_input_a = input('정수 입력> ')
#     print('원의 반지름:', number_input_a)
#     print('원의 둘레:', 2 * 3.14 * number_input_a)
#     print('원의 넓이:', 3.14 * number_input_a * number_input_a ** 2)
# except:
#     print('무언가 잘못되었습니다.')


# list_input_a = ['52', '73', '32', '스파이', '183']

# list_number = []

# for item in list_input_a:

#     try:
#         float(item)
#         list_number.append(item)
#     except:
#         pass

# print(f'{list_input_a} 내부에 있는 숫자는')
# print(f'{list_number} 입니다.')

# try:
#     number_input_a = int(input('정수 입력> '))
# except:    
#     print('정수를 입력하지 않았습니다.')
# else:
#     print('원의 반지름:', number_input_a)
#     print('원의 둘레:', 2 * 3.14 * number_input_a)
#     print('원의 넓이:', 3.14 * number_input_a ** 2)


# try:
#     number_input_a = int(input('정수 입력> '))
#     print('원의 반지름:', number_input_a)
#     print('원의 둘레', 2 * 3.14 * number_input_a)
#     print('원의 넓이', 3.14 * number_input_a ** 2)
# except:
#     print('정수를 입력하지 않았습니다.')
# else:
#     print('예외가 발생하지 않았습니다.')
# finally:
#     print('일단 프로그램이 어떻게든 끝났습니다.')


# try:
#     file = open('info.txt', 'w')
#     file.close()
# except Exception as e:
#     print(e)
# finally:
#     file.close()

# print('파일이 제대로 닫혔는지 확인하기')
# print('file.closed', file.closed)


# def test():
#     print('test()함수의 첫 줄입니다.')
#     try:
#         print('try 구문이 실행되었습니다.')
#         return
#         print('try 구문의 return 키워드 뒤입니다.')
#     except:
#         print('except 구문이 실행되었습니다.')
#     else:
#         print('else 구문이 실행되었습니다.')
#     finally:
#         print('finally 구문이 실행되었습니다.')
#     print('test() 함수의 마지막 줄입니다.')

# test()


# while True:
#     try:
#         print('try 구문이 실행되었습니다.')
#         break
#         print('try 구문의 break 키워드 뒤입니다.')  # 죽은 코드입니다.
#     except:
#         print('except 구문이 실행되었습니다.')
#     finally:
#         print('finally 구문이 실행되었습니다.')
#     print('while 반복문의 마지막 줄입니다.')
# print('프로그램이 종료되었습니다.')


# numbers = [52, 273, 32, 103, 90, 10, 275]

# print('# (1).요소 내부에 있는 값 찾기')
# print('- {}는 {} 위치에 있습니다.'format(52, numbers.index(52)))
# print()

# print('# (2) 요소 내부에 없는 값 찾기')
# number = 10000
# try:
#     print('- {}는 {} 위치에 있습니다.'.format(number, numbers.index(number)))
# except:
#     print('- 리스트 내부에 없는 값입니다.')
# print()

# print('--- 정상적으로 종료되었습니다. ---'

# list_number = [52, 273, 32, 72, 100]
# try:
#     number_input = int(input('점수 입력> '))
#     print(f'{number_input}번째 요소: {list_number[number_input]}')
#     예외.발생해주세요()
# except Exception as exception:
#     if exception is ValueError:
#         print('점수를 입력해 주세요!')
#     elif exception is IndexError:
#         print('리스트의 인덱스를 벗어났어요!')
#     else:
#         print('미리 파악하지 못한 예외가 발생했습니다.')
#         print(type(exception), exception)


# number = input('점수 입력> ')
# number = int(number)

# if number > 0:
#     raise NotImplementedError
# else:
#     raise NotImplementedError


# import math as m

# print(m.sin(1))
# print(m.cos(1))
# print(m.tan(1))
# print(m.floor(2.5))
# print(m.ceil(2.5))


# import random
# print(' random 모듈')


# # 0.0 ~ 1.0 사이의 float를 리턴한다.
# print('random():', random.random())
# # uniform(min, max) 지정한 범위 사이의 float를 리턴한다.
# print('uniform(10, 20)', random.uniform(10, 20))
# # randrange(): 지정한 범위의 int를 리턴한다.
# # randrange(max): 0부터 max사이의 값을 리턴한다.
# # randrange(min, max): min 부터 max 사이의 값ㅎ을 리턴한다.
# print('randrange(10)'. random.randrange(10))
# li = [1, 2, 3, 4, 5]
# # choice(list)리스트 내부에 있는 요소를 랜덤하게 선택합니다.
# print(f'choice/{li}:{random.choice(li)}')

# #shuffle(list): 리스트의 요소들을 랜덤하게 섞습니다.
# print(f'shuffle.{li}:{random.shuffle(li)}')
# print(li)
# #sample(list, k =<숫자>):리스트의 요소중에 k개를 뽑습니다.
# print(f'sample{li}:{random.samle(li, k=2)}')

# import sys
# print(sys.argv)

# print('---')

# print('getwindowsversion:()', sys.getwindowsversion())

# print('---')

# print('copyright:', sys.copyright)

# print('---')

# print('version:', sys.version)

# sys.exit()


# import os

# print('현재 운영체제:', os.name)
# print('현재 폴더:', os.getcwd())
# print('현재 폴더 내부의 요소:', os.listedir())

# os.mkdir('hello')
# os.rmdir('hello')

# with open('original.txt', 'w') as file:
#     file.write('hello')

# os.rename('original.txt', 'new.txt')

# os.remove('new.txt')

# os.system('dir')


# import datetime

# print('현재 시간 출력하기')
# now = datetime.datetime.now()

# print(now.year, '년')
# print(now.month, '월')
# print(now.day, '일')
# print(now.hour, '시')
# print(now.minute, '분')
# print(now.second, '초')

# print()

# print('시간을 포맷에 맞춰 출력하기')
# output_a = now.strftime('%Y.%m.%d %H:%M:%S')
# print(output_a)

# output_b = '{}년 {}월 {}일 {}시 {}분 {}초'.format(
#     now.year,
#     now.month,
#     now.day,
#     now.hour,
#     now.minute,
#     now.second
# )
# print(output_b)
# output_c = now.strftime('%Y{} %m{} %d{} %H{} %M{} %S{}')/format(*"년월일시분초")
# print(output_c)


# import datetime
# now = datetime.datetime.now()

# print('datetime.timedelta로 시간 더하기')

# after = now + datetime.timedelta(
#     weeks = 1,
#     days = 1,
#     hours = 1,
#     minutes = 1,
#     seconds = 1
# )
# print(now)
# print(after.strftime(('%Y{} %m{} %d{} %H{} %M{} %S{}')/format(*"년월일시분초")))
# print()

# print('now.replace()로 1년 더하기')

# ouput = now.replace(year = (now.year + 1))
# print(ouput.strftime('%Y{} %m{} %d{} %H{} %M{} %S{}')/format(*"년월일시분초"))


# import time

# print('지금부터 5초동안 정지합니다!!')

# time.sleep(5)

# print('프로그램을 종료합니다.')


from urllib import request

target = request.urlopen('https://google.com')

output = target.read()

print(output)
