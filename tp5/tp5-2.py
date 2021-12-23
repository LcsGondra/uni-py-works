lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [10, 20, 30, 40, 50, 60, 70, 80]
lista3 = []
for i in range(len(lista1)):
    lista3.append(lista1[i] + lista2[i])
print(lista3)