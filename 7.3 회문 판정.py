a = input("문자열 입력: ")

b = []
for i in a:
    b.append(i)

c = ''
for x in b:
    c = x + c


if a == c:
    print("이 문장은 회문입니다.")
