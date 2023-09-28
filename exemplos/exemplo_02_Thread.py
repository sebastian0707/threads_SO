import threading
import time

# Esta é a função que a thread irá executar
def trabalhador():
    # Esta mensagem é impressa quando a thread começa a executar
    print(f'Eu sou uma thread filha')
    
    # Este loop irá executar 10 vezes
    for i in range(10): 
        # A thread irá esperar por 1 segundo a cada iteração
        time.sleep(1)
        # A cada segundo, a mensagem "to viva" será impressa
        print('to viva')

    # Após o loop terminar, esta mensagem será impressa
    print('Fim da thread filha')
        
# Esta parte verifica se o script está sendo executado diretamente
# e não sendo importado por outro módulo
if __name__ == "__main__":    
    # Aqui estamos criando uma nova thread que irá executar a função trabalhador
    t = threading.Thread(target=trabalhador)
    
    # Iniciando a thread
    t.start()    

    # A thread principal (a que executa este script) irá esperar por 1 segundo
    # antes de continuar a execução
    time.sleep(1)
