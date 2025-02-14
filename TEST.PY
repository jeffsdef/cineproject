import os

def carregar_catalogo(nome_arquivo):
    catalogo = {}
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as f:
            for linha in f:
                nome, ano, genero = linha.strip().split(',')
                catalogo[nome.strip().upper()] = {'ano': ano.strip(), 'genero': genero.strip()}
    return catalogo

def salvar_catalogo(catalogo, nome_arquivo):
    print('salvando catalogo...')
    with open(nome_arquivo, 'w') as f:
        for nome, detalhes in catalogo.items():
            f.write(f"{nome},{detalhes['ano']},{detalhes['genero']}\n")
    print("Catálogo salvo com sucesso!")

def cadastrar_filme(catalogo):
    nome = input("Digite o nome do filme: ").strip().upper()
    ano = input("Digite o ano do filme: ").strip()
    genero = input("Digite o gênero do filme: ").strip()

    if nome and ano and genero:
        catalogo[nome] = {'ano': ano, 'genero': genero}
        print(f"Filme '{nome}' cadastrado com sucesso!")
    else:
        print("Dados inválidos! Todos os campos devem ser preenchidos.")

def pesquisar_filme(catalogo):
    nome = input("Digite o nome do filme para pesquisa: ").strip().upper()
    if nome in catalogo:
        print(f"Filme encontrado: {nome} ({catalogo[nome]['ano']}) - Gênero: {catalogo[nome]['genero']}")
    else:
        print(f"Filme '{nome}' não encontrado no catálogo.")

def exibir_catalogo(catalogo):
    if catalogo:
        print("\nCatálogo de Filmes:")
        for nome, detalhes in catalogo.items():
            print(f"{nome} ({detalhes['ano']}) - Gênero: {detalhes['genero']}")
    else:
        print("O catálogo está vazio.")

def comprar_ingresso(catalogo):
    exibir_catalogo(catalogo)
    nome_filme = input("\nDigite o nome do filme que deseja assistir: ").strip().upper()

    if nome_filme in catalogo:
        nome_cliente = input("Digite seu nome: ").strip().title()
        email_cliente = input("Digite seu e-mail: ").strip().lower()
        
        while True:
            try:
                num_ingressos = int(input("Quantos ingressos deseja comprar? "))
                if num_ingressos > 0:
                    break
                else:
                    print("O número de ingressos deve ser maior que 0.")
            except ValueError:
                print("Digite um número válido.")

        with open("ingressos_vendidos.txt", "a") as f:
            f.write(f"{nome_cliente}, {email_cliente}, {nome_filme}, {num_ingressos}\n")

        print(f"Compra realizada com sucesso! {nome_cliente} comprou {num_ingressos} ingresso(s) para {nome_filme}.")
        print(f"Um comprovante foi enviado para o e-mail: {email_cliente}")
    else:
        print("Filme não encontrado no catálogo.")

def exibir_ingressos_vendidos():
    if os.path.exists("ingressos_vendidos.txt"):
        print("\nIngressos Vendidos:")
        with open("ingressos_vendidos.txt", "r") as f:
            for linha in f:
                nome_cliente, email_cliente, nome_filme, num_ingressos = linha.strip().split(", ")
                print(f"{nome_cliente} ({email_cliente}) comprou {num_ingressos} ingresso(s) para {nome_filme}.")
    else:
        print("Nenhum ingresso vendido até o momento.")

def menu(catalogo):
    while True:
        print("\nMenu de Opções:")
        print("1. Cadastrar Filme")
        print("2. Exibir Catálogo de Filmes da CineXP")
        print("3. Pesquisar Filmes do catálogo da CineXP")
        print("4. Comprar Ingresso")
        print("5. Exibir Ingressos Vendidos")
        print("6. Salvar Catálogo")
        print("7. Sair")

        opcao = input("Escolha uma opção (1-7): ")

        if opcao == '1':
            cadastrar_filme(catalogo)
        elif opcao == '2':
            exibir_catalogo(catalogo)
        elif opcao == '3':
            pesquisar_filme(catalogo)
        elif opcao == '4':
            comprar_ingresso(catalogo)
        elif opcao == '5':
            exibir_ingressos_vendidos()
        elif opcao == '6':
            salvar_catalogo(catalogo, 'catalogo_filmes.txt')
        elif opcao == '7':
            salvar_catalogo(catalogo, 'catalogo_filmes.txt')
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

catalogo = carregar_catalogo('catalogo_filmes.txt')

menu(catalogo)

