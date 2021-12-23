def ler_int():
    dado_ok = False
    while not dado_ok:
        try:
            num = int(input())
            dado_ok = True
        except ValueError:
            print("numero invalido")
    return num  

def ler_str():
    dado_ok = False
    while not dado_ok:
        try:
            string = str(input())
            dado_ok = True
        except ValueError:
            print("input invalido")
    return string

def ler_float():
    dado_ok = False
    while not dado_ok:
        try:
            fnum = float(input())
            dado_ok = True
        except ValueError:
            print("numero invalido")
    return fnum

def ler_contas(contas):
    with open(NOME_ARQUIVO, "r") as arq:
        linha = arq.readline()
        while (linha != ""):
            linha = linha.strip("\n\n")
            linha = linha.split(";")
            linha[0],linha[1],linha[2] = int(linha[0]),str(linha[1]),float(linha[2]) #botar sobrenome e nome juntos
            contas.append(linha)
            linha = arq.readline() 

def grava_contas(contas):
    with open(NOME_ARQUIVO, "w") as arq:
        for conta in contas:
            arq.write(str(conta[0]) + ";" + conta[1] + ";" + str(conta[2]) + "\n") #juntar nme e sobrenome aqui tb
    print("arquivo gravado com sucesso")

def achar_conta(contas, numcont):
    pos = -1
    for i in range(len(contas)):
        if contas[i][0] == numcont:
            pos = i
            break
    return pos

def test_conta(contas, numcont):
    achou = False
    for conta in contas:
        if (conta[0] == numcont):
            achou = True
            break
    return achou

#ajustar os nomes no resto
def nome_conta():
    while True:
        nome = ler_str()
        if (len(nome.split(" ")) >= 2):
            break
        print("o nome precisa ter pelo menos 2 caracteres:")
    return nome

def saldo_conta():
    saldo = ler_float()
    while (saldo < 0):
        print("o saldo precisa ser maior que 0:")
        saldo = ler_float()
    return saldo

def add_conta(contas):
    print(("-" * 35),"\n\n","inclusao de conta","\n\n","insira o numero da nova conta:")
    numcont = ler_int()
    while test_conta(contas, numcont):        
        print("\n","numero de conta ja existe, tente denovo:")
        numcont = ler_int()
    else:
        print("\n","insira o nome e sobrenome do dono da nova conta:")
        nome = nome_conta()
        print("\n","saldo inicial:")
        saldo = saldo_conta()
        nconta = [numcont,nome,saldo] #juntar nome e sobrenome aqui tb
        print(("-" * 35),"\n\n","numero da conta:",numcont,"\n\n","nome do correntista:",nome,"\n\n","saldo da conta:",saldo,"\n\n","conta adicionada com sucesso")
        contas.append(nconta)
        contas.sort()

def change_conta(contas):
    print("\n",("-" * 35),"\n\n","alteracao de saldo","\n\n","escolha a conta a ter o saldo alterado:",)
    numcont = ler_int()
    pos = achar_conta(contas,numcont)
    if (pos != -1):
        mostrar_conta(contas,pos)
        menu_crebito() #botar esses em funcao tb, tirar isso de voltar ao menu
        crebito = ler_int()
        if (crebito == 1):
            add_credito(contas,pos)
        elif (crebito == 2):
            add_debito(contas,pos)
        else:
            print("escolha uma opcao valida:")
            crebito = ler_int()   
        mostrar_conta(contas,pos)
    else:
        print("conta inexistente, tente novamente")

def add_credito(contas,pos):
    print("\n","insira a quantidade de credito a ser adicionada:")
    cred = ler_float()
    contas[pos][2] += cred

def add_debito(contas,pos):
    print("\n","insira a quantidade de debito a ser adicionada:")
    deb = ler_float()
    contas[pos][2] -= deb

def del_conta(contas):
    print(("-" * 35),"\n\n","exclusao de conta","\n\n","escolha a conta a ser excluida:")
    numcont = ler_int()
    pos = achar_conta(contas,numcont)
    if (pos != -1):
        if (contas[pos][2] == 0):
            print(mostrar_conta(contas,pos),"conta excluida com sucesso")
            contas.remove(contas[pos])
        else:
            print("erro, saldo da conta nao eh 0")
    else:
        print("conta inexistente")

def contas_neg(contas):
    for i in range(len(contas)):
        if (contas[i][2] < 0):
            print("\n",("-" * 35),"\n\n","numero da conta:",contas[i][0],"\n\n","nome do correntista:",contas[i][1],"\n\n","saldo da conta:",contas[i][2])

def filtrar_contas(contas):         
    print("\n","escolha um valor para filtrar:")
    valmin = ler_int()
    for i in range(len(contas)):
        if (contas[i][2] > valmin):
            print("\n",("-" * 35),"\n\n","numero da conta:",contas[i][0],"\n\n","nome do correntista:",contas[i][1],"\n\n","saldo da conta:",contas[i][2])

def mostrar_contas(contas):
    for i in range(len(contas)):
        print("\n",("-" * 35),"\n\n","numero da conta:",contas[i][0],"\n\n","nome do correntista:",contas[i][1],"\n\n","saldo da conta:",contas[i][2])

def mostrar_conta(contas,pos):
    print("\n",("-" * 35),"\n\n","numero da conta:",contas[pos][0],"\n\n","nome do correntista:",contas[pos][1],"\n\n","saldo da conta:",contas[pos][2],"\n")

def rel_conta(contas): #quebrar em aprtes q nem menu la embaixo
    menu_relatorio()
    gerenc = ler_int()
    if (gerenc == 1):
        contas_neg(contas) 
    elif (gerenc == 2):
        filtrar_contas(contas)
    elif (gerenc == 3):
        mostrar_contas(contas) #criar funcao que faz print das contas mais arrumado, com nome: contas[pos][1] e etc
    else:
        print("escolha uma opcao valida:")

def menu_principal():
    print("\n",("-" * 35),"\n\n","Menu:","\n\n","[1] - inclusao de conta","\n","[2] - alteracao de saldo","\n",
    "[3] - exclusao de conta","\n","[4] - relatorios gerenciais","\n","[5] - salvar modificacoes e sair do programa","\n\n","escolha uma opcao:")

def menu_relatorio():
    print("\n",("-" * 35),"\n\n","relatorios gerenciais:","\n\n","[1] - listar contas com saldo negativo","\n","[2] - contas com saldo acima de x","\n",
    "[3] - listar todas as contas","\n\n","escolha uma opcao:")

def menu_crebito():
    print("\n",("-" * 35),"\n\n","escolha:","\n\n","[1] - credito","\n\n","[2] - debito","\n")

NOME_ARQUIVO = "contas.txt"
contas = []
ler_contas(contas)
menu_principal()
escolha = ler_int()
while (escolha != 5):
    if (escolha == 1):
        add_conta(contas)
    elif (escolha == 2):
        change_conta(contas)
    elif (escolha == 3):
        del_conta(contas)
    elif (escolha == 4):
        rel_conta(contas)
    else:
        print("opcao invalida")
    menu_principal()
    escolha = ler_int()
contas.sort()
grava_contas(contas)