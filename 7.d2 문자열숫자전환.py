cont = dict()

cont['A'] = cont['B'] = cont['C'] = '2'
cont['D'] = cont['E'] = cont['F'] = '3'
cont['G'] = cont['H'] = cont['I'] = '4'
cont['J'] = cont['K'] = cont['L'] = '5'
cont['M'] = cont['N'] = cont['O'] = '6'
cont['p'] = cont['Q'] = cont['R'] = cont['S'] = '7'
cont['T'] = cont['U'] = cont['V'] = '8'
cont['W'] = cont['X'] = cont['Y'] = cont['Z'] = '9'
b = ""
str = input("문자열을 입력하세요: ")
for i in str:

    b += cont[i]

print(b)
