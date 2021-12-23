def test_input():
    dado_ok = False
    while not dado_ok:
        try:
            num = int(input("insira um numero: ")) 
            dado_ok = True
        except (ValueError):
            print("insira um numero valido")
    return num

num = test_input()
cont = 0
while (num != 0):
    if (num <= 1):
        print(num,"nao eh numero primo")
    else:
        for i in range(2,num):
            if((num % i) == 0):
                print(num,"nao eh numero primo")
                break
        else:
            print(num,"eh numero primo")
            cont += 1
    num = test_input()
print(cont, "numeros primos encontrados")
