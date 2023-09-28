import threading
import time

def trabalhador():
    print(f'Eu sou uma thread filha')
    for i in range(10): 
        time.sleep(1)
        print('to viva')

    print('Fim da thread filha')
        
if __name__ == "__main__":    
    t = threading.Thread(target=trabalhador)
    t.start()    
    time.sleep(1)
