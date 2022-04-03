'''
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

n = int(input())
print(fib(n))

# 람다 표현식: lambda에 매개변수 지정하고 :(콜론) 뒤에 반환값으로 사용할 식 지정

plus_ten = lambda x: x + 10 # 람다 자체는 익명변수이기 때문에 이름을 지정해야
print(plus_ten(1))

print(list(map(plus_ten, [1,2,3])))
print(list(map(lambda x: x + 10, [1,2,3])))

a = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x: str(x) if x%3 == 0 else x, a)))
# 람다 표현식 안에서 조건부 표현식 if, else 사용시 콜론 붙이지 않음
# if를 사용했다면 반드시 else 사용
# 람다 표현식 안에서는 elif 사용 불가 (식1 if 조건식1 else 식2 if 조건식2 else 식3...)

def f(x):
    if x == 1:
        return str(x)
    elif x == 2:
         return float(x)
    else:
        return x+10
print(list(map(f,a)))
# map은 리스트 등 반복 가능 객체를 여러 개 넣을 수도 있음
a = [1,2,3,4,5]
b = [2,4,6,8,10]
print(list(map(lambda x, y: x* y, a, b)))
# filter함수는 반복 가능 객체에서 특정 조건에 맞는 요소만 가져옴

def f(x):
    return x > 5 and  x < 10

a = [8,3,2,10,15,7,1,9,0,11]
print(list(filter(f,a)))

print(list(filter(lambda x: x>5 and x<10,a)))


# refuce함수는 반복 가능 객체 각 요소를 지정된 함수로 처리한 뒤 이전 결과와 누적해 반환
def f(x,y):
     return x+y

a = [1,2,3,4,5]
from functools import reduce
print(reduce(f,a))
print(reduce(lambda x,y: x+y,a))

files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']
print(filter(lambda x: x.find('.jpg') != -1 or x.find('.png') != -1, files))

# 32.5 파일 이름을 한꺼번에 바꾸기
files = input().split()

print(list(map(lambda x: x.split('.')[0].zfill(3) + '.' + x.split('.')[1], files))) #zfill()사용

list(map(lambda x: '{0:03d}.{1}'.format(int(x.split('.')[0]),x.split('.')[1]) ,files)) #포매팅

# 클로저 사용하기
# 전역번수와 지역변수

x = 10          # 전역 변수
def foo():
    global x    # 전역 변수 x를 사용하겠다고 설정 
    x = 20      # x는 전역 변수
    print(x)    # 전역 변수 출력

foo()
print(x)

# 함수 안에 함수
def print_hello():
    hello = 'Hello, world!'
    def print_message():
        print(hello)
    print_message()
 
print_hello()

def A():
    x = 10      # A의 지역변수 x
    def B():
         x = 20 # x에 20 할당, B의 지역변수 x를 새로 만든 것

    B()
    print(x)    # A의 지역변수 x 출력

A() # 10이 출력
'''
#-------------------------------------------------------------------
def A():
    x = 10        # A의 지역 변수 x
    def B():
        nonlocal x    # 현재 함수의 바깥쪽에 있는 지역 변수 사용
        x = 20        # A의 지역 변수 x에 20 할당
 
    B()
    print(x)      # A의 지역 변수 x 출력
 
A()

# 전역 변수는 코드가 복잡해졌을 때 변수의 값을 어디서 바꾸는지 알기 힘들기 때문에 가급적 사용하지 않는 것을 권

