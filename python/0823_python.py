# dictionary = {
#     "name":"7D 건조 망고",
#     "type":"당절임",
#     "ingredient":["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
#     "origin":"필리핀"
# }

# print("name", dictionary["name"])
# print("type", dictionary["type"])
# print("ingredient:", dictionary["ingredient"])
# print("origin", dictionary["origin"])
# print()

# dictionary["name"] = "8D 건조 망고"
# print("name:", dictionary["name"])

# # import random



# 로또 번호 뽑기 6개, 청소 당번 번호 뽑기

# numbers = []
# while len(numbers) < 7:
#     number = random.randint(1, 10)
#     if number not in numbers:
#         numbers.append(number)
# print(number)

# dictionary = {
#     "name":"7D 건조 망고",
#     "type":"당절임",
#     "ingredient":["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
#     "origin":"필리핀"
# }

# key = input("> 접근하고자 하는 키:")

# if key in dictionary:
#     print(Dictionary[key])
# else:
#     print("존재하지 않는 키에 접근하고 있습니다.")


# dictionary = {
#     "name":"7D 건조 망고",
#     "type":"당절임",
#     "ingredient":["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
#     "origin":"필리핀"
# }

# value = dictionary.get("존재하지 않는 키")
# print("값:", value)

# if value == None:
#     print("존재하지 않는 키에 접근했었습니다.")


# dictionary = {
#     "name":"7D 건조 망고",
#     "type":"당절임",
#     "ingredient":["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
#     "origin":"필리핀"
# }

# for key in dictionary:
#     print(key, ":", dictionary[key])

# character = {
#     "name" : "기사",
#     "level" : 12,
#     "item" : {
#         "sword" : "불꽃의 검",
#         "aromr" : "풀 플레이트"
#     },
#     "skill" : ["베기", "세게 베기", "아주 세게 베기"]
# }

# for key in character:
#     if type(charcter[key]) is dict:
#         dicdic = character[key]
#         for k in dicdic:
#             print(k , ":", dicdic[k])
#     elif type (character[key]) is list:
#         dicdic = character[key]
#         for k in diclis:
#             print(key, ":", k)
#     else:
#         print(key, ":", character[key])


# array = [273, 32, 103, 57, 52]

# for i in range(len(array)):
#     print(f"{i}번째 반복 : {array[i]}")


# for i in range(4, 0, -1):
#     print(f"현재 반복 변수 {i}")


# key_list = ["name", "hp", "mp", "level"]
# valu_list = ["기사", 200, 30, 5]
# character = {}


# numbers = [1, 2, 3, 4, 5, 6]

# r_rum = reversed(numbers)
# print(r_rum)

# print(next(r_rum))
# print(next(r_rum))
# print(next(r_rum))
# print(next(r_rum))
# print(next(r_rum))
# print(next(r_rum))



# a = input("입력 ")
# b = input("입력 ")

# na = int(a)
# nb = int(b)

# print( na + nb )
# print( na - nb )
# print( na * nb )
# print( na / nb )
# print( na % nb )


# num_a = input("1 입력")
# num_b = input("2 입력")

# if num_a > 0 and num_b > 0:
#     print(num_a + num_b)
#     print(num_a - num_b)
#     print(num_a * num_b)
#     print(num_a / num_b)
#     print(num_a % num_b)
# else:
#     print("error")



pocket = ['paper', 'cellphone', 'money']
del pocket[2]
print(pocket)
if 'money' in pocket:
    print("택시 타")
else:
    print("걸어가")







