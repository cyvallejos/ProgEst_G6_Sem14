import time
import random

#Generar intervalos
def generar_intervalos(cantidad):
    elementos = [
        max(1, cantidad // 4),
        max(1, cantidad //2),
        cantidad
    ]
    return sorted(set(elementos))


#Generar numeros
def generar_numeros(cantidad):
    inicio = time.perf_counter()
    datos = [random.randint(0, 5_000_000) for _ in range(cantidad)]
    fin = time.perf_counter()
    tiempo = fin - inicio
    return datos, tiempo

cantidad = int(input("Cantidad de elementos: "))
datos, tiempo = generar_numeros(cantidad)
print("Iniciar generación.")
print(f"Tiempo en ejecucion: {tiempo:.4f}")
print("Fin de generación.")
ini = time.perf_counter()
print(datos)
fin = time.perf_counter()
dif = fin - ini
print(f"Tiempo en ejecución: {tiempo:.4f}")
print(f"Duración de impresión: {dif:.4f}")


# Ordenar los números aleatorios generados arriba y medir cuánto tarda.
def ordenar_burbuja(datos):
    for i in range(len(datos) - 1):
        hubo_intercambio = False
        for j in range(len(datos) - 1 - i):
            if datos[j] > datos[j + 1]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
                hubo_intercambio = True
        if not hubo_intercambio:
            break
    return datos


inicio_ordenamiento = time.perf_counter()
ordenar_burbuja(datos)
tiempo_ordenamiento = time.perf_counter() - inicio_ordenamiento
print(f"\nEl tiempo que tardó en ordenar los números aleatorios fue: {tiempo_ordenamiento:.6f} segundos")
print("Números ordenados:", datos)