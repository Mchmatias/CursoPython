"""
Ejercicio 1
"""


# def lista_enteros(numero1, numero2):
#     resultado = []
#     if numero1 <= numero2:
#         for contador in range(numero1, numero2 + 1):
#             resultado += [contador]
#     else:
#         for contador in range(numero1, numero2 - 1, -1):
#             resultado += [contador]
#     return resultado

# print(lista_enteros(2, 6))


"""
Ejercicio 2
"""


# def lista_pares(num1, num2):
#     resultado = []
#     if num1 < num2:
#         for contador in range(num1 + 1, num2):
#             if contador % 2 == 0:
#                 resultado += [contador]
#     else:
#         for contador in range(num1 - 1, num2, -1):
#             if contador % 2 == 0:
#                 resultado += [contador]
#     return resultado


# print(lista_pares(2, 89))


"""
Ejercicio 3
"""


# def contar_caracter(texto, caracter):
#     contador = 0
#     for car in texto:
#         if car.lower() == caracter.lower():  #ignora mayúsc/minúsc
#             contador += 1
#     return contador

# print(contar_caracter("hola mundo", "o"))


"""
Ejercicio 4
"""

# def primos_rango(num1, num2):
#     resultado = []
#     if num1 > num2:
#         num1, num2 = num2, num1  # me aseguro de que a sea menor
#     for num in range(num1 + 1, num2):  # rango abierto
#         if num > 1:
#             es_primo = True
#             for contador in range(2, num):
#                 if num % contador == 0:
#                     es_primo = False
#                     break
#             if es_primo:
#                 resultado += [num]
#     return resultado

# print(primos_rango(0,299))


"""
Ejercicio 5
"""

# def todos_pares(lista):
#     for num in lista:
#         if num % 2 != 0:
#             return False
#     return True

# print(todos_pares([222]))

"""
Ejercicio 6
"""


# def todos_primos(lista):
#     for num in lista:
#         if num < 2:
#             return False
#         es_primo = True
#         for contador in range(2, num):
#             if num % contador == 0:
#                 es_primo = False
#                 break
#         if not es_primo:
#             return False
#     return True

# print(todos_primos([3]))


#Realizado por Ramirez Galvan Jose Mahias