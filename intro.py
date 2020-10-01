a_String = 'like this'
a_number = 3
a_float = 3.12
a_boolean = True
a_none = None
#'not exist' type, nothing

print(type(a_none))

#list는 변경 가능한 sequence
days = ["Mon", "Tue", "Wed", "Thur", "Fri"]
print(days)
print(type(days))
print("Mon" in days)
#Mon이 리스트 days에 들어 있는지

print(days[3])
#java에서와 마찬가지로 배열 인덱스는 0부터

print(len(days))
#length

#데이터 추가
days.append("Sat")

#데이터 순서 거꾸로
days.reverse()
print(days)

#tuple, 수정 불가능한 배열
dayss = ("Mon", "Tue", "Wed", "Thu", "Fri")
print(type(dayss))

#dictionary: list, tuple 다 저장 가능
nico = {
"name" : "Nico",
"age" : 29,
"Korean" : False,
"fav_food" : ["Kimchi", "Sashimi"]
}

#dictionary 특정 요소 출력
print(nico["name"])

#dictionary 요소 추가
nico["foreign"] = True
print(nico)

#built-in functions: import없이 쓸 수 있는
#define function: 함수 정의하기
def say_hello():
  print("hello")
  #파이선은 {}안쓰고 들여쓰기(tab)로 함수 구분
say_hello()
#()는 절대 잊지 않는다. 

def func_hello(who):
  print("hello", who)

who = "JY"
func_hello("podo")

def plus(a, b):
  if type(b) is str or type(b) is int:
    return None
  else:
    print(a + b)
print(plus(3, 4))

def minus(a, b=3): #default값 설정 가능
  print(a - b)
minus(3, 2)

#function은 결과에 대해 신경써야 한다.
def sum(a, b): 
  return a + b
print(plus(2, 3), sum(2, 3))
#안에서 print명령을 쓴 함수는 None으로 출력
#return은 함수를 종료시킨다. return 뒤의 내용은 X

#keyword argument - 인자의 위치 상관x
print(sum(b=4, a=2))

def say_hi(name, age):
  return f"Hello {name} you are {age} years old"

hi = say_hi("JY", "12")
print(hi)

#7 functions 만들기
#plus, minus, times, division, negation, power, reminder
#calculator 만들기 + 예외 처리
#built-in functions 사용해서 형변환

#조건문 조건
# a and b, a or b, not a, ...
def age_check(age):
  print(f"you are {age}")
  if age < 18:
    print("not allowed")
  elif age == 18:
    print("babe")
  else:
    print("welcome!")
age_check(18)

#Loop
weekdays = {"Mon", "Tue", "Wed", "Thu", "Fri"}
for day in weekdays:
  if day == "Wed":
    break
  else:
    print(day)

for letter in "jiyeon":
  print(letter)

#module
#import를 통해 모듈을 사용한다.
#datatypes, io, socket, 등등등 많음
#쓸 것만 import하자
#import math
from math import ceil, fsum
print(ceil(1.2))
#print(math.fabs(-1.2))
print(fsum([1, 2, 3, 4, 5]))