Readme.

Programa de cálculos intensivos
Este programa es un ejemplo de cómo distribuir tareas intensivas de cálculo en paralelo utilizando la biblioteca concurrent.futures de Python. El objetivo es realizar cálculos intensivos utilizando la biblioteca NumPy y distribuir la carga de trabajo en múltiples hilos para aprovechar los recursos de la CPU.

Funcionalidad:
El programa consta de dos partes principales:

La función intensive_calculation(start, end) realiza un cálculo intensivo en un rango de valores utilizando la biblioteca NumPy. Genera un arreglo de números aleatorios y realiza una serie de operaciones sobre ellos para obtener un resultado.

La función main() distribuye la carga de trabajo en múltiples hilos mediante ThreadPoolExecutor y recopila los resultados de las tareas para obtener el resultado final.

El programa permite ejecutar continuamente las tareas de cálculo intensivo mientras el usuario no ingrese el comando "stop". Se pausa durante 1 segundo entre cada ejecución del bucle para evitar un uso excesivo de los recursos de la CPU.

Requisitos:
El programa requiere tener instaladas las siguientes bibliotecas de Python:

NumPy
concurrent.futures
Puedes instalar estas bibliotecas utilizando pip con el siguiente comando:

        pip install numpy

Uso
Para ejecutar el programa, simplemente ejecuta el archivo Python. El programa comenzará a realizar los cálculos intensivos en múltiples hilos y mostrará el resultado final. Si deseas detener la ejecución del programa, ingresa el comando "stop" cuando se te solicite.

Nota: Ten en cuenta que se trata de elevar la tempratura, monitorea el sistema mientras se ejecuta el programa.
