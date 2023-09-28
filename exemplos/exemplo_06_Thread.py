import threading
import time
import random

# Esta é a função que cada thread irá executar
def trabalhador(tempo, nome):
    # A thread imprime uma mensagem indicando o nome e o tempo
    print(f'Eu sou uma thread filha: {nome} tempo:{tempo}')
    # A thread espera pelo tempo especificado
    time.sleep(tempo)
    # Após a espera, a thread imprime uma mensagem indicando o nome e o tempo novamente
    print(f'Fim da thread filha: {nome} tempo:{tempo}')
     
if __name__ == "__main__":    
    jobs = []    
    # O usuário informa quantas threads ele quer criar
    n = int(input("Quantas threads ? ")) 

    # Para o número de threads especificado pelo usuário
    for i in range(n):
        # Gera um tempo aleatório entre 1 e 20 segundos
        randTempo = random.randint(1, 20)
        
        # Cria uma nova thread, atribuindo a função trabalhador e passando argumentos tempo e nome
        t = threading.Thread(target=trabalhador, args=(randTempo, f'Thread_{i}'))
        
        # Adiciona a nova thread à lista de jobs
        jobs.append(t)
    
    # Inicia cada uma das threads
    for j in jobs:
        j.start()
              
    # A thread principal aguarda por 5 segundos
    time.sleep(5)
   
    # A thread principal espera que todas as threads filhas terminem usando o método join
    for j in jobs:
        j.join()

    # Quando todas as threads terminam, a mensagem abaixo é impressa
    print('Fim da thread principal')
