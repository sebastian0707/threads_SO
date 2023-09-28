import threading
import time

# Definindo a variável global 'rodando'
global rodando

# Esta é a função que a thread irá executar
def trabalhador():
    # Esta mensagem é impressa quando a thread começa a executar
    print(f'Eu sou uma thread filha')
    
    # Este é um loop que continua enquanto 'rodando' é True
    while(rodando == True):
        # A thread irá esperar por 2 segundos
        time.sleep(2)
        
        # Este é um cheque de segurança para ter certeza que a thread deve continuar
        if not rodando:
            break
        
        # A cada 2 segundos, a mensagem "to viva" é impressa
        print('to viva')       
        
        # A thread espera por mais 2 segundos
        time.sleep(2)
    
    # Quando o loop termina, esta mensagem é impressa
    print('Fim da thread filha')

# Esta parte verifica se o script está sendo executado diretamente
# e não sendo importado por outro módulo
if __name__ == "__main__":    
    # Aqui estamos criando uma nova thread que irá executar a função 'trabalhador'
    t = threading.Thread(target=trabalhador)
    
    # Iniciando a thread
    rodando = True
    t.start()    
    
    # A thread principal (a que executa este script) irá esperar por 5 segundos
    # antes de continuar a execução
    time.sleep(5)   
    
    # Modificando a variável global 'rodando' para False, sinalizando para a thread
    # 'trabalhador' que ela deve parar
    rodando = False 
    
    # Mensagem indicando que a thread principal terminou
    print('Fim da thread principal')
