from threading import *
import time
  
class Mythread(Thread): 
      
    def run(self): 
        # Este loop irá executar 10 vezes
        for i in range(10): 
            # A cada iteração, imprime uma mensagem indicando a iteração
            print('Child Thread: ', i) 
            # A thread irá esperar por 2 segundos
            time.sleep(2)

        # Quando o loop termina, imprime "Fim da thread filha"
        print('Fim da thread filha')
                
# Criando uma instância da classe Mythread
t = Mythread() 

# Definindo a thread como um daemon
t.setDaemon(True) 

# Iniciando a thread
t.start() 

# Este loop na thread principal irá executar 10 vezes
for i in range(10): 
    # A cada iteração, imprime uma mensagem indicando a iteração
    print('Main Thread: ', i) 
    # A thread principal irá esperar por 1 segundo
    time.sleep(1)

# Quando o loop termina, imprime "Esperando..."
print("Esperando...")

# O .join simplesmente pausa a thread atual (de onde ele foi chamado) até que 
# a thread alvo (a thread a que ele está atrelado, neste caso, 't') termine.
t.join()

# Após a thread 't' terminar, imprime "Fim!"
print('Fim!') 
