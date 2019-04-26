while 1:
    bir = input("생년월일 입력")
    list_bir = []
    for i in bir:
        list_bir.append(i)

    t_bir = (list_bir)


    print(t_bir)
    if len(t_bir) != 8 or t_bir[0] == 0:
        print("잘못된 생년월일 입니다.")
        continue
    elif int(t_bir[4]) > 1 or int(t_bir[6]) > 3:
        print("잘못된 생년월일 입니다.")
        continue
    elif t_bir[4] == 1 and int(t_bir[5])>2:
        print("잘못된 생년월일 입니다.")
        continue
    elif t_bir[6] == str(3) and int(t_bir[7]) > 1:
        print("잘못된 생년월일 입니다.")
        continue


