import random
import multiprocessing
from time import perf_counter

# Função que irá adicionar números aleatórios a uma lista
def list_append(count, id, out_list): 
    for i in range(count):
        out_list.append(random.random())

if __name__ == "__main__":
    size = 1_000_000   # Quantidade de números aleatórios que serão adicionados
    procs = 10  # Número de processos a serem criados

    jobs = []  # Lista para armazenar os processos

    # Criando os processos
    for i in range(0, procs):
        out_list = list()  # Cria uma lista vazia para cada processo
        process = multiprocessing.Process(target=list_append, 
                                          args=(size, i, out_list))
        jobs.append(process)

    start_time = perf_counter()  # Inicia a contagem do tempo

    # Inicia cada processo
    for j in jobs:
        j.start()

    # Espera até que todos os processos terminem
    for j in jobs:
        j.join()

    end_time = perf_counter()  # Finaliza a contagem do tempo
    print(f'Levou {end_time - start_time:0.4f} segundos para processar.')
