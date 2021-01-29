# Programa que le pide un número al usuario y le indica si el número ingresado 
# forma parte de la secuencia de Fibonacci.

flag = True
while flag:
    try:
        user_number = int(input("Ingrese un número: "))
        flag = False
    except:
        print("Debe ingresar un número.")
fibo_list = [0, 1]
for i in range(2,6):
    new_number = fibo_list[i-1] + fibo_list[i-2]
    if new_number <= user_number:
        fibo_list.append(new_number)
    else:
        break
if user_number > 5:
    for j in range(6,user_number):
        new_number = fibo_list[j-1] + fibo_list[j-2]
        if new_number <= user_number:
            fibo_list.append(new_number)
        else:
            break
if user_number in fibo_list:
    index = fibo_list.index(user_number) + 1
    if user_number == 1:
        print("El número", user_number, "es el elemento", index, "y", (index+1), "de la secuencia de Fibonacci.")
    else:
        print("El número", user_number, "es el elemento", index, "de la secuencia de Fibonacci.")
else:
    print("El número", user_number, "no está en la secuencia de Fibonacci.")