import threading
import time

# Esta é a função que cada thread irá executar
def trabalhador(num):   
    # A thread irá esperar por 1 segundo (simulando algum trabalho)
    time.sleep(1)
    # Em seguida, imprimirá uma mensagem indicando o número do trabalhador
    print(f'Eu sou o trabalhador: {num} \n')

# Esta parte verifica se o script está sendo executado diretamente
# e não sendo importado por outro módulo
if __name__ == "__main__":
    
    # Aqui estamos criando 10 threads e iniciando-as
    for i in range(10):
        t = threading.Thread(target=trabalhador, args=(i,))
        t.start()
    
    # A thread principal (a que executa este script) irá esperar por 5 segundos
    # antes de continuar a execução
    time.sleep(5)

    # Após todas as threads terem tido tempo suficiente para executar,
    # a mensagem abaixo será impressa
    print("Thread principal terminou")
