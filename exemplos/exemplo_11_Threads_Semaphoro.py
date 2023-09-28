# Sincronização utilizando Semáforo 
# Quando usamos Exclusão Mútua (Mutex), em Python  lock.acquire() / lock.release(),
#   apenas uma Thread pode ser executadoa mas às vezes nosso requisito é executar 
#   um determinado número de Threads por vez.   

# Suponha que tenhamos que permitir que 10 membros acessem o banco de dados por vez e 
#   apenas 4 membros tenham permissão para acessar a conexão de rede. 
# Para lidar com esses tipos de requisitos, não podemos usar o conceito de 
#   lock.acquire() / lock.release(),  devemos usar o Semáforo (Semaphore). 
# O semáforo pode ser usado para limitar o acesso aos  recursos compartilhados 
#   com capacidade limitada.

# Para usar crie um objeto de Semaphore: 
# object_name = Semáforo (contagem)
# 'contagem' é o número de Threads permitidos para acessar simultaneamente. O valor padrão de contagem é 1.
# Quando umq Thread executa o método de acquire(), então o valor da variável “count” será decrementado em 1 
#   e sempre que um Thread executa o método release() então o valor da variável “count” será incrementado em 1. 


import threading
import time

# Criando um semáforo com uma contagem máxima de 3 threads permitidas simultaneamente
semaforo = threading.Semaphore(3)       

# Função que será executada por cada thread
def display(name):             
    semaforo.acquire()  # A thread adquire o semáforo (entra na região crítica)
    
    for i in range(2): 
        print('Olá, ', end = '') 
        time.sleep(1) 
        print(name) 
        
    semaforo.release()  # A thread libera o semáforo (sai da região crítica)

if __name__ == '__main__':            
    jobs = []  # Lista para armazenar as threads
    
    n = 15  # Número de threads a serem criadas
    
    # Criando e iniciando as threads
    for i in range(n):     
        t = threading.Thread(target=display, args=(f'Thread_{i}',))
        jobs.append(t)
        
    for j in jobs:
        j.start()
