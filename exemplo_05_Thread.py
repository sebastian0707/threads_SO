from threading import *
import time
  
class Mythread(Thread): 
      
    def run(self): 
        for i in range(10): 
            print('Child Thread: ',i) 
            time.sleep(2)

        print('Fim da thread filha')
                
t = Mythread() 
t.setDaemon(True) 
t.start() 
for i in range(10): 
    print('Main Thread: ',i) 
    time.sleep(1)

print("Esperando...")
t.join()
print('Fim!') 

# Uma thread pode ser unida (join) em Python chamando o método Thread.join(). 
# Isso tem o efeito de bloquear o thread atual até que a thread de destino que 
# foi associada seja encerrado.

# O .join simplesmente pausa a thread atual (de onde ele foi chamado) até que 
# a thread alvo (a thread a que ele está atrelado) termine.