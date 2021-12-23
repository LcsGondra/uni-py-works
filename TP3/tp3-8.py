nummax = int(input("quantos numeros: "))
n1 = int(input("primeiro numero: "))
n2 = int(input("segundo numero: "))
razao = n2 - n1
c = 0
while (c < nummax):
    print(n1,end = " ")
    n2 = n1 + razao
    n1 = n2
    c += 1