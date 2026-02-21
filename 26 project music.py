import json

ARQUIVO = "musicas.json"    #cria um arquivo p/ salvar todas as musicas
ARQUIVO_ARTISTAS = "artistas.json"  #cria um arquivo p/ salvar os artistas e suas médias de avaliação

#FUNÇOES P/ GERENCIAR OS ARTISTAS 
def carregar_artistas():
    try:
        with open(ARQUIVO_ARTISTAS, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
            return []


def salvar_artistas(artistas):
    with open(ARQUIVO_ARTISTAS, "w") as f:
        json.dump(artistas, f, indent=4)


def adicionar_artista(artistas):
    nome = input("Nome do artista: ")
    if "5" in nome:
        print("Cancelando operaçao...")
        return
    
    genero = input("Gênero: ")
    if "5" in genero:
        print("Cancelando operaçao...")
        return
    
    biografia = input("Biografia: ")
    if "5" in biografia:
        print("Cancelando operaçao...")
        return
    
    ano_inicio = input("Ano de início: ")
    if "5" in ano_inicio:
        print("Cancelando operaçao...")
        return
    
    artista = {
        "nome": nome,
        "genero": genero,
        "biografia": biografia,
        "ano_inicio": ano_inicio
    }

    artistas.append(artista)
    salvar_artistas(artistas)
    print("Artista adicionado com sucesso!")

def pesquisar_artista_info(artistas):
    nome = input("Digite o nome do artista: ").lower()
    if "5" in nome:
        print("Cancelando operaçao...")
        return
    
    encontrados = [
        a for a in artistas
        if nome in a["nome"].lower()
    ]

    if encontrados:
        for a in encontrados:
            print("\n---")
            print("Nome:", a["nome"])
            print("Gênero:", a["genero"])
            print("Ano de início:", a["ano_inicio"])
            print("Biografia:", a["biografia"])
    else:
        print("Artista não encontrado.")


    #FUNÇOES P/ GERENCIAR AS MUSICAS
def carregar_musicas():
   try:
        with open(ARQUIVO, "r") as var: #abre o arquivo para leitura
            return json.load(var)
   except (FileNotFoundError, json.JSONDecodeError): 
        return []

def salvar_musicas(musicas):
    with open(ARQUIVO, "w") as var:  #abre o arquivo para escrita
        json.dump(musicas, var, indent=4)  #salva a lista de musicas no arquivo em formato json       

def adicionar_musica(musicas):
         
        nome = input("Nome da música: ")
        if "5" in nome:
            print("Cancelando operaçao...")
            return
        artista = input("Artista: ")
        if "5" in artista:
            print("Cancelando operaçao...")
            return
        nota = input("Nota (0-5): ")
        if "5" in nota:
            print("Cancelando operaçao...")
            return
        comentario = input("Comentário: ")
        if "5" in comentario:
            print("Cancelando operaçao...")
            return
        genero = input("Gênero: ").strip()
        if "5" in genero:
            print("Cancelando operaçao...")
            return

        if genero == "":
            genero = "Não identificado"

        musica = {
            "nome": nome,
            "artista": artista,
            "nota": nota,
            "comentario": comentario,
            "genero": genero
        }

        musicas.append(musica)
        salvar_musicas(musicas)
        print("Música adicionada com sucesso!")

def pesquisa(musicas):
    print("\n1 - Filtrar por nome")
    print("2 - Filtrar por artista")
    print("3 - Filtrar por gênero")
    print("4 - Filtrar por nota")

    escolha = input("Escolha: ")

    if escolha == "1":
        termo = input("Nome da música: ").lower()
        resultados = [m for m in musicas if termo in m["nome"].lower()]

    elif escolha == "2":
        termo = input("Nome do artista: ").lower()
        resultados = [m for m in musicas if termo in m["artista"].lower()]

    elif escolha == "3":
        termo = input("Gênero: ").lower()
        resultados = [m for m in musicas if termo in m["genero"].lower()]

    elif escolha == "4":
        try:
            termo = int(input("Nota (0-5): "))
            resultados = [m for m in musicas if m["nota"] == termo]
        except ValueError:
            print("Nota inválida.")
            return
        
    elif escolha == "5":
        print("Cancelando pesquisa...")
        return

    else:
        print("Opção inválida.")
        return

    if resultados:
        for m in resultados:
            print("\n---")
            print("Nome:", m["nome"])
            print("Artista:", m["artista"])
            print("Gênero:", m.get("genero", "Não identificado"))
            print("Nota:", m["nota"])
            print("Comentário:", m["comentario"])
    else:
        print("Nenhuma música encontrada.")


    def media_artista(musicas, artista):
        notas = [m["nota"] for m in musicas if m["artista"]. lower() == artista.lower()]
        if notas:
             media = sum(notas) / len(notas)
             return None
        
    def filtrar_por_artista(musicas, artista):  
        artista_busca = input("Digite o nome do artista: ").lower()  

        resultados= [
            m for m in musicas
            if artista_busca in m["artista"].lower()
        ]  

        if resultados:
            print(f"\nMúsicas do artista '{artista_busca}':") 
            for m in resultados:
                print("\n---")
                print("Nome:", m["nome"])
                print("Artista:", m["artista"])
                print("Nota:", m["nota"])
                print("Comentário:", m["comentario"])
                print("Gênero:", m.get("genero", "Não identificado"))

            media = media_artista(musicas, artista_busca)

            if media is not None:
                 print(f"\nMédia de avaluações para '{artista_busca}': {media:.2f}")
            else:
                 print("Nenhuma música encontrada.")

def deletar_musica():
    nome = input("Digite o nome da música a ser deletada: ").lower()
    if "5" in nome:
        print("Cancelando operaçao...")
        return

    musicas = carregar_musicas()
    musicas_filtradas = [m for m in musicas if nome not in m["nome"].lower()]

    if len(musicas_filtradas) < len(musicas):
        salvar_musicas(musicas_filtradas)
        print("Música deletada com sucesso!")
    else:
        print("Música não encontrada.")

def deletar_artista():
    nome = input("Digite o nome do artista a ser deletado: ").lower()
    if "5" in nome:
        print("Cancelando operaçao...")
        return

    artistas = carregar_artistas()
    artistas_filtrados = [a for a in artistas if nome not in a["nome"].lower()]

    if len(artistas_filtrados) < len(artistas):
        salvar_artistas(artistas_filtrados)
        print("Artista deletado com sucesso!")
    else:
        print("Artista não encontrado.")

def deletar():
    print("\n1 - Deletar música")
    print("2 - Voltar")
    print("3 - Deletar artista")
    escolha = input("Escolha: ")
    if escolha == "1":
         deletar_musica()
    elif escolha == "2":
         return
    elif escolha == "3":
        deletar_artista()

def main():
    musicas = carregar_musicas()
    artistas = carregar_artistas()

    while True:
        print("\n1 - Adicionar música")
        print("2 - Adicionar artista")
        print("3 - Pesquisar músicas")
        print("4 - Pesquisar artista")
        print("5 - Sair")
        print("6 - Deletar música ou artista")

        escolha = input("Escolha: ")

        if escolha == "1":
            adicionar_musica(musicas)
        elif escolha == "2":
            adicionar_artista(artistas)
        elif escolha == "3":
            pesquisa(musicas)
        elif escolha == "4":
            pesquisar_artista_info(artistas)
        elif escolha == "5":
            break
        elif escolha == "6":
            deletar()
        else:
            print("Opção inválida.")
main()

     

