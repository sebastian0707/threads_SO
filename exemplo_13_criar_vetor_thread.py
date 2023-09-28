import random
import threading
from time import perf_counter

def list_append(count, id, out_list):
    for i in range(count):
        out_list.append(random.random())

if __name__ == "__main__":
    size = 1_000_000   # Quantidade de números aleatórios que serão adicionados
    procs = 10  # Número de threads a serem criadas

    jobs = []  # Lista para armazenar as threads

    for i in range(0, procs):
        out_list = list()  # Cria uma lista vazia para cada thread
        thread = threading.Thread(target=list_append, args=(size, i, out_list))  # Correção: Adiciona args=(size, i, out_list)
        jobs.append(thread)

    start_time = perf_counter()  # Inicia a contagem do tempo

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    end_time = perf_counter()  # Finaliza a contagem do tempo
    print(f'Levou {end_time - start_time:0.4f} segundos para processar.')
