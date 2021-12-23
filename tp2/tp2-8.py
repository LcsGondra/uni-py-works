ip = input("insira seu ip: ")
prim_ponto = ip.find(".")
prim_octeto = int(ip [:prim_ponto])
if((0 <= prim_octeto) and (prim_octeto <= 127)):
    print("ip classe A")
elif((128 <= prim_octeto) and (prim_octeto <= 191)):
    print("ip classe B")
elif((192 <= prim_octeto) and (prim_octeto <= 223)):
    print("ip classe C")
elif((224 <= prim_octeto) and (prim_octeto <= 239)):
    print("ip classe D")
elif((240 <= prim_octeto) and (prim_octeto <= 255)):
    print("ip classe E")
else:
    print("ip invalido, tente novamente")
