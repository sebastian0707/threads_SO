from time import perf_counter

def generate_big_random_sentences(filename, numero_linhas):
    import random
    nouns = ("puppy", "car", "rabbit", "girl", "monkey")  # Lista de substantivos
    verbs = ("runs", "hits", "jumps", "drives", "barfs")  # Lista de verbos
    adj = ("adorable", "clueless", "dirty", "odd", "stupid")  # Lista de adjetivos
    adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.")  # Lista de advérbios

    all = [nouns, verbs, adj, adv]  # Lista de todas as categorias de palavras

    with open(filename, 'w') as f:
        for i in range(numero_linhas):
            # Escolhe aleatoriamente uma palavra de cada categoria e as une em uma frase
            f.writelines([' '.join([random.choice(i) for i in all]), '\n'])
    pass

def gerar_arquivos(numero_aquivos, numero_linhas):
    for i in range(numero_aquivos):
        # Gera um arquivo com um nome formatado e um número especificado de linhas
        generate_big_random_sentences(F'arquivoTeste{i:02}.txt', numero_linhas)

def replace(filename, substr, new_substr):
    print(f'Processando o arquivo {filename}')
    # Obtém o conteúdo do arquivo
    with open(filename, 'r') as f:
        content = f.read()

    # Substitui a substring pela nova substring
    content = content.replace(substr, new_substr)

    # Escreve os dados no arquivo com o sufixo ".alterado.txt"
    with open(filename + '.alterado.txt', 'w') as f:
        f.write(content)

if __name__ == "__main__": 

    numero_aquivos = 2
    numero_linhas = 100
    gerar_arquivos(numero_aquivos, numero_linhas)
            
    start_time = perf_counter() 

    for i in range(numero_aquivos):
        # Substitui a palavra 'car' por 'truck' em cada arquivo gerado
        replace(F'arquivoTeste{i:02}.txt', 'car', 'truck')

    end_time = perf_counter()
    print(f'Levou {end_time - start_time:0.4f} segundos para processar.')
