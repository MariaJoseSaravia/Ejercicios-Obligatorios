def get_int(a):
    try:
        return int(a)
        
    except ValueError:
        while True:         
           return get_int(input("Error: Ingrese un valor entero"))
a = input("Ingrese un numero entero: ")
print(get_int(a))
 