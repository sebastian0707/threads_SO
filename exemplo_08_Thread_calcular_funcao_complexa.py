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

def expo(x):
    #print('Thread: expo')
    global resp_expo
    resp_expo = 0
    time.sleep(5)
    resp_expo = x ** 2

def mult(x):
    #print('Thread: mult')
    global resp_mult
    resp_mult = 0
    time.sleep(6)
    resp_mult = 3 * x

def seno(x):
    #print('Thread: seno')
    global resp_seno
    resp_seno = 0
    time.sleep(7)
    resp_seno = sin(x)

if __name__ == '__main__':
    x = 5

    thread1 = threading.Thread(target=expo, args=(x,))
    thread2 = threading.Thread(target=mult, args=(x,))
    thread3 = threading.Thread(target=seno, args=(x,))

    thread1.start()
    thread2.start()
    thread3.start()
    
    thread1.join()
    thread2.join()
    thread3.join()

    fx = resp_expo + resp_mult + resp_seno
    print('Equação f(x) = x^2 + 3*x + sen(x)')
    print(f'Resultado para x = {x}: {fx}')