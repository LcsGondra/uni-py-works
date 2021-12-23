sal=float(input("valor do salario: "))
if((sal <= 1000) and (sal > 0)):
    print(sal*1.3)
elif(1000 < sal <= 2000):
    print(sal*1.25)
elif(2000 < sal <= 3000):
    print(sal*1.2)
elif(3000 < sal <= 4000):
    print(sal*1.15)
elif(4000 < sal):
    print(sal*1.1)
else:
    print("insira um salario valido")