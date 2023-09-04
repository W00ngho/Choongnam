
# from urllib import request
# from bs4 import BeautifulSoup
# target = request.urlopen('https://www.kma.go.kr/weather/forescast/mid-term-rss3.jsp?stnId=108')
# soup = BeautifulSoup(target, 'html.parser')

# for location in soup.select('location'):
#     print('도시:', location.select_one('city').string)
#     print('날씨:', location.select_one('wf').string)
#     print('최저기온:', location.select_one('tmn').string)
#     print('최고기온:', location.select_one('tmx').string)
#     print()


# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello():
#     target = request.urlopen('https://www.kma.go.kr/weather/forescast/mid-term-rss3.jsp?stnId=108')
#     soup = BeautifulSoup(target, 'html.parser')
#     output = ""
#     for location in soup.select('location'):
#         output += '<h3>{}</h3>'.format(location.select_one('city').string)
#         output += '날씨{}<br/>'.format(location.select_one('wf').string)
#         output += '최저/최고 기온: {}/{}'\
#         .format(
#             location.select_one('tmn').string,
#             location.select_one('tmx').string
#         )
#         output += '<hr/>'
#     return output


# PI = 3.141592

# def number_input():
#     output = input('숫자 입력> ')
#     return float(output)

# def get_circumference(radius):
#     return 2 * PI * radius

# def get_circle_area(radius):
#     return PI * radius * radius


# class Student:
#     def __init__(self, name, korean, math, english, science):
#         self.name = name
#         self.korean = korean
#         self.math = math
#         self.english = english
#         self.science = science
#     def get_sum(self):
#         return self.korean + self.math + self.english + self.science

#     def get_average(self):
#         return self.get_sum() / 4
    
#     def to_string(self):
#         return "{}\t{}\t{}".format(
#             self.name,
#             self.get_sum(),
#             self.get_average()
#         )
# students = [
#     Student('윤인성', 87, 98, 88, 95),
#     Student('연하진', 92, 98, 96, 98),
#     Student('구지연', 76, 96, 94, 90),
#     Student('나선주', 98, 92, 96, 92),
#     Student('윤아린', 95, 98, 98, 98),
#     Student('윤명월', 64, 88, 92, 92)

# ]
# for student in students:
#     print(student.to_string())

# students[0].name
# students[0].korean
# students[0].math
# students[0].english
# students[0].science


# class Human:
#     def __init__(self) -> None:
#         pass
# class Student(Human):
#     def __init__(self) -> None:
#         pass

# student = Student()

# print('isinstace(student, Human):', isinstance(student, Human))
# print('type(student) == Human:', type(student) == Human)


# class Student:
#     def study(self):
#         print('공부를 합니다.')

# class Teacher:
#     def teach(self):
#         print('학생을 가르칩니다.')

# classroom = [Student(), Student(), Teacher(), Student(), Student()]

# for person in classroom:
#     if isinstance(person, Student):
#         person.study()
#     elif isinstance(person, Teacher):
#         person.teach()


# class Student:
#     def __init__(self, name, korean, math, english, science):
#         self.name = name
#         self.korean = korean
#         self.math = math
#         self.english = english
#         self.science = science
#     def get_sum(self):
#         return self.korean + self.math + self.english + self.science

#     def get_average(self):
#         return self.get_sum() / 4
    
#     def __str__(self):
#         return "{}\t{}\t{}".format(
#             self.name,
#             self.get_sum(),
#             self.get_average()
#         )

# students = [
#     Student('윤인성', 87, 98, 88, 95),
#     Student('연하진', 92, 98, 96, 98),
#     Student('구지연', 76, 96, 94, 90),
#     Student('나선주', 98, 92, 96, 92),
#     Student('윤아린', 95, 98, 98, 98),
#     Student('윤명월', 64, 88, 92, 92)

# ]

# print('이름', '총점', '평균', sep='\t')
# for student in students:
#     print(str(student))


class Student:
    count = 0
    students = []

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count +=1
    classmethod
    def print(cls):
        print('----- 학생 목록 -----')
        print('이름\t총점\t평균')
        for student in cls.students:
            print(str(student))
        print('----- ----- -----')

        
        students = [
    Student('윤인성', 87, 98, 88, 95),
    Student('연하진', 92, 98, 96, 98),
    Student('나선주', 98, 92, 96, 92),
    Student('윤아린', 95, 98, 98, 98),
    Student('윤명월', 64, 88, 92, 92)
]


print()
print(f'현재 생성된 총 학생 수는 {Student.count} 명 입니다.')










