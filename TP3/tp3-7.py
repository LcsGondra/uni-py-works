a = 0
b = 1
num = int(input("quantidade de numeros desejados na sequencia: "))
if num <= 1:
    print("insira um numero maior que 1 para formar uma sequencia")
else:
    for i in range(num):
        print(a,end=" ") 
        c = a + b
        a = b
        b = c