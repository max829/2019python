
cont = dict()


while 1:

    name = input("(입력모드)이름 입력: ")
    num = input("(입력모드)전화번호 입력: ")


    cont[name] = num

    if name == "" or num == "":
        break


while 1:

    na = input("(검색모드)이름 입력: ")
    if na in cont:
        print("전화번호는", cont[na], "입니다.")
    else:
        print("잘못된 이름입니다.")
