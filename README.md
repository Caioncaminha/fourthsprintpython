# Computational Thinking with Python - Sprint 4 (Passa a Bola)

## 🧠1. Descrição

Simulador CLI em Python que gerencia um cadastro simples de atletas, clubes e partidas para a disciplina de Python no contexto do projeto Passa a Bola.

O código principal está em `main.py` e carrega os dados iniciais de `pb.json` ao iniciar.

## 🛠️2. Tecnologias

- Linguagem: Python (compatível com Python 3.x)
- Dependências: nenhuma biblioteca externa
- Persistência atual: arquivo JSON (`pb.json`) lido em memória no início; o programa não regrava alterações nesse arquivo automaticamente

## 🎲3. Modelo de dados (formato em `pb.json`)

Os dados estão agrupados sob a chave `dados` e usam as seguintes estruturas:

- `POSITIONS`: lista de posições permitidas (ex.: "Goleira", "Zagueira", ...)
- `clubes`: lista de objetos com a estrutura:
  - `nome` (string)
  - `cidade` (string)
  - `atletas` (lista de strings — nomes de atletas vinculadas ao clube)
- `atletas`: lista de objetos com a estrutura:
  - `nome` (string)
  - `idade` (inteiro)
  - `posicao` (string — deve existir em `POSITIONS`)
  - `clube` (string — nome do clube)
- `partidas`: lista de objetos com a estrutura:
  - `clubeA` (string)
  - `clubeB` (string)
  - `placar` (string no formato "<golsA> x <golsB>")

No início da execução, `main.py` sincroniza os atletas (cada atleta cujo campo `clube` corresponde ao nome de um clube tem seu nome adicionado à lista `atletas` do respectivo clube).

## ✅4. Funcionalidades implementadas (conforme `main.py`)

Leitura e validação de entrada

- `read_non_empty(prompt)` — solicita texto não-vazio e rejeita entradas numéricas.
- `read_positive_int(prompt)` — solicita um inteiro não-negativo.
- `select_option(options, prompt, allow_blank=False)` — apresenta uma lista numerada e valida a escolha do usuário.

Operações principais (CRUD em memória)

- `cadastrar_atleta()` — cadastra uma atleta (nome, idade, posição e vínculo a um clube existente). Atualiza também a lista `clubes[].atletas` em memória.
- `cadastrar_clube()` — cria um novo clube com `nome`, `cidade` e uma lista vazia de `atletas`.
- `registrar_partida()` — registra uma partida entre dois clubes (impede que o clube jogue contra si mesmo) e armazena o placar.
- `listar_atletas()`, `listar_clubes()`, `listar_partidas()` — exibem os registros atualmente carregados em memória.

Interface

- `menu()` — loop principal que apresenta opções numeradas e executa as ações correspondentes.

Observação atual: embora o programa carregue `pb.json` ao iniciar, ele não grava automaticamente as alterações de volta no arquivo. Todas as operações CRUD acontecem em memória apenas durante a execução.

## ⚠️5. Proteções e tratamento de erros

O código já implementa validações básicas (não aceita strings vazias, força números inteiros não-negativos, valida seleção a partir de listas). A leitura do arquivo `pb.json` é feita sem bloco try/except atualmente — portanto, erros como arquivo ausente ou JSON inválido levantarão exceções ao iniciar. Para a Sprint 4, recomenda-se envolver a leitura/escrita em blocos `try/except` para tratar erros de I/O e JSON de forma amigável.

## ▶️6. Como rodar

1. Certifique-se de ter Python 3 instalado.
2. Abra um terminal na pasta do projeto (onde estão `main.py` e `pb.json`).
3. Execute:

```bash
python main.py
```

4. Use o menu interativo (opções 1 a 7). Não há pacotes adicionais a instalar.

## 👥 Integrantes A-Z

- Caio Nascimento Caminha
- Gabriel Alexandre Fukushima Sakura
- Gabriel Oliveira Amaral
- Lucas Henrique Viana Estevam Sena
- Rafael Tavares Santos

## 📜 Licença

Projeto acadêmico. Uso livre para fins educacionais.
