def ler_numero():
    dado_ok = False
    while not dado_ok:
        try:
            num = int(input("entre com um numero: "))
            dado_ok = True
        except ValueError:
            print("numero invalido")
    return num

num = ler_numero()
if (num <= 1):
    print(num,"nao eh numero primo")
else:
    for i in range(2,num):
        if((num % i) == 0):
            print(num,"nao eh numero primo")
            break
    else:
        print(num,"eh numero primo")