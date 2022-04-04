'''
# 35.5 연습문제: 날짜 클래스 만들기
class Date:
    @staticmethod
    def is_date_valid(date_string):
        year, month, day = map(int, date_string.split('-'))
        return month <= 12 and day <= 31

if Date.is_date_valid('2000-10-31'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')

# 35.6 심사문제 시간 클래스 만들기
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @classmethod
    def from_string(cls, time_string):
        hour, minute, second = map(int, time_string.split(':'))
        time = cls(hour, minute, second)
        return time
    
    @staticmethod
    def is_time_valid(time_string):
        hour, minute, second = map(int, time_string.split(':'))
        return hour<=24 and minute<=59 and second<=60


time_string = input()

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')

# 클래스 상속
class Person:
    def greeting(self):
        print('안녕하세요.')

class Student(Person):      # Person 클래스를 상속 받음
    def sudy(self):
        print('공부하기')

james = Student()
james.greeting()
james.study()
# 클래스 상속은 기반 클래스의 기능을 유지하면서 새로운 기능 추가

# 포함 관계, 속성에 인스턴스 넣어 관리 (has-a)
class Person:
    def greeting(self):
        print('안녕하세요.')

class PersonList:
    def __init__(self):
        self.person_list = []

    def append_person(self, person):
        self.person_list.append(person)

# seper()로 기반 클래스 초기화(기반 클래스의 __init__불러오기)
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요'

class Student(Person):
    def __init__(self):
        super().__init__()
        print('Student + __init__')
        self.school = '파이썬 코딩 도장'

james = Student()
print(james.school)
print(james.hello)
# 파생 클래스에서 __init__메소드 생략하면 기반 클래스의 __init__ 자동 호출
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
 
class Student(Person):
    pass
 
james = Student()
print(james.hello)

# 메소드 오버라이딩
# overriding은 무시하다, 우선하다라는 뜻. 기반 클래스 메소드 무시하고 새로운 메소드 생성
class Person:
    def greeting(self):
        print('안녕하세요.')
 
class Student(Person):
    def greeting(self):
        print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')
 
james = Student()
james.greeting()

class Person:
    def greeting(self):
        print('안녕하세요.')
 
class Student(Person):
    def greeting(self):
        print('저는 파이썬 코딩 도장 학생입니다.')
        super().greeting()    # 기반 클래스의 메서드 호출하여 중복을 줄임
        print('저는 파이썬 코딩 도장 학생입니다.')
 
james = Student()
james.greeting()

# 다중 상속

class Person:
    def greeting(self):
        print('안녕하세요.')

class University:
    def manage_credit(self):
        print('학점 관리')

class Undergraduate(Person, University):
    def study(self):
        print('공부하기')

james = Undergraduate()
james.greeting()
james.manage_credit()
james.study()

# 메소드 탐색 순서 확인
# 클래스.__mro__
print(Undergraduate.__mro__)
'''
# 추상 클래스는 인스턴스로 만들 때는 사용하지 않으며 오로지 상속에만 사용

#36.9 심사문제: 다중 상속 사용하기

class Animal:
    def eat(self):
        print('먹다')
 
class Wing:
    def flap(self):
        print('파닥거리다')

class Bird(Animal, Wing):
    def fly(self):
        print('날다')

b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird, Animal))
print(issubclass(Bird, Wing))