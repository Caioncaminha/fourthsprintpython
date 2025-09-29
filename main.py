# Passa a Bola - Simulador de Gestão do Futebol Feminino

"""Pequeno gerenciador em memória baseado no arquivo `pb.json`.

Notas:
- Não adicionamos novas funções públicas além das já existentes; as
  funções foram apenas tornadas mais robustas e comentadas.
"""

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
    """Lê uma string não vazia e que não seja apenas numérica.

    Continua pedindo até receber uma entrada válida.
    """
    while True:
        value = input(prompt).strip()
        if not value:
            print("Entrada inválida! Este campo deve ser preenchido.")
            continue
        # Rejeita entradas que sejam apenas números (inteiras ou com
        # ponto/vírgula). Tenta converter para float; se conseguir,
        # considera numérico e pede novamente.
        try:
            float(value.replace(',', '.'))
            print("Entrada inválida! Este campo não pode ser numérico.")
            continue
        except ValueError:
            return value
       
def read_positive_int(prompt):
    """Lê um inteiro não-negativo do usuário.

    Continua pedindo até que o usuário digite um inteiro >= 0.
    """
    while True:
        val = input(prompt).strip()
        try:
            valor = int(val)
            if valor < 0:
                print("Entrada inválida. Digite um número inteiro não-negativo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número inteiro não-negativo.")
         
 
def select_option(options, prompt, allow_blank=False):
    """Apresenta uma lista numerada e retorna a opção escolhida.

    Se `allow_blank` for True, o usuário pode digitar '0' para retornar
    uma string vazia. A função valida a entrada e repete o prompt em
    caso de valores inválidos.
    """
    for idx, opt in enumerate(options, start=1):
        print(f"{idx} - {opt}")
    if allow_blank:
        print("0 - Não especificar")

    while True:
        choice = input(prompt).strip()
        if allow_blank and choice == '0':
            return ""
        if not choice.isdigit():
            print("Opção inválida, digite apenas o número da opção.")
            continue
        idx = int(choice)
        if 1 <= idx <= len(options):
            return options[idx - 1]
        print(f"Opção inválida: escolha entre 1 e {len(options)}.")
    

 
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
    """Registra uma nova partida entre dois clubes.

    Garante que Clube A e Clube B sejam diferentes.
    """
    nomes_clubes = [c['nome'] for c in dados['dados']['clubes']]
    clubeA = select_option(nomes_clubes, "Escolha o Clube A: ")
    while True:
        clubeB = select_option(nomes_clubes, "Escolha o Clube B: ")
        if clubeB == clubeA:
            print("Um clube não pode jogar contra ele mesmo. Escolha outro clube.")
            continue
        break

    placarA = read_positive_int(f"Quantos gols o {clubeA} marcou? ")
    placarB = read_positive_int(f"Quantos gols o {clubeB} marcou? ")
    dados['dados']['partidas'].append({
        "clubeA": clubeA,
        "clubeB": clubeB,
        "placar": f"{placarA} x {placarB}"
    })
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