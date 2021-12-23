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
indice = -1
for i in range(len(lista)):
    if (lista[i] == num):
        indice = i
        break
if (indice >= 0):
    print("numero esta na lista, na posicao", indice)
else:
    print("numero nao esta na lista")