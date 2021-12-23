def check_data():
    dado_ok = False
    while not dado_ok:
        data_valida = True
        try:
            data = input("insira a data no formato dd/mm/aaaa: ")
            datas = data.split("/")
            dia = int(datas[0])
            mes = int(datas[1])
            ano = int(datas[2])
            if((dia <= 0) or (dia > 31)):
                raise Exception
            elif((mes <= 0) or (mes > 12)):
                raise Exception
            elif((mes == (4 or 6 or 9 or 11)) and (dia > 30)):
                raise Exception
            elif(((ano % 4 == 0) and (ano % 100 != 0))  or ((ano % 400 == 0))):
                if(mes == 2):
                    if(dia == 29):
                        data_valida = True
                        dado_ok = True
                    else:
                        raise Exception
            else:
                data_valida = True
            dado_ok = True
        except (IndexError, ValueError, Exception):
            data_valida = False
    return data_valida


if(check_data()):
    print("data valida")
else:
    print("data invalida")