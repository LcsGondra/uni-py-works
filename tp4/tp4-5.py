def test_input():
    dado_ok = False
    while not dado_ok:
        try:
            num = int(input("insira um numero: ")) 
            dado_ok = True
        except (ValueError):
            print("insira um numero valido")
    return num

def fibo(num):
    a = 0
    b = 1
    for i in range(num):
        print(a,end=" ") 
        c = a + b
        a = b
        b = c

print("insira a quantidade de numeros desejados na sequencia:")
num = test_input()
while num <= 1:
    print("insira um numero maior que 1 para formar uma sequencia")
    num = test_input()
else:
    fibo(num)