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
soma = 0
n = 0
FIM = 0
num = ler_numero()
while (num != FIM):
    soma = soma + num
    allnum.append(num)
    n = n + 1
    num = ler_numero()
if (n > 0):
    print(allnum)
    print("soma =", soma)
    print("media =", soma/n)
    print("maior numero =", max(allnum))
    print("menor numero =", min(allnum))
else:
    print("nenhum dado inserido")