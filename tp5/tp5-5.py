def ler_numero():
    dado_ok = False
    while not dado_ok:
        try:
            num = int(input("entre com um numero: "))
            dado_ok = True
        except ValueError:
            print("numero invalido")
    return num

lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
num = ler_numero()
while num not in lista:
    num = ler_numero()
if num in lista:
    print("numero esta na lista")
