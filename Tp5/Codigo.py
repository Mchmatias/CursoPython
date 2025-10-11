from Funciones.Funciones import * #ejercicio 2
import datetime  #Ejercicio 3
import time #Ejercicio 6


def suma_decimal(numero1, numero2):  #Ejercicio 2
    inicio = time.time()
    suma = numero1 + numero2
    redondear(suma)
    fin = time.time()
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")

def mostrar_fecha_hora():  #Ejercicio 3
    inicio = time.time()
    print(datetime.datetime.now())  
    fin = time.time()
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")



def ejecutar_con_tiempos():  #Ejercicio 9
    tiempos = {}
    inicio = time.time()
    mostrar_fecha_hora()
    tiempos['mostrar_fecha_hora'] = time.time() - inicio

    inicio = time.time()
    suma_decimal(3.6, 4.2)
    tiempos['suma_decimal'] = time.time() - inicio

    inicio = time.time()
    num_par_azar()
    tiempos['num_par_azar'] = time.time() - inicio

    inicio = time.time()
    bola_magica("¿Voy a aprobar el examen?")
    tiempos['bola_magica'] = time.time() - inicio

    inicio = time.time()
    redondear(5.5)
    tiempos['redondear'] = time.time() - inicio

    print("\nTiempos de ejecución:")
    for funcion, t in tiempos.items():
        print(f"{funcion}: {t:.6f} segundos")


"""
Comprovacion del ejercicio 6
"""
# mostrar_fecha_hora()
# suma_decimal(3.6, 4.2)
# num_par_azar()
# bola_magica("¿Voy a aprobar el examen?")
# redondear(5.5)


