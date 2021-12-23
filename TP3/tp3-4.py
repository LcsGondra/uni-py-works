allnum = []
soma = 0
nummax = int(input("insira a quantidade de numeros a serem inseridos: "))
num = int(input("insira um numero inteiro: "))
for num in range(nummax):
    soma = soma + num
    allnum.append(num)
    num = int(input("insira um numero inteiro: "))
print("soma =", soma)
print("media =", soma/nummax)
print("maior numero =", max(allnum))
print("menor numero =", min(allnum))