import numpy as np
import concurrent.futures
import time

def intensive_calculation(start, end):
    array = np.random.rand(end - start)  # Create an array of random numbers / Crear un arreglo de números aleatorios

    result = np.sum(np.sin(np.sqrt(array)))  # Intensive calculation with NumPy / Cálculo intensivo con NumPy

    return result

def main():
    num_tasks = 4  # Number of tasks to distribute the load / Número de tareas para distribuir la carga
    total_iterations = 10000000  # We increase the number of iterations / Incrementamos el número de iteraciones
    chunk_size = total_iterations // num_tasks

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i in range(num_tasks):
            start = i * chunk_size + 1
            end = (i + 1) * chunk_size + 1
            futures.append(executor.submit(intensive_calculation, start, end))
        
        # Collect task results / Recopilar los resultados de las tareas
        result = sum(f.result() for f in futures)
        
    print("El resultado es:", result)

def detener_programa():
    comando = input("Ingresa un comando: ")
    if comando == "stop":
        return True
    else:
        return False

if __name__ == '__main__':
    while not detener_programa():
        main()
        time.sleep(1)  # Pause of 1 second between each execution of the loop / Pausa de 1 segundo entre cada ejecución del bucle
