# Passa a Bola - Simulador de Gestão do Futebol Feminino

# Dados iniciais (Pode ser substituído por um banco de dados real)

import json

def pega_dados():
    with open('pb.json') as f:
        dados = json.load(f)
    return dados
dados = pega_dados()
    
for atleta in dados["dados"]["atletas"]:
    for clube in dados['dados']['clubes']:
        if atleta["clube"] == clube["nome"]:
            clube["atletas"].append(atleta["nome"])

# -------- Funções auxiliares --------
def read_non_empty(prompt):
    # Força o usuário a digitar algo que não seja vazio ou numérico
    while True:
        value = input(prompt).strip()
        if not value:
            print("Entrada inválida! Este campo deve ser preenchido.")
            continue
        try:
            float(value)
            print("Entrada inválida! Este campo não pode ser numérico.")
        except ValueError:
            return value
       
def read_positive_int(prompt):
     # Força o usuário a digitar um número positivo
    while True:
        try:    
            valor = int(input(prompt))
            if valor < 0:
                print("Entrada inválida. Digite um número positivo.")
            else:
                return valor
        except ValueError:      
            print("Entrada inválida. Digite um número positivo.")
         
 
def select_option(options, prompt, allow_blank=False):
    # Força o usuário a escolher uma opção válida de uma lista
    for idx, opt in enumerate(options, start=1):
        print(f"{idx} - {opt}")
    if allow_blank:
        print("0 - Não especificar")

    choice = input(prompt).strip()
    
    while True:
        try:
            choice = input(prompt).strip()
            if choice.isnumeric() or int(choice) not in range(1, len(options)+1):
                continue
        except ValueError:
            print("Opção inválida, digite apeas números.")
        

        if allow_blank and choice == "0":
            return ""
        
        return options[int(choice) - 1]
    

 
# -------- Funcionalidades --------
def cadastrar_atleta():
    nome = read_non_empty("Digite o nome da atleta: ")
    idade = read_positive_int("Digite a idade da atleta: ")
    print("\nEscolha a posição da atleta:")
    posicao = select_option(dados["dados"]["POSITIONS"], "Digite o número da posição: ")
    print("\nEscolha o clube da atleta:")
    nomes_clubes = [c["nome"] for c in dados["dados"]["clubes"]]
    clube = select_option(nomes_clubes, "Digite o número do clube: ")

    atleta = {"nome": nome, "idade": idade, "posicao": posicao, "clube": clube}
    dados["dados"]["atletas"].append(atleta)
    # Adiciona atleta ao clube
    for c in dados["dados"]["clubes"]:
        if c["nome"] == clube:
            c["atletas"].append(nome)

    print(f"✅ Atleta {nome} cadastrada com sucesso!\n")

def cadastrar_clube():
    # Cadastrar novo clube
    nome = read_non_empty("Digite o nome do clube: ")
    cidade = read_non_empty("Digite a cidade do clube: ")
    dados["dados"]["clubes"].append({"nome": nome, "cidade": cidade, "atletas": []})
    print(f"✅ Clube {nome} cadastrado com sucesso!\n")

def registrar_partida():
    # Registrar nova partida
    nomes_clubes = [c["nome"] for c in dados["dados"]["clubes"]]
    clubeA = select_option(nomes_clubes, "Escolha o Clube A: ")
    clubeB = select_option(nomes_clubes, "Escolha o Clube B: ")
    placarA = read_positive_int(f"Quantos gols o {clubeA} marcou? ")
    placarB = read_positive_int(f"Quantos gols o {clubeB} marcou? ")
    dados["dados"]["partidas"].append({"clubeA": clubeA, "clubeB": clubeB, "placar": f"{placarA} x {placarB}"})
    print("✅ Partida registrada com sucesso!\n")

def listar_atletas():
    # Listar todas as atletas
    if not dados["dados"]["atletas"]:
        print("Nenhuma atleta cadastrada ainda.\n")
    else:
        print("\n📋 Lista de Atletas:")
        for a in dados["dados"]["atletas"]:
            print(f"- {a['nome']} ({a['posicao']}, {a['idade']} anos) - Clube: {a['clube']}")
        print("")

def listar_clubes():
    # Listar todos os clubes
    if not dados["dados"]["clubes"]:
        print("Nenhum clube cadastrado ainda.\n")
    else:
        print("\n📋 Lista de Clubes:")
        for c in dados ["dados"]["clubes"]:
            print(f"- {c['nome']} ({c['cidade']}) - {len(c['atletas'])} atletas")
        print("")

def listar_partidas():
    # Listar todas as partidas
    if not dados["dados"]["partidas"]:
        print("Nenhuma partida registrada ainda.\n")
    else:
        print("\n📋 Lista de Partidas:")
        for p in dados["dados"]["partidas"]:
            print(f"- {p['clubeA']} vs {p['clubeB']} - Placar: {p['placar']}")
        print("")

# -------- Menu --------
def menu():
        opcoes = {
            "1": cadastrar_atleta,
            "2": cadastrar_clube,
            "3": registrar_partida,
            "4": listar_atletas,
            "5": listar_clubes,
            "6": listar_partidas,
        }
        while True:
            print("⚽ Bem-vindo ao sistema Passa a Bola ⚽\n1 - Cadastrar Atleta\n2 - Cadastrar Clube\n3 - Registrar Partida\n4 - Listar Atletas\n5 - Listar Clubes\n6 - Listar Partidas\n7 - Sair")
            opcao = input("Escolha uma opção: ").strip()
            if opcao == "7":
                print("👋 Saindo do sistema... Até logo!")
                break
                
            elif opcao in opcoes:
                opcoes[opcao]()
            else:
                print("❌ Opção inválida, tente novamente.\n")

menu()