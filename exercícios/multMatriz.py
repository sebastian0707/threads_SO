def inicializacaoFixa(linhas, colunas):
    """
    Inicializa uma matriz com valores fixos, onde os elementos são sequenciais
    a partir de 0 e incrementados de acordo com o número de colunas.

    Args:
        linhas (int): Número de linhas da matriz.
        colunas (int): Número de colunas da matriz.

    Returns:
        list: Matriz inicializada.
    """
    matriz = [ [i+j*colunas for i in range(colunas)] for j in range(linhas)]
    return matriz

def inicializacao(linhas, colunas, valor):
    """
    Inicializa uma matriz com um valor específico.

    Args:
        linhas (int): Número de linhas da matriz.
        colunas (int): Número de colunas da matriz.
        valor: Valor com o qual a matriz será preenchida.

    Returns:
        list: Matriz inicializada.
    """
    matriz = [ [valor for i in range(colunas)] for j in range(linhas)]
    return matriz    

def printMatriz(mat):
    """
    Imprime uma matriz na tela.

    Args:
        mat (list): Matriz a ser impressa.
    """
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], ' ', end='')

        print('')   
    print()   

def multMatriz(mA, mB):
    """
    Multiplica duas matrizes.

    Args:
        mA (list): Matriz A.
        mB (list): Matriz B.

    Returns:
        list: Matriz resultante da multiplicação.
    """
    result = inicializacao(len(mA), len(mB[0]), 0)  

    for i in range(len(result)):
        for j in range(len(result[0])):
            for k in range(len(mA[0])):
                result[i][j] += mA[i][k] * mB[k][j]
    return result

if __name__ == "__main__":   
    mA = inicializacaoFixa(2,3)
    mB = inicializacaoFixa(3,4)

    print("Matriz A")
    printMatriz(mA)

    print("Matriz B")
    printMatriz(mB)

    mC = multMatriz(mA,mB)

    print("Matriz C")
    printMatriz(mC)
