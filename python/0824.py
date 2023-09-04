# def print_3_times():
#     print('안녕하세요')
#     print('안녕하세요')
#     print('안녕하세요')

#     print_3_times()

# def print_n_times(value, n):
#     for i in range(n):
#         print(value)
    

# # print_n_times('안녕하세요', 5)


# def print_n_times(n, *values):
#     for i in range(n):
#         for value in values:
#             print(value)

#         print()

# print_n_times(3, '안녕하세요', '즐거운', '파이썬 프로그래밍')

# def print_n_times(value, n=2):
#     for i in range(n):
#         print(value)

# print_n_times('안녕하세요')

# def print_n_times(*values, n = 2):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()

# print_n_times('안녕하세요', '즐거운', n=3)


# def return_test():
#     return 200

# value = return_test()
# print(value)


# def sum_all(start, end, step=1):
#     output = 0
#     for i in range(start, end + 1):
#         output += i
#     return output

# output = sum_all(0, 100, 10)
# print(f' 0 to 100 {output}')
# print(f' 0 to 100 {sum_all(end=100)}')
# print(f' 0 to 100 {sum_all(end=100, step=1)}')


# def mul(*values):
#     output = 1
#     for v in values:
#         output *= v
#     return output
# print(mul(5, 7, 9, 10))

# with open('basic.txt', 'w') as file:
#     contents = file.read()

# import random

# hanguls = list('가나다라마바사아자차카타파하')

# with open('info.txt', 'w') as file:
#     for i in range(1000):
#         name = random.choice(hanguls) + random.choice(hanguls)
#         weight = random.randrange(40, 100)
#         height = random.randrange(140, 200)
        
#         file.write(f'{name}, {weight}, {height}')

# with open('info.txt', 'r') as file:
#     for line in file:
#         (name, weight, height) = line.strip().split(', ')
#         if (not name) or (not weight) or (not height):
#             continue
#     bmi = int(weight) / ((int(height)/100)**2)
#     result = ""

#     if 25 <= bmi:
#         result = '과체중'
#     elif 18.5 <= bmi:
#         result = '정상체중'
#     else:
#         result = '저체중'

#     print('\n'.join([
#         '이름: {}',
#         '몸무게: {}',
#         '키: {}',
#         'BMI: {}',
#         '결과: {}'
#     ]).format(name, weight, height, bmi, result))
#     print()

                       
# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit + 1
#     print('나무를 %d번 찍었습니다.' % treeHit)
#     if treeHit == 10:
#         print('나무 넘어갑니다.')


# number = 10
# while number !=4:
#     print('prompt')
#     number = int(input())

# i = 10
# while i > 0:
#     print('{}번째 반복입니다.'.format(i))
#     i -= 1

# i = 0
# while i < 101:
#     print(format(i))
#     i += 2



# x = int(input())

# if x % 2 == 0:
#     print('짝수')
# else:
#     print('홀수')

# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i)



# output = ""
# for i in range(1, 10):
#     for j in range(0, i):
#         output +="*"
#     output += "\n"

# print(output)

output = ""
for i in range(1, 15):
    for j in range(14, i, -1):
        output += " "
    for k in range(0, 2 * i -1):
        output += '*'
    output += "\n"

print(output)

































