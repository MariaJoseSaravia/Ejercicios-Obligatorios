def minimo_comun_multiplo(num1, num2):
    mult = max(num1, num2)

    while True:
        if (mult % num1 == 0) and (mult %num2 == 0):
            return mult
        mult += 1

print(minimo_comun_multiplo(2,4))
print(minimo_comun_multiplo(32, 13))
print(minimo_comun_multiplo(17, 15))