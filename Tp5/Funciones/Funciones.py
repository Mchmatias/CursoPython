
from datetime import datetime #ejercicio 8
import random  #Ejercicio 4
import time #Ejercicio 6

def redondear(numero):  #Ejercicio 1
    inicio = time.time()
    if numero - int(numero) >= 0.5:
        print(int(numero) + 1)
    else:
        print(int(numero))
    fin = time.time()
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
    
def num_par_azar():  #Ejercicio 4
    inicio = time.time()
    print(random.choice([2, 4, 6, 8, 10]))
    fin = time.time()
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")

def bola_magica(pregunta):  #Ejercicio 5
    inicio = time.time()
    respuestas = [ 
        "Es seguro que sí ",
        "Las chances son buenas", 
        "Puedes contar con ello",
        "Pregúntame de nuevo más tarde", 
        "Concéntrate y pregunta de nuevo",
        "No veo con claridad, intenta de nuevo",
        "Mi respuesta es no",
        "Mis fuentes me dicen que no"
    ]
    print(f"{random.choice(respuestas)}")
    fin = time.time()
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")

def sorteo(pozo, cantidad_ganadores=1):  #Ejercicio 7
    """
    pozo: lista de nombres o números en el pozo
    cantidad_ganadores: cuántos papeles se sacan
    """
    if cantidad_ganadores > len(pozo):
        print("No hay suficientes papeles en el pozo.")
        return
    ganadores = random.sample(pozo, cantidad_ganadores)
    print("Ganador/es:", ganadores)

#sorteo(["Ana", "Luis", "Carlos", "Marta", "Sofía"], 2)

def dias_desde_nacimiento():  #| ejercicio 8
    try:
        anio = int(input("Año de nacimiento: "))
        mes = int(input("Mes de nacimiento: "))
        dia = int(input("Día de nacimiento: "))
        fecha_nac = datetime(anio, mes, dia)
        hoy = datetime.now()
        dias = (hoy - fecha_nac).days
        print(f"Han pasado {dias} días desde su nacimiento.")
    except Exception:
        print("Datos incorrectos. Ingrese números válidos.")


