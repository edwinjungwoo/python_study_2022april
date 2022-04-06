'''# decorator
# 함수를 수정하지 않은 상태에서 추가 기능 구현할 때 사용
def trace(func):                             # 호출할 함수를 매개변수로 받음
    def wrapper():                           # 호출할 함수를 감싸는 함수
        print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
        func()                               # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper                           # wrapper 함수 반환
 
def hello():
    print('hello')
 
def world():
    print('world')
 
trace_hello = trace(hello)    # 데코레이터에 호출할 함수를 넣음
trace_hello()                 # 반환된 함수를 호출
trace_world = trace(world)    # 데코레이터에 호출할 함수를 넣음
trace_world()                 # 반환된 함수를 호출

def trace(func):                             # 호출할 함수를 매개변수로 받음
    def wrapper():
        print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
        func()                               # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper                           # wrapper 함수 반환
 
@trace    # @데코레이터
def hello():
    print('hello')
 
@trace    # @데코레이터
def world():
    print('world')
 
hello()    # 함수를 그대로 호출
world()    # 함수를 그대로 호출

def trace(func):          # 호출할 함수를 매개변수로 받음
    def wrapper(a, b):    # 호출할 함수 add(a, b)의 매개변수와 똑같이 지정
        r = func(a, b)    # func에 매개변수 a, b를 넣어서 호출하고 반환값을 변수에 저장
        print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r))  # 매개변수와 반환값 출력
        return r          # func의 반환값을 반환
    return wrapper        # wrapper 함수 반환
 
@trace              # @데코레이터
def add(a, b):      # 매개변수는 두 개
    return a + b    # 매개변수 두 개를 더해서 반환
 
print(add(10, 20))

# 매개변수 있는 데코레이터
def is_multiple(x):              # 데코레이터가 사용할 매개변수를 지정
    def real_decorator(func):    # 호출할 함수를 매개변수로 받음
        def wrapper(a, b):       # 호출할 함수의 매개변수와 똑같이 지정
            r = func(a, b)       # func를 호출하고 반환값을 변수에 저장
            if r % x == 0:       # func의 반환값이 x의 배수인지 확인
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, x))
            return r             # func의 반환값을 반환
        return wrapper           # wrapper 함수 반환
    return real_decorator        # real_decorator 함수 반환
 
@is_multiple(3)     # @데코레이터(인수)
def add(a, b):
    return a + b
 
print(add(10, 20))
print(add(2, 5))

# 정규표현식(regular expression) 사용하기
import re

print(re.match('Hello', 'Hello,world!')) # 매치 객체 반환

# 문자열 앞에 ^를 붙이면 문자열이 맨 앞에 오는지 판단
# 문자열 뒤에 $를 붙이면 문자열이 맨 뒤에 오는지 판단

re.search('^Hello', 'Hello, world!')
re.search('world!$', 'Hello, world!')

# | 는 특정 문자열에서 지정된 문자열이 하나라도 포함되는지 판단

# 문자열이 숫자인지 판단, 패턴 자리에 [ ] 안에 숫자 범위를 넣고 * 또는 *를 붙임

print(re.match('[0-9]*', '1234'))
re.match('[0-9]+', '1234')
re.match('[0-9]+', 'abcd')

# 문자나 숫자가 한 개만 있는 판단할 때 ?와 . 활용
# 문자 개수 판단할 때는 {개수}
print(re.match('h{3}', 'hhhello'))

print(re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-0001-0001')) # 휴대전화 형식

# 숫자와 영문 문자 조합, 한글 조합
# 0-9 \d
# a-z
# A-Z
# 가-힣

#반대로 포함이 아닌지 획인하려면 [^A-Z] 안 맨 앞에 ^ 붙임, ^[A-Z]과 헷갈린 주위

# 정규표현식 그룹으로 묶기
import re
m = re.match('([0-9]+) ([0-9]+)', '10 295')
print(m.group(1))
print(m.group(2))
print(m.group())

# (?P<이름>정규표현식)

# findall
print(re.findall('[0-9]+', '1 2 Fizz 4 Buzz Fizz 7 8'))

# 문자열 바꾸기
re.sub('apple|orange', 'fruit', 'apple box orange tree')
re.sub('([a-z]+) ([0-9]+)', '\\2 \\1 \\2 \\1', 'hello 1234')

import re
 
p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
emails = ['python@mail.example.com', 'python+kr@example.com',              # 올바른 형식
          'python-dojang@example.co.kr', 'python_10@example.info',         # 올바른 형식
          'python.dojang@e-xample.com',                                    # 올바른 형식
          '@example.com', 'python@example', 'python@example-com']          # 잘못된 형식
 
for email in emails:
    print(p.match(email) != None, end=' ')

# import로 모듈 가져오기
import math
print(math.pi)
print(math.sqrt(4.0))

import math as m
print(m.sqrt(2.0))

# from import로 원하는 변수만 호출
from math import pi
print(pi)
from math import sqrt as s
print(s(4.0))
del math

from math import ceil, floor

x = 1.5

print(ceil(x), floor(x))

from math import pi

r = float(input())
print(pi*(r**2))

# 모듈

#if __name__ == '__main__':
    # 현재 스크립트 파일이 실행되는 상태 파악
def add(a, b):
    return a + b
 
def mul(a, b):
    return a * b
 
if __name__ == '__main__':    # 프로그램의 시작점일 때만 아래 코드 실행
    print(add(10, 20))
    print(mul(10, 20))
'''
A=[1,2,3,4,5,6,7,8,9,10]
B=set([11,11,12,13,14,15,16,17,18,19,20])
C=list(zip(A,B))
print(C)