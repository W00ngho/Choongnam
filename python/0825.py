
# marks = [90, 25, 67, 45, 80]

# number = 0
# 5
# for mark in marks:
#     number = number + 1
#     if mark <= 60:
#         continue
#     print(f'{number}번 학생은 합격입니다.')
    

# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f"{i} * {j} = {i * j}  ", end = '')
#     print(' ')


# for dan in range(2, 5+1):
#   for i in range(1, 9+1):
#     print("{} X {} = {}".format(dan, i, dan*i))
#   print("----------")


# a = [1, 2, 3, 4]
# result = []

# for num in a:
#     result.append(num * 3)
# print(result)
# a = [1, 2, 3, 4]
# result = [num * 3 for num in a]

# i = 0
# while True:
#     i += 1
#     if i > 5: break
#     print("*" * 1)

# A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# total = 0
# for score in A:
#     total += score

# average = total / len (A)
# print(average)
# def sum_mul(choice, *args):
#     if choice == "sum":

#         result = 0
#         for i in args:
#             result = result + i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result = result * i
#     return result
# result = sum_mul('sum', 1, 2, 3, 4, 5)
# print(result)
# result = sum_mul('mul', 1, 2, 3, 4, 5)
# print(result)


# import turtle as t
# t.shape('turtle')
# t.speed(1)
# t.pensize(5)
# t.shapesize(5)
# t.color('green')
# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(120)


# a = []
# for i in (range(10, 110, 10)):
#     a.append(i)

# a.reverse()
# print(a)
# for i in range(1, 11):
#     a.append(i * 10)

# a.reverse()
# print(a)

# import turtle as t

# t.shape('turtle')
# angle = 89
# t.bgcolor('black')
# t.color('green')
# t.spped(1)
# for x in range(200):
#     t.forwrad(x)
#     t.left(angle)
# t.hideturtle()


# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(120)

# import turtle as t
# n = 5
# t.color('purple')
# t.begin_fill()

# for x in range (n):
#     t.forwrad(50)
#     t.left(360/n)

# t.end_fill()
# t.hideturtle

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print('1!', factorial(1))
# print('2!', factorial(2))
# print('3!', factorial(3))
# print('4!', factorial(4))


# def fibonacci(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1 
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# dictionary = {
#     1: 1,
#     2: 1
# }
# def fibonacci(n):
#     if n in dictionary:
#         return dictionary[n]
#     else:
#         output = fibonacci(n - 1) + fibonacci(n - 2)
#         dictionary[n] = output
#         return output
    
# print(fibonacci(35))

# def flatten(data):
#     result = []
#     if type(data) is list:
#         for el in data:
#             result += flatten(el)
#     else:
#         result += [data]
#     return result

# example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
# print(example)
# print(flatten(example))

# a, b = 10, 20

# print(a, b)

# a, b = b, a
# print(a, b)

# a, b = 97, 40
# print(divmod(a, b))

# x, y = divmod(a, b)
# print(x)
# print(y)

# def power(item):
#     return item * item

# def under_3(item):
#     return item < 3

# list_input_a = [1, 2, 3, 4, 5]

# output_a = map(power, list_input_a)
# print('map() 함수의 실행결과')
# print(output_a)
# print(list(output_a))
# print()

# output_b = filter(under_3, list_input_a)
# print(output_b)
# print(list(output_b))

# power = lambda x: x * x
# under_3 = lambda x: x < 3 

# list_input_a = [1, 2, 3, 4, 5]

# output_a = map(power, list_input_a)
# print("map() 함수의 실행결과")
# print(output_a)
# print(list(output_a))
# print()

# output_b = filter(lambda x: x < 3, list_input_a)
# print(output_b)
# print(list(output_b))








