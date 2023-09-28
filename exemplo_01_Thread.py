import threading
import time

def trabalhador(num):   
    time.sleep(1)
    print(f'Eu sou o trabalhador: {num} \n')

if __name__ == "__main__":
    
    for i in range(10):
        t = threading.Thread(target=trabalhador, args=(i,))
        t.start()
    
    time.sleep(5)

   
    print("Thread principal terminou")
    
    
    
    
    
    
    
    #t = threading.Thread(target=trabalhador, args=(42,))
    #t.start()
    
    #for i in range(5):
    #    t = threading.Thread(target=trabalhador, args=(i,))
    #    t.start()

   