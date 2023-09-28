
def inicializacaoFixa(linhas, colunas):
    matriz = [ [i+j*colunas for i in range(colunas)] for j in range(linhas)]
    return matriz

def inicializacao(linhas, colunas, valor):
    matriz = [ [valor for i in range(colunas)] for j in range(linhas)]
    return matriz    

def printMAtriz(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], ' ', end='')

        print('')   
    print()   

def multMatriz(mA, mB):
    result = inicializacao(len(mA),len(mB[0]),0)  

    for i in range(len(result)):
        for j in range(len(result[0])):
            for k in range(len(mA[0])):
                    #print(i,j,k)
                    result[i][j] += mA[i][k] * mB[k][j]
    return result

if __name__ == "__main__":   
    mA = inicializacaoFixa(2,3)
    mB = inicializacaoFixa(3,4)

    print("Matriz A")
    printMAtriz(mA)

    print("Matriz B")
    printMAtriz(mB)

    mC = multMatriz(mA,mB)

    print("Matriz C")
    printMAtriz(mC )

 