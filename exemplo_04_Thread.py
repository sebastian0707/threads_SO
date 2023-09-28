from threading import *
import time
  
class Mythread(Thread): 
  
    def run(self): 
        for i in range(10): 
            print('Child Thread: ',i) 
            time.sleep(2)
        print('Fim da thread filha')
   
if __name__ == "__main__":              
    t = Mythread() 
    #t.setDaemon(True) 
    t.start() 
    #t.run()
    for i in range(10): 
        print('Main Thread: ',i) 
        time.sleep(1)
    print('Fim!') 

# Daemon threads são interrompidas quando a thread principal
# termina de executar e o programa termina.

# Os daemons são úteis apenas quando o programa principal está em execução, 
# e não há problema em eliminá-los assim que os outros threads não-daemon forem encerrados. 
# Sem threads daemon, temos que gerenciá-las e dizer-lhes para sair, antes que nosso programa 
# possa sair completamente. 
# Ao defini-las como threads daemon, podemos deixá-las rodar e esquecê-las, e quando nosso programa
# é encerrado, qualquer thread daemon é morta automaticamente.