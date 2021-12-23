def test_input():
    dado_ok = False
    while not dado_ok:
        try:
            num = int(input("insira um numero: ")) 
            dado_ok = True
        except (ValueError):
            print("insira um numero valido")
    return num

def PA(termos, n1, n2):
    c = 0
    while (c < termos):
        print(n1,end = " ")
        n2 = n1 + razao
        n1 = n2
        c += 1

print("insira a quantidade de termos desejados para a PA:")
termos = test_input()
print("insira o primeiro termo:")
n1 =  test_input()
print("insira o segundo termo:")
n2 = test_input()
razao = n2 - n1
PA(termos,n1,n2)