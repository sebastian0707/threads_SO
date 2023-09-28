# f(x) = x^2 + 3*x + sen(x)
# Perceba que cada parte da equação (x^2, 3*x, sen(x))
# poderia ser calculada e depois somada no final para obter o
# resultado final. Imagine então que em vez de um cálculo simples,
# fosse algo mais complexo e que pudéssemos entregar
# cada parte deste cálculo a uma pessoa diferente. Vamos então
# imaginar que cada pessoa seja uma thread e que cada uma fará
# sua parte no cálculo da equação em separado para, no final,
# alguém só fazer o “fácil" trabalho de somar os resultados.

import threading
from math import sin
import time

# Definindo funções que calculam partes da equação
def expo(x):
    #print('Thread: expo')
    global resp_expo
    resp_expo = x ** 2

def mult(x):
    #print('Thread: mult')
    global resp_mult
    resp_mult = 3 * x

def seno(x):
     #print('Thread: seno')    
    global resp_seno
    resp_seno = sin(x)

if __name__ == '__main__':
    x = 5

    # Criando três threads, cada uma responsável por um cálculo específico
    thread1 = threading.Thread(target=expo, args=(x,))
    thread2 = threading.Thread(target=mult, args=(x,))
    thread3 = threading.Thread(target=seno, args=(x,))
   
    # Iniciando as threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Esperando que todas as threads terminem
    thread1.join()
    thread2.join()
    thread3.join()

    # Somando os resultados dos cálculos
    fx = resp_expo + resp_mult + resp_seno

    # Imprimindo a equação e o resultado
    print('Equação f(x) = x^2 + 3*x + sen(x)')
    print(f'Resultado para x = {x}: {fx}')
