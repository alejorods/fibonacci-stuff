# Programa que le pide un número al usuario y le indica si el número ingresado 
# forma parte de la secuencia de Fibonacci.

while True:
    try:
        user_number = int(input("Ingrese un número: "))
        break
    except:
        print("Debe ingresar un número.")
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