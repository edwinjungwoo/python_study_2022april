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
'''
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
