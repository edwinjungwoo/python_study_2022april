'''
lines = ['안녕하세요.\n', '파이썬\n', '김정우입니다.\n']
 
with open('hello.txt', 'w') as file:    # hello.txt 파일을 쓰기 모드(w)로 열기
    file.writelines(lines)

with open('hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    lines = file.readlines()
    print(lines)

# 한 줄씩 순차적으로 읽으려면
with open('hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    line = None    # 변수 line을 None으로 초기화
    while line != '':
        line = file.readline()
        print(line.strip('\n'))    # 파일에서 읽어온 문자열에서 \n 삭제하여 출력
'
# 피클링: 파이썬 객체를 파일에 저장하는 과정, 피클 파일은 파이썬 객체 자체를 파일로 저장한 것
import pickle
name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}

with open('james.p', 'wb') as file:    # james.p 파일을 바이너리 쓰기 모드로 열기
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)

# 언피클링
with open('james.p', 'rb') as file:    # james.p 파일을 바이너리 읽기 모드(rb)로 열기
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)

# 27.6 심사문제: 특정 문자가 들어있는 단어 찾기
with open('words.txt', 'r') as file:
    line = file.read()
a = (line.split(' '))
for i in a:
    i = (i.strip(',.'))
    if 'c' in i:
        print(i)

#회문판별
a = input()
is_palindrome = True
for i in range(len(a)//2):
    if a[i] != a[-1 -i]:
        is_palindrome = False
        break

print(is_palindrome)

# 간단
a = input()
print(a == a[::-1])
print(a == ''.join(reversed(a)))

# 284.
with open('words.txt', 'r') as file:
    word = file.read()
    word = word.split()
    
for i in word:
    if i == i[::-1]:
        print(i)

with open('words.txt', 'r') as file:
    word = file.read()                  # 전부 문자열로 반환
    print(word)

with open('words.txt', 'r') as file:
    word = file.readline()              # 첫줄만 반환
    print(word)

with open('words.txt', 'r') as file:
    word = file.readlines()             # 모든 줄 리스트로 반환
    print(word)


# 함수
def 함수이름():
    코드
# 함수 호출할 때, 반드시 함수를 먼저 만든 뒤 호출해야 함

def add(a, b):
    print(a + b)
add(10, 20)

def add(a, b):
    return a + b # 함수 중간에서 빠져나올 때 자주 사용

x = add(10, 20)
print(x)

# 값 여러 개 반환
def add_sub(a, b):
    return a + b, a - b

x = 10
y = 3
def mokrem(a, b):
    return a//b, a%b
mok, rem = mokrem(x, y)
print('몫: {0}, 나머지: {1}'.format(mok, rem))

# 29.4
x, y = map(int, input().split())

def calc (q,w):
    return q+w, q-w, q*w, q/w

a, s, m, d = calc(x, y)
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))

# 위치 인수와 리스트 언패킹
def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)

print_numbers(10, 20, 30)

# 언패킹: 함수(*리스트), 함수(*튜플)
x = [10, 20, 30]
print_numbers(*x) # 애스터리스크가 x를 풀어줌

# 가변 인수 함수 만들기
def print_numbers(*args): # arguments 매개변수, 관용적으로 args라고 씀
    for arg in args:
        print(arg)

# 키워드 인수: print()함수의 sep과 end처럼 위치가 달라도 똑같이 적용

def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

print(personal_info(age=30, address='서울시 용산구 이촌동', name='홍길동'))
'
# 딕셔너리 언패킹: **을 사용, 딕셔너리는 키-값 쌍 형태이기 때문
def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')

x = {'name':'김정우', 'age':25, 'address':'서울시 강남구 도곡2동', 'grade':4}

print(personal_info(**x))

korean, english, mathematics, science = 100, 86, 81, 91

def get_max_score(*args):
    return max(args)

max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수:', max_score)
 
max_score = get_max_score(english, science)
print('높은 점수:', max_score)

# 30.7
korean, english, mathematics, science = map(int, input().split())

def get_min_max_score(*args):
    return min(args), max(args)
def get_average(**kwargs):
    return sum(kwargs.values())/len(kwargs)


min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))
 
min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))

# 재귀호출
def hello(count):
    if count == 0:    # 종료 조건을 만듦. count가 0이면 다시 hello 함수를 호출하지 않고 끝냄
        return
    
    print('Hello, world!', count)
    
    count -= 1      # count를 1 감소시킨 뒤
    hello(count)    # 다시 hello에 넣음
 
hello(5)    # hello 함수 호출

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
'''
