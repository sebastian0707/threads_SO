# Região crítica é uma região de memória compartilhada que acessa um recurso que está 
# compartilhado e que não possa ser acessado concorrentemente por mais de uma linha de execução. 


# Para entender melhor região crítica é bom ter em mente o que seria Condição de disputa. 
# Esta consiste em um conjunto de recursos que deve ser compartilhado entre processos no 
# qual, em um mesmo intervalo tempo, dois ou mais processos tentem alocar uma mesma parte 
# de um mesmo recurso para poder utilizá-lo. Nesta hora que ocorre o problema do controle de disputa.

# Uma das soluções:
# - Exclusão Mútua (Mutex)
# Nunca duas entidades podem estar simultaneamente em suas regiões críticas
# Pode ser implementada com lock/unlock  
# Em python lock.acquire() / lock.release()

import threading
import time

N = 0
lock = threading.Lock()

def worker():
    global N
    print(threading.currentThread().getName(), 'Starting', N)
    lock.acquire() # Início região crítica
    M = N
    print(M)
    time.sleep(1)
    N = M+1
    lock.release()  # Fim região crítica
    #time.sleep(1)
    print(threading.currentThread().getName(), 'Exiting', N)

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        t = threading.Thread(target=worker)                 
        jobs.append(t)
        t.start()
   
    for j in jobs:
        j.join()
  
    print("O valor de N é ", N)    
