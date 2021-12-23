vogais = ("a","A","e","E","i","I","o","O","u","U")
car = input("insira o caractere: ")
c = 0
while (car != "."):
    if (car in vogais):
        c += 1
    car = input("insira o caractere: ")
print("numero de vogais:", c)