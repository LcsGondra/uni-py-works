n1 = int(input("insira o primeiro numero: "))
n2 = int(input("insira o segundo numero: "))
n3 = int(input("insira o terceiro numero: "))
if(n1 > (n2 and n3)):
    print("o numero maior é",n1)
elif (n2 > (n1 and n3)):
    print("o numero maior é",n2)
elif (n3 > (n1 and n2)):
    print("o numero maior é",n3)
elif (n2 == n3 == n1):
    print("os numeros sao iguais")