# -*- coding: utf-8 -*-
'''
██████╗  ██████╗███████╗██╗██████╗ ███████╗
██╔══██╗██╔════╝██╔════╝██║██╔══██╗██╔════╝
██████╔╝██║     █████╗  ██║██████╔╝█████╗  
██╔═══╝ ██║     ██╔══╝  ██║██╔══██╗██╔══╝  
██║     ╚██████╗██║     ██║██║  ██║███████╗
╚═╝      ╚═════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝                                                             
'''                               
#######################################################
#    PcFire.py
#
# PcFire is a tool that allows you to perform intensive
# calculations in parallel by creating multiple 
# instances of the program. Each instance executes 
# complex calculations using the NumPy library and 
# stops after a predefined period of time.
#
#
# 10/18/23 - Changed to Python3 (finally)
#
# Author: Facundo Fernandez 
#
#
#######################################################

import os
import numpy as np  
import concurrent.futures
import time
import signal
from multiprocessing import Process 

def intensive_calculation(start, end):
    array = np.random.rand(end - start)  # Create an array of random numbers / Crear una matriz de números aleatorios

    result = np.sum(np.sin(np.sqrt(array)))  # Intensive calculation with NumPy / Cálculo intensivo con NumPy

    return result

def main():
    num_tasks = 4
    total_iterations = 10000000
    chunk_size = total_iterations // num_tasks

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i in range(num_tasks):
            start = i * chunk_size + 1
            end = (i + 1) * chunk_size + 1
            futures.append(executor.submit(intensive_calculation, start, end))
        
        # Collect and print the task results / Recoger e imprimir los resultados de la tarea
        result = sum(f.result() for f in futures)
        print("El resultado es:", result)

def create_and_run():
    while True:
        pid = os.fork()  # Bifurcates the current process / Bifurcates the current process
        if pid == 0:
            main()
            exit()

def signal_handler(sig, frame):
    # Maneja la señal SIGINT (Ctrl+C) / Handles SIGINT signal (Ctrl+C)
    print("Deteniendo procesos...")
    for process in processes:
        process.terminate()
        process.join()
    print("Procesos detenidos.")
    exit()

if __name__ == '__main__':
    num_instances = 5  # Number of instances you want to run in parallel / Número de instancias que desea ejecutar en paralelo
    processes = []

    # Capture SIGINT signal (Ctrl+C) to stop processes / Captura la señal SIGINT (Ctrl+C) para detener los procesos
    signal.signal(signal.SIGINT, signal_handler)

    for _ in range(num_instances):
        process = Process(target=create_and_run)
        process.start()
        processes.append(process)

    print("Presiona Ctrl+C para detener los procesos.")
    for process in processes:
        process.join()
