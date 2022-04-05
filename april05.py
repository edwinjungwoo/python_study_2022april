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

import math

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point2D(x=30, y=20)
p2 = Point2D(x=60, y=50)

print('p1: {}, {}'.format(p1.x, p1.y))
print('p2: {}, {}'.format(p2.x, p2.y))

a = p2.x - p1.x
b = p2.y - p1.y

c = math.sqrt(a**2 + b**2)
print(c)

# abs() 절댓값

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

rect = Rectangle(x1=20, y1=20, x2=40, y2=30)

width = abs(rect.x2 - rect.x1)
height = abs(rect.y2 - rect.y1)
area = width * height
print(area)

import math

class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

length = 0.0
p = [Point2D(), Point2D(), Point2D(), Point2D()]
p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())

for i in range(len(p) - 1):
    a = p[i+1].x - p[i].x
    b = p[i+1].y - p[i].y
    c = math.sqrt(a**2 + b**2)
    length += c

print(length)

# 예외 처리
# try except 사용하기
try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
    print(y)
except:    # 예외가 발생했을 때 실행됨
    print('예외가 발생했습니다.')

y = [10, 20, 30]
 
try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index] / x)
except ZeroDivisionError as e:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.', e)
except IndexError as e:           # 범위를 벗어난 인덱스에 접근하여 에러가 발생했을 때 실행됨
    print('잘못된 인덱스입니다.', e)

# try except else finally
try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드
else:
    예외가 발생하지 않았을 때 실행할 코드
finally:
    예외 발생 여부와 상관없이 항상 실행할 코드

# if raise로 예외 지정하고 에러 발생 가능
try:
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:                                 # x가 3의 배수가 아니면
        raise Exception('3의 배수가 아닙니다.')    # 예외를 발생시킴
    print(x)
except Exception as e:                             # 예외가 발생했을 때 실행됨
    print('예외가 발생했습니다.', e)

# 예외 만들기
# 'Exception'을 상속받아서 새로운 클래스를 만들면 됨

class NotPalindromeError(Exception):
    def __init__(self):
        super().__init__('회문이 아닙니다.')

def palindrome(word):
    if word != word[::-1]:
        raise NotPalindromeError
    print(word)

try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)

# 이터레이터는 값을 차례로 꺼낼 수 있는 객체
class Counter:
    def __init__(self, stop):
        self.current = 0
        self. stop = stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.stop:
            r = self.current
            self.current += 1
            return r
        else:
            raise StopIteration

for i in Counter(3):
    print(i, end = ' ')

# map도 이터레이터

# 제너레이터 yield
# yield는 현재 함수를 잠시 중단하고 함수 바깥 코드 실행
def number_generator():
    yield 0    # 0을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보
    yield 1    # 1을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보
    yield 2    # 2를 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보
 
g = number_generator()
 
a = next(g)    # yield를 사용하여 함수 바깥으로 전달한 값은 next의 반환값으로 나옴
print(a)       # 0
 
b = next(g)
print(b)       # 1
 
c = next(g)
print(c)       # 2
'''
# 코루틴 (coopeerative routine)
# 코루틴은 진입점이 여러개
def number_coroutine():
    while True:        # 코루틴을 계속 유지하기 위해 무한 루프 사용
        x = (yield)    # 코루틴 바깥에서 값을 받아옴, yield를 괄호로 묶어야 함
        print(x)
 
co = number_coroutine()
next(co)      # 코루틴 안의 yield까지 코드 실행(최초 실행)
 
co.send(1)    # 코루틴에 숫자 1을 보냄
co.send(2)    # 코루틴에 숫자 2을 보냄
co.send(3)    # 코루틴에 숫자 3을 보냄
