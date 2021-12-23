n1 = int(input("insira o primeiro numero: "))
n2 = int(input("insira o segundo numero: "))
n3 = int(input("insira o terceiro numero: "))
if(n1 <= n2 <= n3):
    print(n1,n2,n3)
elif(n1 <= n3 <= n2):
    print(n1,n3,n2)
elif(n2 <= n1 <= n3):
    print(n2,n1,n3)
elif(n2 <= n3 <= n1):
    print(n2,n3,n1)
elif(n3 <= n1 <= n2):
    print(n3,n1,n2)
elif(n3 <= n2 <= n1):
    print(n3,n2,n1)