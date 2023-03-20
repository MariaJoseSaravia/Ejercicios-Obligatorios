def maximo_comun_div(num1,num2):
    maximo_comun_div=1

    if num1 % num2 ==0:
        return num2
    
    for i in range(int(num2/2), 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            maximo_comun_div = i
            break
    return maximo_comun_div
print(maximo_comun_div(8,4))
print(maximo_comun_div(15,9))