def ler_matrix():
    matrix = [[0] * 2,[0] * 2]
    for i in range(len(matrix)):
        for j in range (len(matrix[i])):
            dado_ok = False
            while not dado_ok:
                try:
                    num = int(input("entre com um numero: "))
                    dado_ok = True
                except ValueError:
                    print("numero invalido")
            matrix[i][j] = num
    return matrix
            

def soma_matrix(matrix1, matrix2):
    matrix3 = [[0] * 2,[0] * 2]
    for i in range(len(matrix3)):
        for j in range (len(matrix3[i])):
            matrix3[i][j] = matrix1[i][j] +matrix2[i][j]
    return matrix3

matrix1 = ler_matrix()
print("matrix1: ", matrix1)
matrix2 = ler_matrix()
print("matrix2:", matrix2)
print("Soma das matrizes:", soma_matrix(matrix1, matrix2))