# Función que toma un número como argumento y le indica al usuario si el número forma 
# parte de la secuencia de Fibonacci.

def isFibonacci(user_number):
    # A modo de ejemplo: 
    # isFibonacci(1)
    # El número 1 es el elemento 2 y 3 de la secuencia de Fibonacci.
    # isFibonacci(8)
    # El número 8 es el elemento 7 de la secuencia de Fibonacci.
    # isFibonacci(2923)
    # El número 2923 no está en la secuencia de Fibonacci.

    fibo_list = [0, 1]
    for i in range(2,user_number+2):
        new_number = fibo_list[i-1] + fibo_list[i-2]         
        if new_number <= user_number:
            fibo_list.append(new_number)
        else:
            break
    if user_number in fibo_list:
        position = fibo_list.index(user_number) + 1
        if user_number == 1:
            print("El número", user_number, "es el elemento", position, "y", (position+1), "de la secuencia de Fibonacci.")
        else:
            print("El número", user_number, "es el elemento", position, "de la secuencia de Fibonacci.")
    else:
        print("El número", user_number, "no está en la secuencia de Fibonacci.")