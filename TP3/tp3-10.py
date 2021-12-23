def test_input():
    dado_ok = False
    while not dado_ok:
        try:
            num = int(input("insira um numero: ")) 
            dado_ok = True
        except (ValueError):
            print("insira um numero valido")
    return num

print("insira o numero inicial:")
num1 = test_input()
print("insira o numero final:")
num2 = test_input()
cont = 0
for i in range(num1, num2 + 1):
    if (i <= 1):
        print(i,"nao eh numero primo")
    else:
        for j in range(2,i):
            if((i % j) == 0):
                print(i,"nao eh numero primo")
                break
        else:
            print(i,"eh numero primo")
            cont += 1
print(cont, "numeros primos encontrados")
