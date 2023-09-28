from threading import *
import time
  
# Criando uma classe que herda de Thread
class Mythread(Thread): 
  
    # Sobrescrevendo o método run() que será executado quando a thread iniciar
    def run(self): 
        # Este loop irá executar 10 vezes
        for i in range(10): 
            # A cada iteração, imprime uma mensagem indicando a iteração
            print('Child Thread: ', i) 
            # A thread irá esperar por 2 segundos
            time.sleep(2)
        # Quando o loop termina, imprime "Fim da thread filha"
        print('Fim da thread filha')
   
if __name__ == "__main__":              
    # Criando uma instância da classe Mythread
    t = Mythread() 
    # Iniciando a thread
    t.start() 
    
    # Este loop na thread principal irá executar 10 vezes
    for i in range(10): 
        # A cada iteração, imprime uma mensagem indicando a iteração
        print('Main Thread: ', i) 
        # A thread principal irá esperar por 1 segundo
        time.sleep(1)
    
    # Quando o loop termina, imprime "Fim!"
    print('Fim!') 

# Daemon threads são interrompidas quando a thread principal
# termina de executar e o programa termina.

# Os daemons são úteis apenas quando o programa principal está em execução, 
# e não há problema em eliminá-los assim que os outros threads não-daemon forem encerrados. 
# Sem threads daemon, temos que gerenciá-las e dizer-lhes para sair, antes que nosso programa 
# possa sair completamente. 
# Ao defini-las como threads daemon, podemos deixá-las rodar e esquecê-las, e quando nosso programa
# é encerrado, qualquer thread daemon é morta automaticamente.
