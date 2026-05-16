## 🎮 Mini Monopoly Python

Um jogo simples e interativo em Python para praticar conceitos básicos de programação.

## Integrantes do Grupo
- Lucas Silva - [lNascimento-01](https://github.com/lnascimento-01)
- Danilo Bragion -[danilobbragion-stack](https://github.com/danilobbragion-stack)
- Kaique Martins -[kaiquemartinscont-collab](https://github.com/kaiquemartinscont-collab)
- Eduardo Peres - [duuhperes](https://github.com/duuhperes)
- Gabriel Tomaz - [001gabrieltomazmiranda-ship-it](https://github.com/001gabrieltomazmiranda-ship-it)
- Igor Brito - [iiGo-tch](https://github.com/iigo-tch)

## Descrição do Projeto

Este projeto consiste em um jogo interativo desenvolvido em Python que roda diretamente no console.
O jogo é inspirado no clássico Banco Imobiliário (Monopoly), onde os jogadores percorrem um tabuleiro, compram propriedades, pagam aluguel, enfrentam eventos aleatórios e tentam evitar a falência.

O programa utiliza sistema de turnos, rolagem de dados, gerenciamento de saldo e condições de vitória para tornar a experiência dinâmica e divertida.

## Pré-requisitos

Para rodar este projeto, necessário ter o Python 3.x instalado em sua máquina, o que estou usando no momento é o 3.14.3.
Para verificar se você já possui o Python instalado, abra o terminal e digite:

python --version

Download Python

Extensões Recomendadas (VS Code)

Caso utilize o Visual Studio Code, as seguintes extensões são recomendadas para desenvolvimento em Python:


| Extensão                                                                                                            | Função                              |
| ------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| [Python (Microsoft)](https://marketplace.visualstudio.com/items?itemName=ms-python.python&utm_source=chatgpt.com)   | Suporte completo ao Python          |
| [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance&utm_source=chatgpt.com)      | Autocompletar e análise inteligente |
| [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy&utm_source=chatgpt.com)     | Depuração do código                 |
| [autopep8](https://marketplace.visualstudio.com/items?itemName=ms-python.autopep8&utm_source=chatgpt.com)           | Formatação automática do código     |
| [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner&utm_source=chatgpt.com) | Executar código rapidamente         |


1. Clone o repositório:
git clone https://github.com/lNascimento-01/Projeto-Monopoly

2. Acesse a pasta do projeto:
mini.py

3. Execute o arquivo principal:
python mini.py

4. No terminal, insira o bônus inicial dos jogadores e siga as instruções exibidas durante as rodadas do jogo.
Explicação Técnica

O projeto foi desenvolvido aplicando os seguintes conceitos de lógica de programação dados em sala de aula:

Importação de Bibliotecas
Utilizamos import random para geração de números aleatórios simulando o dado e import os para interação com o terminal.
Estruturas de Repetição
O uso do while True garante que o jogo continue em execução até existir um vencedor ou todos os jogadores falirem.
Controle de Fluxo (Condicionais)
Aplicamos if, elif e else para controlar eventos do jogo como compra de propriedades, multas, eventos aleatórios e falência.
Funções
O sistema foi dividido em funções para organizar melhor a lógica do jogo, como:
rolar_dado()
mostrar_status()
evento()
verificar_propriedade()
verificar_falencia()
verificar_vitoria()
Entrada e Saída de Dados
Uso de input() para capturar ações do jogador e print() para exibir informações do jogo no terminal.
Estruturas de Dados
Foram utilizadas listas e dicionários para armazenar:
jogadores
saldos
propriedades
aluguéis
posições no tabuleiro
Manipulação de Terminal
O projeto utiliza códigos ANSI para exibir mensagens coloridas no console, melhorando a experiência visual do usuário.
Demonstração

Exemplo de execução no terminal:

🎮 Bem-vindo ao Mini Monopoly!

======== 🕹️ Rodada 1 ========

🗺️ TABULEIRO:
0 - 🏁 Início
1 - 🏠 Casa A
2 - 🎁 Evento
3 - 🏠 Casa B
4 - ⚠️ Multa
5 - 🏠 Casa C

🎮 Turno de 😎 Jogador 1

🎲 Dado: 4
📍 Caiu em: ⚠️ Multa
💸 Multa de R$100

💰 😎 Jogador 1: R$900
Funcionalidades
🎲 Sistema de dado aleatório
🏠 Compra de propriedades
💸 Sistema de aluguel
🎁 Eventos aleatórios
⚠️ Sistema de multas
💀 Sistema de falência
🏆 Verificação automática de vencedor
🎨 Interface colorida no terminal
🗺️ Tabuleiro interativo
