allnum = []
soma = 0
n = 0
FIM = 0
num = int(input("insira um numero inteiro: "))
while (num != FIM):
    if isinstance(num, int):
        soma = soma + num
        allnum.append(num)
        n = n + 1
    num = int(input("insira um numero inteiro: "))
if (n > 0):
    print(allnum)
    print("soma =", soma)
    print("media =", soma/n)
    print("maior numero =", max(allnum))
    print("menor numero =", min(allnum))
else:
    print("nenhum dado inserido")