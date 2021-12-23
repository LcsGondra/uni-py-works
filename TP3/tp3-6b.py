allnum = []
soma = 0
n = 0
num = input("insira um numero inteiro: ")
while (num != 0):
    if isinstance(num, int):
        soma = soma + num
        allnum.append(num)
        n = n + 1
    num = input("insira um numero inteiro: ")
print(allnum)
print("soma =", soma)
print("media =", soma/n)
print("maior numero =", max(allnum))
print("menor numero =", min(allnum))