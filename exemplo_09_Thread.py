import threading
import time

N = 0

def worker():
    global N
    print(threading.currentThread().getName(), 'Starting', N)
    M = N
    print(M)
    time.sleep(1)
    N = M+1    
    print(threading.currentThread().getName(), 'Exiting', N)

if __name__ == '__main__':
    jobs = [] 
    for i in range(5):
        t = threading.Thread(target=worker)  
        jobs.append(t)  
        t.start()       
          
    for j in jobs:
        j.join()
  
    print("O valor de N é ", N)    