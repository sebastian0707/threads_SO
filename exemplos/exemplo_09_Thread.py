import threading
import time

# Variável global N
N = 0

# Função executada por cada thread
def worker():
    global N  # Indica que estamos usando a variável global N
    print(threading.currentThread().getName(), 'Starting', N)
    M = N  # Copia o valor atual de N para M
    print(M)
    time.sleep(1)  # Espera por 1 segundo (simulando algum trabalho)
    N = M + 1  # Incrementa o valor global de N
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
