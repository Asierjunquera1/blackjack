cartas = { 
    chr(0x1f0a1): 11, 
    chr(0x1f0a2): 2, 
    chr(0x1f0a3): 3, 
    chr(0x1f0a4): 4, 
    chr(0x1f0a5): 5, 
    chr(0x1f0a6): 6, 
    chr(0x1f0a7): 7, 
    chr(0x1f0a8): 8, 
    chr(0x1f0a9): 9, 
    chr(0x1f0aa): 10, 
    chr(0x1f0ab): 10, 
    chr(0x1f0ad): 10, 
    chr(0x1f0ae): 10, 
} 

def valor():
    return cartas
def diccionario_a_lista():
    lista=[]
    for i in cartas:
        lista.append(i)
    return lista

lista_cartas=diccionario_a_lista()
def pedir_carta():
    carta=int(input("Elija una carta del 1 al 13:"))
    return lista_cartas[carta-1]
def escoger_2_cartas():
    lista2=[]
    for i in range(2):
        lista2.append(pedir_carta())
    return lista2


def valor_carta():
    lista3=escoger_2_cartas()
    dic={}
    for i in lista3:
        dic[i]=cartas[i]
    return dic

import random
def escoger_dos_cartas_al_azar():
    dic2={}
    for i in range(2):
        numero=random.randint(0,12)
        dic2[lista_cartas[numero]]=cartas[lista_cartas[numero]]
    return dic2

def sumar_cartas(cartasDic):
    contador=0
    for i in cartasDic:
        contador+=cartasDic[i]
    return contador
def jugar():
    jugador=valor_carta()
    maquina=escoger_dos_cartas_al_azar()
    valorj=sumar_cartas(jugador)
    valorm=sumar_cartas(maquina)
    print("Tus cartas son:", jugador)
    print("Las cartas de la banca son:", maquina)
    if valorj>valorm:
        print("Has ganado")
    elif valorj<valorm:
        print("Has perdido")
    else:
        print("Has empatado")
jugar()



