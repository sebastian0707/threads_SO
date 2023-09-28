import threading
import time

global rodando

def trabalhador():
    print(f'Eu sou uma thread filha')
    while(rodando == True):
        time.sleep(2)
        if not rodando:
            break
        print('to viva')       
        time.sleep(2)
    print('Fim da thread filha')
        
if __name__ == "__main__":    
    t = threading.Thread(target=trabalhador)    
    rodando = True
    t.start()    
    time.sleep(5)   
    rodando = False 
    print('Fim da thread principal')