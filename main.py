import os
import random
import time

mapasTxt = "NomeArquivo.txt"

mapas = [
    "MP001",
    "MP003",
    "MP007",
    "MP011",
    "MP012",
    "MP013",
    "MP017",
    "MP018",
    "MP_Subway"
]

modos_jogo = [
    "ConquestLarge0",
    "ConquestSmall0",
    "Domination0",
    "squadDeathMatch0",
    "TeamDeathMatch0",
    "RushLarge0",
    "ConquestAssaultLarge0",
    "ConquestAssaultSmall0"
]

def reconhece_path():
    #Verificar se o arquivo existe e se não está vazio
    if os.path.exists("path.txt") and os.path.getsize("path.txt") != 0: 
        return
    else:
        print("\nInforme o caminho do arquivo dentro do VC\n")
        path = input("Caminho: ") ###verificar se passar o nome do arquivo junto deve ser retornado sem erro
        caminho = rf"{path}\{mapasTxt}"

        with open("path.txt", "w") as arquivo:
            arquivo.write(caminho)
        print("Caminho Salvo...")
        print("\nQualquer alteração no caminho deve ser trocada no arquivo path.txt\n")
        time.sleep(2)
        pause = input("Pressione qualquer tecla para continuar...")

        if not os.path.exists(caminho):
            print("Arquivo não encontrado, verifique caminho se encontra certo")
            reconhece_path()

    return

def gerar_mapa():
    #Gera indices aleatorios para listas, retornando um mapa e um modo de jogo aleatorio
    mapa_aleatorio = random.choice(mapas)
    modos_jogo_aleatorio = random.choice(modos_jogo)

    sentença = f"{mapa_aleatorio} {modos_jogo_aleatorio} 1"

    with open(path_arquivo_mapas, "r") as arquivo: #Ler o arquivo para verificar se o mapa já existe
        conteudo = arquivo.read()

    if mapa_aleatorio in conteudo: #Se o mapa já existe, gerar outro, porem o modo de jogo pode-se repetir
        return gerar_mapa()
    else:
        return sentença
    

reconhece_path() #verificar se o arquivo existe ou cria-lo

#Lê o caminho que foi salvo no path.txt
with open("path.txt", "r") as arquivo: 
    path_arquivo_mapas = arquivo.read()

# Deixar o arquivo em branco antes de escrever novos dados
with open(path_arquivo_mapas, "w") as arquivo:
    pass

# Escrever novas linhas no final do arquivo
for i in range(6):
    mapa_gerado = gerar_mapa()

    with open(path_arquivo_mapas, "a") as arquivo:  # Modo de adição 'a'
        arquivo.write(mapa_gerado + "\n")