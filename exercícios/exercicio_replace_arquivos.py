from time import perf_counter

def generate_big_random_sentences(filename,numero_linhas):
    import random
    nouns = ("puppy", "car", "rabbit", "girl", "monkey")
    verbs = ("runs", "hits", "jumps", "drives", "barfs")
    adj = ("adorable", "clueless", "dirty", "odd", "stupid")
    adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.")

    all = [nouns, verbs, adj, adv]

    with open(filename,'w') as f:
        for i in range(numero_linhas):
            f.writelines([' '.join([random.choice(i) for i in all]),'\n'])
    pass
def gerar_arquivos(numero_aquivos,numero_linhas):
    for i in range(numero_aquivos):
        generate_big_random_sentences(F'arquivoTeste{i:02}.txt', numero_linhas)
        
def replace(filename, substr, new_substr):
    print(f'Processing the file {filename}')
    # get the contents of the file
    with open(filename, 'r') as f:
        content = f.read()

    # replace the substr by new_substr
    content = content.replace(substr, new_substr)

    # write data into the file
    with open(filename+'.alterado.txt', 'w') as f:
        f.write(content)

if __name__ == "__main__": 

    numero_aquivos = 10
    numero_linhas = 100
    gerar_arquivos(numero_aquivos,numero_linhas)
            
    start_time = perf_counter() 

    for i in range(numero_aquivos):
        replace(F'arquivoTeste{i:02}.txt', 'car', 'truck')

    end_time = perf_counter()
    print(f'Levou {end_time- start_time: 0.4f} segundos para processar.')