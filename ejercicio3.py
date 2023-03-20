texto = """Un texto es una composición de signos codificados en un sistema de escritura que forma una unidad de sentido"""
quitar =".()"
for caracter in quitar:
    texto = texto.replace(caracter, "")
texto = texto.lower()

palabras =texto.split()
diccionario_frecuencias = {}
for palabra in palabras:
    if palabra in diccionario_frecuencias:
        diccionario_frecuencias[palabra] += 1
    else:
         diccionario_frecuencias[palabra] = 1
for palabra in diccionario_frecuencias:
    frecuencia=diccionario_frecuencias[palabra]
    print(f"La palabra: '{palabra}' ,tiene la frecuencia de:'{frecuencia}'")

