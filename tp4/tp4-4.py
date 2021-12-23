def soma_num(num):
    soma = 0
    for i in range(1,num + 1):
        soma += i
    return(soma)

dado_ok = False
while not dado_ok:
    try:
        num = int(input("insira ate que numero deseja somar: ")) 
        print(soma_num(num))
        dado_ok = True
    except (ValueError):
        print("insira um numero valido")