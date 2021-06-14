#21.06.07
#튜플 자료형
#튜플(순서o, 중복o, 수정x, 삭제x) 한번 선언되면 값이 불변이다.
a = ()
b = (1,) # 원소가 하나일 때는 원소 뒤에 콤마를 삽입해야 한다.
         # b = (1)은 type 출력 시 int로 출력된다.
print(type(a), type(b))
print()
c = (10, 20, 25, ('apple', 'baseball', 'case'))
print('e - ', list(c[-1][0])) #튜플 역시 리스트로 형변환이 가능. 이때 불변 특성은 사라진다.
# c[0] = 29 입력시, 'tuple' object does not support item assignment로 변경이 되지 않는다.
print()
print(c[:3])
print(c[1:4])
print(c[-1][0:2]) ##튜플은 리스트와 같은 "시퀀스 성질"(?)을 갖고 있기에, 슬라이싱이 적용됨을 확인.
#튜플에서도 같은 자료형끼리 +, * 연산이 가능하다.
#튜플 함수
print()
d = (2, 4, 7, 7)
print(d.index(7)) ## 출력값은 2.
print((d.count(7)))
#팩킹
t = ('foot', 'head', 'hand', 'jaw')
print(t.index('foot'))
print(t[0])
#언팩킹
print()
(x1, x2, x3, x4) = t #괄호가 없더라도 언팩킹 성립. 관습상 '언팩킹 했음'을 나타내기 위해 괄호를 씌운다고 한다.
print(type(x1),type(x2),type(x3),type(x4))
print(x2, x1, x3, x4)
#팩킹&언팩킹
print()
t2 = 1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4, = t3
print(t2)
print(t3)
print(x1, x2, x3)
print(x4)
