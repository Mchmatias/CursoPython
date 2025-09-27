# def factorial(numero):
#     fact = numero
#     for multiplicador in range(1,fact):
#         fact = fact * multiplicador
#     print(fact)

# x=6
# factorial(x)


def num_es_prim(numero):
    if numero <= 1:
        return False
    for contador in range(2,numero):
        if numero % contador == 0:
            return False
    return True

def numeros_primos(num):
    for num in range(1,num+1):
        if num_es_prim(num):
            print(num)

numero = int(input("ingrese su numero:"))

numeros_primos(numero)