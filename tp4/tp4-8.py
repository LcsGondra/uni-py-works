def test_prime(num):
    for i in range(2, num):
        if((num % i) == 0):
            return False
            break
    return True

def test_input():
    dado_ok = False
    while not dado_ok:
        try:
            num = int(input("insira um numero: ")) 
            dado_ok = True
        except (ValueError):
            print("insira um numero valido")
    return num

num1 = test_input()
num2 = test_input()
cont = 0
for i in range(num1, num2+1):
    if(test_prime(i)):
        cont += 1
        print(i, "eh primo")
print(cont, "numeros primos encontrados")