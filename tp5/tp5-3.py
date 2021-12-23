def ler_numero():
    dado_ok = False
    while not dado_ok:
        try:
            num = int(input("entre com um numero: "))
            dado_ok = True
        except ValueError:
            print("numero invalido")
    return num

def list_rev(allnum):
    for i in range(len(allnum)-1,-1,-1):
        print(allnum[i], end = " ")

allnum = []
num = ler_numero()
while (num != 0):
    allnum.append(num)
    num = ler_numero()
list_rev(allnum)