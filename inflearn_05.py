#21.06.05~06
#리스트 함수
a = [1, 2, 3, 4, 5]
a.append(-1)
print('append a', a) # 데이터를 추가할 때 호출하는 함수:appended
a.sort()
print('sorted a',a) # 오름차순으로 정렬하는 함수:sorted
b = [2, 1, 7, 4]
b.reverse()
print('reverse b', b) # 역순으로 데이터의 원소들을 배열시키는 함수:reverse
print('b - ', b.index(2), b[2]) # index(x)는 리스트 배열 안의 값x의 위치를 반환시키는 함수이다.
                                # 따라서 b.index(2)는 reverse 된 b의 원소2의 위치, 즉 3을 반환한다.
                                # however, b[y] returns value of y indexed number in list b.
                                # in this case, b[2] returns value 1.
print(a.index(1))
c = [3, 5, 8, 6, 10]
c.insert(2,15)        # m.insert(n,x) inserts value x in index number n. and so on.
print('insert c', c)
# del[]는 특정번호의 인덱스를 지우기는 용이하나 원소가 많을 시에는 번거롭다.
c.remove(15)
print('remove c',c) # remove 함수는 특정 원소를 지정해 삭제한다.
                    # del은 예약어, remove는 함수.
d = [1, 2, 3, 7, 8, 7]
d.remove(7)
print(d)            ## remove(n)에서 n이, 리스트 안에 복수 개가 있다면 어떻게 되는가?
e = [5, 5, 10, 15, 20]
print('e - ', e.pop()) # pop은 리스트 가장 오른쪽의 값을 꺼내온다.
print('pop e - ', e) # pop으로 꺼내진 값 없이 리스트 e 출력.
print('e.count(5) - ', e.count(5)) #count함수 안의 값이 몇 개가 리스트 안에 있는지 세아려 출력한다.
ex = [20, 25, 30]
e.extend(ex)
print('extend e - ', e) # extend 함수는 끝부분에 리스트 원소를 추가시킨다.
# 삭제 method로는 대표적으로 remove, pop, del이 있다.
