def vogal_test(car):
    if car in vogais:
        vogal_valido = True 
    else:
        vogal_valido = False
    return vogal_valido

dado_ok = False
vogais = ("a","A","e","E","i","I","o","O","u","U")
FIM = "."
car = input("insira o caractere: ")
c = 0
while not dado_ok:
    try:
        while (car != FIM):
            vogal_valido = vogal_test(car)
            if vogal_valido:
                c += 1
            car = input("insira o caractere: ")
        print("numero de vogais =", c)
        dado_ok = True
    except (ValueError):
        print("erro, tente novamente")