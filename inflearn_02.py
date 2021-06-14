#   21.05.30
# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리

print('e1', 12+3 > 4+5)
print('한글')
print()
score = 75
if score >= 90 :
    print('Grade: A')
elif score >= 80 :
    print('Grade: B')
elif score >= 70 :
    print('Grade: C')
else : print('You are lost.')
print()
grade = 'A'
total = 85
if grade == 'A':
    if total >= 90 :
        print('장학금 100%')
    elif total >= 80 :
        print('장학금 50%')
    else : print('장학금 30%')
else : print('장학금 0%')

