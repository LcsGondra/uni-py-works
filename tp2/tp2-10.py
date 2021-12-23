data = input("insira a data no formato dd/mm/aaaa: ")
datas = data.split("/")
dia = int(datas[0])
mes = int(datas[1])
ano = int(datas[2])
if((dia <= 0) or (dia > 31)):
    print("data invalida")
elif((mes <= 0) or (mes > 12)):
    print("data invalida")
elif((mes == (4 or 6 or 9 or 11)) and (dia > 30)):
    print("data invalida")
elif(((ano % 4 == 0) and (ano % 100 != 0))  or ((ano % 400 == 0))):
    if(mes == 2):
        if(dia == 29):
            print("data valida")
        else:
            print("data invalida")
else:
    print("data valida")