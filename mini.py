import random  # geração de números aleatórios (dado)
import os      # interação com o sistema (terminal)


# CONFIGURAÇÃO DE CORES (TERMINAL)

os.system("")  # necessário para ativar cores no Windows

RESET = "\033[0m"     # reset de cor
VERDE = "\033[92m"    # sucesso / positivo
VERMELHO = "\033[91m" # erro / negativo
AMARELO = "\033[93m"  # alerta 
AZUL = "\033[94m"     # informação


# EXEMPLOS DE TIPOS DE DADOS

quantidade_jogadores = 2      # int
taxa_bonus = 1.5              # float
nome_jogo = "Mini Monopoly"   # str
jogo_ativo = True             # bool

print(f"{AZUL}🎮 Bem-vindo ao {nome_jogo}!{RESET}")


# INPUT + CONVERSÃO DE TIPOS

bonus_inicial = float(input("Digite um bônus inicial para os jogadores: "))


# DADOS DOS JOGADORES

nomes = ["😎 Jogador 1", "🤖 Jogador 2"]  # identificação dos jogadores
saldos = [1000 + bonus_inicial, 1000 + bonus_inicial]  # dinheiro inicial
posicoes = [0, 0]                        # posição no tabuleiro
vivos = [True, True]                     # status (ativo ou falido)


# DEFINIÇÃO DO TABULEIRO

tabuleiro = [
    "🏁 Início",
    "🏠 Casa A",
    "🎁 Evento",
    "🏠 Casa B",
    "⚠️ Multa",
    "🏠 Casa C",
]


# CONFIGURAÇÃO DAS PROPRIEDADES

precos = {
    "🏠 Casa A": 200,
    "🏠 Casa B": 300,
    "🏠 Casa C": 400
}  # valor de compra

aluguéis = {
    "🏠 Casa A": 20,
    "🏠 Casa B": 30,
    "🏠 Casa C": 50
}  # valor de aluguel

donos = {}  # mapeia propriedade -> jogador


# FUNÇÕES PRINCIPAIS DO JOGO

def rolar_dado():
    """Gera um número de 1 a 6 simulando um dado"""
    dado = random.randint(1, 6)
    print(f"{AZUL}🎲 Dado: {dado}{RESET}")
    return dado


def mostrar_status(i):
    """Exibe saldo e status do jogador"""
    status = "💀 FALIDO" if not vivos[i] else ""
    print(f"{VERDE}💰 {nomes[i]}: R${saldos[i]} {status}{RESET}")


def evento(i):
    """Aplica evento aleatório de ganho ou perda"""
    valor = random.choice([200, -150, 100, -50])
    saldos[i] += valor

    if valor > 0:
        print(f"{VERDE}🎁 {nomes[i]} ganhou R${valor}{RESET}")
    else:
        print(f"{VERMELHO}⚠️ {nomes[i]} perdeu R${abs(valor)}{RESET}")


def verificar_propriedade(i, casa):
    """Gerencia compra e pagamento de aluguel"""
    if casa not in donos:
        print(f"{AMARELO}{casa} custa R${precos[casa]}{RESET}")

        if saldos[i] >= precos[casa]:
            escolha = input("Comprar? (s/n): ").lower()

            if escolha == "s":
                saldos[i] -= precos[casa]
                donos[casa] = i
                print(f"{VERDE}✔️ Propriedade adquirida!{RESET}")
        else:
            print(f"{VERMELHO}💸 Saldo insuficiente{RESET}")

    else:
        dono = donos[casa]

        if dono != i:
            aluguel = aluguéis[casa]
            saldos[i] -= aluguel
            saldos[dono] += aluguel

            print(f"{VERMELHO}💸 Pagou R${aluguel} para {nomes[dono]}{RESET}")


def verificar_falencia(i):
    """Verifica se o jogador ficou sem dinheiro"""
    if saldos[i] < 0:
        vivos[i] = False
        print(f"{VERMELHO}💀 {nomes[i]} faliu!{RESET}")


def verificar_vitoria():
    """Define condição de vitória"""
    ativos = [i for i in range(len(nomes)) if vivos[i]]

    if len(ativos) == 1:
        print(f"\n{VERDE}🏆 VENCEDOR: {nomes[ativos[0]]}{RESET}")
        return True

    if len(ativos) == 0:
        print("\n💀 Todos faliram!")
        return True

    return False


def mostrar_tabuleiro():
    """Exibe o tabuleiro com índices"""
    print("\n🗺️ TABULEIRO:")
    for i, casa in enumerate(tabuleiro):
        print(f"{i} - {casa}")



# LOOP PRINCIPAL DO JOGO


rodada = 1

while True:
    print(f"\n======== 🕹️ Rodada {rodada} ========")
    mostrar_tabuleiro()

    for i in range(len(nomes)):
        if not vivos[i]:
            continue

        print(f"\n🎮 Turno de {nomes[i]}")
        input("Pressione ENTER para jogar...")

        dado = rolar_dado()

        # movimentação com retorno ao início (%)
        posicoes[i] = (posicoes[i] + dado) % len(tabuleiro)

        casa = tabuleiro[posicoes[i]]
        print(f"📍 Caiu em: {casa}")

        if casa == "🎁 Evento":
            evento(i)

        elif casa == "⚠️ Multa":
            print(f"{VERMELHO}💸 Multa de R$100{RESET}")
            saldos[i] -= 100

        elif casa in precos:
            verificar_propriedade(i, casa)

        verificar_falencia(i)
        mostrar_status(i)

        if verificar_vitoria():
            exit()

    rodada += 1