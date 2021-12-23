allnum = []
soma = 0
num = int(input("insira um numero inteiro: "))
for num in range(1,5):   
    allnum.append(num)
    soma += num
    num = int(input("insira um numero inteiro: "))
print("numeros inseridos: ", allnum)
print("soma =", soma)
print("media =", soma/20)
print("maior numero =", max(allnum))
print("menor numero =", min(allnum))