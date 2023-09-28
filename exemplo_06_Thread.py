import threading
import time
import random

def trabalhador(tempo,nome):
    print(f'Eu sou uma thread filha: {nome} tempo:{tempo}')
    time.sleep(tempo)
    print(f'Fim da thread filha: {nome} tempo:{tempo}')
     
if __name__ == "__main__":    
    jobs = []    
    n = int(input("Quantas threads ? ")) 

    for i in range(n):
        randTempo = random.randint(1,20)
        t = threading.Thread(target=trabalhador,
                             args=(randTempo,f'Thread_{i}'))
        #t.setDaemon(True)
        jobs.append(t)
    
    # start das Threads
    for j in jobs:
        j.start()
              
    time.sleep(5)
   
    for j in jobs:
        j.join()

    print('Fim da thread principal')