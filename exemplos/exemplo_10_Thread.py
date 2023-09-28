import threading
import time

# Variável global N
N = 0

# Criando um objeto Lock para controlar o acesso à região crítica
lock = threading.Lock()

# Função executada por cada thread
def worker():
    global N
    
    print(threading.currentThread().getName(), 'Starting', N)
    
    # Início da região crítica (adquirindo o lock)
    lock.acquire()
    
    M = N
    print(M)
    time.sleep(1)  # Simulando algum trabalho
    
    N = M + 1
    
    # Fim da região crítica (liberando o lock)
    lock.release()
    
    #time.sleep(1)
    print(threading.currentThread().getName(), 'Exiting', N)

if __name__ == '__main__':
    jobs = []  # Lista para armazenar as threads

    # Cria e inicia 5 threads
    for i in range(5):
        t = threading.Thread(target=worker)  # Cria uma nova thread que executará a função 'worker'
        jobs.append(t)  # Adiciona a nova thread à lista 'jobs'
        t.start()       # Inicia a thread

    # Aguarda até que todas as threads tenham terminado
    for j in jobs:
        j.join()

    # Após todas as threads terminarem, imprime o valor de N
    print("O valor de N é ", N)
