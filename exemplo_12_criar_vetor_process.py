import random
import multiprocessing

from time import perf_counter


def list_append(count, id, out_list): 
    for i in range(count):
        out_list.append(random.random())

if __name__ == "__main__":
    size = 1_000_000   # Quantidade de números ramdômicos que serão adicionado
    procs = 10  # Número de processos
   
    jobs = []
    for i in range(0, procs):
        out_list = list()
        process = multiprocessing.Process(target=list_append, 
                                          args=(size, i, out_list))
        jobs.append(process)

    start_time = perf_counter()
      
    for j in jobs:
        j.start()
    
    for j in jobs:
        j.join()

    end_time = perf_counter()
    print(f'Levou {end_time- start_time: 0.4f} segundos para processar.')