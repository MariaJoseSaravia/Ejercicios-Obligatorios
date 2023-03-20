def cuenta_palabras(texto):
    claves=texto.split()
    diccionario=dict()
    
    for i in claves:
        cont=claves.count(i)
        diccionario.setdefault(i,cont)
    return(diccionario)
    
    
    
def cuenta_palabras2(diccionario):
    valores=list()
    tupla=tuple()
    max=0
    for i in diccionario:
        valores.append(diccionario[i])
    print(valores)
    for x in valores:
        if x >= max:
            max=x
    for z in diccionario:
        if diccionario[z]==max:
            tupla = z,max
    return tupla
        

texto= input("Ingrese un texto: ")
resul=cuenta_palabras(texto)
resultado=cuenta_palabras2(resul)
print("funcion 1",resul,"funcion 2",resultado)
