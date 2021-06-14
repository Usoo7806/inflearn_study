# 21.05.31
# 리스트 순서, 중복, 수정, 삭제가 가능한 자료형이다.
a = []
b = list()
c = [10, 20, 25, 40] #len
d = [20, 30, 'alpha', 'beta']
e = [7, 14, 21, ['normal', 6, 9]]
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# 인덱싱 : 내가 원하는 데이터형을 꺼내오는 과정.
print('>>>>>>>>>>>>>>>>')
print('d - ', type(d), d)
print('d - ', d[3]) # beta 출력. 인덱스는 0번부터 시작함.
print('c - ', c[-2]) # 인덱싱을 음수로 할 시에는 오른쪽부터 -1, -2, -3... 으로 숫자가 부여된다.
print('e - ', type(e[3][0])) # 3번 리스트 안의 0번 리스트를 출력한다.
print('e - ', list(e[3][0])) # 형변환을 하면 str을 list 형태로 일일이 분해한다.