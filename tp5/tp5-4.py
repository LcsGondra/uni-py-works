def ler_numero():
    dado_ok = False
    while not dado_ok:
        try:
            num = int(input("entre com um numero: "))
            dado_ok = True
        except ValueError:
            print("numero invalido")
    return num

allnum = []
num = ler_numero()
FIM = 0
while (num != FIM):
    allnum.append(num)
    num = ler_numero()
if (len(allnum) != 0):
    media = sum(allnum)/len(allnum)
    for i in allnum :
        if (i >= media):
            print(i, end = " ")
else:
    print("lista vazia")
