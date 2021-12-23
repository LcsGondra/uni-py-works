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
print(num)