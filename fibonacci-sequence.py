# Programa que genera la secuencia 
# de Fibonacci hasta el término 
# solicitado por el usuario.

try:
    element = int(input("¿Cuántos elementos de la secuencia quieres?: "))
    fibo_list = [0, 1]
    if element <= 0:
        print("¡Debes ingresar un número entero mayor que cero")
    elif element == 1:
        print(fibo_list[0])
    else:
        for i in range(2,element):
            new_element = fibo_list[i-1] + fibo_list[i-2]
            fibo_list.append(new_element)
        print(fibo_list)
except:
    print("¡Debes ingresar un número entero mayor que cero!")