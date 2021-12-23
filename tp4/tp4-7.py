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

num = test_input()
if test_prime(num):
    print(num,"é numero primo")
else:
    print(num,"nao é numero primo")