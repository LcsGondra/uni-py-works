def ler_mes():
    dado_ok = False
    while not dado_ok:
        try:
            mes = int(input("entre com um numero: "))
            if (1 <= mes <= 12):
                dado_ok = True
        except ValueError:
            print("mes invalido")
    return mes

mes = ler_mes()
nummes = {
    1:"janeiro", 2:"fevereiro", 3:"março", 4:"abril", 
    5:"maio", 6:"junho", 7:"julho", 8:"agosto", 
    9:"setembro", 10:"outubro", 11:"novembro", 12:"dezembro"
}
print(nummes[mes])