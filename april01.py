'''
# 서식 지정자로 문자열 넣기
name = 'james'
sentence = 'I am %s.' %name
# %s(string)에 name이 들어감
print(sentence)

# 서식 지정자로 숫자 넣기
yr = int('13')
sentence = 'I am %d years old.' %yr
print(sentence)

# 서식 지정자로 소수점 표현하기
'%f' %2.3 # 기본값은 소수 6자리까지 표시
'%.3f' %2.3 # 소수점 3자리까지 표시

# %길이d
# %길이.자릿수f

#응용
s = 'Today is %d of %s.' %(1, 'April')
print(s)

# format 메소드 사용하기
# * 파이썬은 문자열 만들 때 서식 지정자 방식보다 더 간단한 문자열 포매팅을 제공
# '{인덱스}.format(값)
s = 'Hello, {0}'.format('world!')
print(s)
# 여러개
s = 'Today is {0} {1} {2}.'.format(1, 'April', 2022)
print(s)
# 숫자(인덱스) 생략하면 순서대로 값이 들어감
# 숫자가 아니라 이름 지정도 가능
s = 'Today is {day} {month} {year}.'.format(year=2022, month='April', day=1)
print(s)

# 문자열 만드는 간단한 방법
year = 2022
month = 'April'
day = 1
print(f'Today is {day} {month} {year}.')

# format메소드로 문자열 정렬
'{0:<10}'.format('python') #왼쪽 정렬
'{0:>10}'.format('python') #오른쪽 정렬

# 금액에서 천단위의 콤마 넣기
format(1493500, ',') #자동으로 넣어줌

path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
x = path.split('\\')
filename = x[-1]
print(filename)

# 문단에서 특정 단어만 추출
# 1
passage = input()
table = passage.maketrans({
    '.':'',
    ',':''
})
psg = passage.translate(table)
print(psg)
p = psg.split()
the = p.count('the')
print(the)
# 2
passage = input()
words = passage.split()
cnt = 0
for i in words:
    if i.strip(',.') == 'the':
        cnt += 1

print(cnt)

# 24.6 심사문제: 높은 가격순으로 출력하기
a = list(map(int, input().split(';')))
a.sort(reverse = True)
for price in a:
    print('{:>9,}'.format(price))

# 포매팅에서 콤마 삽입
#>>> '{0:,}'.format(1493500)
#'1,493,500'

# 딕셔너리 조작하기
x = {'a':10, 'b':20, 'c':30, 'd':40}
x.setdefault('e') #딕셔너리에 키-값 쌍 추가
print(x)
x.setdefault('f', 60)
print(x)

# 딕셔너리 키값 수정하기
x.update(e=50)
print(x)
x.update(g=70) # 키가 없으면 자동으로 추가하고 값까지 할당
print(x) # update(키=값)은 키가 문자열일 때만 가능, 키가 숫자라면 update({키:값})으로 수정

# setdefault는 추가만 가능하고 update는 수정도 가능

# 딕셔너리 키-값 쌍 삭제하기
x.pop('a')
print(x)
del x['b']
print(x)
x.popitem() # 마지막 키-값 쌍 삭제
print(x)
x.clear() # 모두 삭제
print(x)

x = {'a':10, 'b':20, 'c':30, 'd':40}
print(x.get('a')) # 키의 값 호출
print(x.items()) # 모든 키-값 쌍 가져오기
print(x.keys()) # 키 가져오기
print(x.values()) # 값 가져오기

# 리스트(or 튜플)로 딕셔너리 만들기
keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys)
print(x)

# 반복문으로 딕셔너리 키-값 쌍 모두 출력
x = {'a':10, 'b':20, 'c':30, 'd':40}
for k, v in x.items():
    print(k, v)

for k in x.keys():
    print(k)

for v in x.values():
    print(v)

# 중첩 딕셔너리: 딕셔너리 안에서 딕셔너리
terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069,
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
}
 
print(terrestrial_planet['Venus']['mean_radius'])    # 6051.8

# deepcopy는 깊은 복사로 중첩 딕셔너리를 완전히 복사

# 25.7 연슴문제: 평균 점수 구하기

maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
average = sum(maria.values()) / len(maria)
print(average)

# 25.8 심사문제: 딕셔너리에서 특정 값 삭제하기
keys = input().split()
values = map(int, input().split())
 
x = dict(zip(keys, values))

x.pop('delta')
x = {k:v for k,v in x.items() if v != 30}
print(x)

# 세트
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
# 세트의 요소는 순서가 없음(unordered), 인덱스가 부재
# set() 함수로 세트 생성 가능
a = set('apple')
print(a) # 중복 문자 출력 X

# 합집합
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a|b)
print(set.union(a,b))
# 교집합
print(a&b)
print(set.intersection(a,b))
# 차집합
print(a-b)
print(set.difference(a,b))
# 대칭차집합
print(a^b)
print(set.symmetric_difference(a,b))

# 세트 조작하기

a = {1, 2, 3, 4}
a.add(5) #세트에 추가
a.remove(3) #세트에서 삭제
a.discard(3) #세트에서 삭제, but 없어도 넘어감
a.pop() #임의 요소 삭제 ?? 처음거만 삭제되는디
print(a)

# 세트 표현식
a = {i for i in 'pineapple' if i not in 'apl'} # a,p,l 제외한 알파벳 출력

# 공배수 구하기
a = {i for i in range(1,101) if i % 3 == 0}
b = {i for i in range(1,101) if i % 5 == 0}

print(a & b)

# 공약수 구하기
x, y = map(int,input().split())
a = {i for i in range(1, x+1) if x % i == 0}
b = {i for i in range(1, y+1) if y % i == 0}
divisor = a & b

result = 0
if type(divisor) == set:
    result = sum(divisor)
 
print(result)
'''
# 파일 사용하기
file = open('hello.txt', 'w') # hello.txt 파일을 쓰기 모드로 열기
file.write('Hello, world!') # 파일에 문자열 저장
file.close()

file = open('hello.txt', 'r') # hello.txt 파일을 읽기 모드로 열기
s = file.read() # 파일에서 문자열 읽기
print(s)
file.close()

# 자동으로 파일 객체 닫기
with open('hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    s = file.read()                     # 파일에서 문자열 읽기
    print(s)                            # Hello, world!
