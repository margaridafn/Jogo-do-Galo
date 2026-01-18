# Jogo do Galo

Este repositório contém uma implementação simples em linha de comandos do jogo do galo, conhecido como *Jogo do Galo* em português. Este projeto foi desenvolvido como trabalho final do curso Python Essentials 1.

## Jogabilidade

Este é um jogo para um jogador, onde se compete contra o computador.

* O jogo é jogado numa grelha 3x3.

* Joga-se como 'O' e o computador joga como 'X'.
* O computador faz sempre o primeiro movimento, colocando um 'X' no quadrado central.

* Os jogadores revezam-se colocando as suas marcas em quadrados vazios.

* Ganha o primeiro jogador a alinhar três das suas marcas horizontalmente, verticalmente ou diagonalmente.

* Se todos os quadrados estiverem preenchidos e ninguém tiver ganho, o jogo termina empatado.

## Como Jogar

1. Certifique-se de que tem o Python 3 instalado no seu sistema.

2.º Clone ou descarregue este repositório para a sua máquina local. 3.º Abra um terminal ou uma linha de comandos e navegue até ao diretório do projeto.
4.º Execute o jogo com o seguinte comando:

```

python Jogo.py

```
5.º O tabuleiro do jogo será apresentado. Quando for a sua vez, introduza um número de 1 a 9 correspondente à casa onde pretende colocar o seu 'O'.

## Visão Geral do Código

Toda a lógica do jogo está contida no script `Jogo.py`. Aqui está uma descrição das principais funções:

* `display_board(board)`: Apresenta o estado atual do tabuleiro 3x3 na consola.

* `enter_move(board)`: Gere a vez do jogador humano. Solicita a entrada, valida se a casa escolhida é válida e está desocupada e, em seguida, atualiza o tabuleiro com um 'O'.

* `make_list_of_free_fields(board)`: Analisa o tabuleiro e devolve uma lista de todas as casas actualmente vazias.
* `victory_for(board, sgn)`: Verifica se o jogador com o sinal fornecido ('X' ou 'O') obteve uma combinação vencedora.
* `draw_move(board)`: Executa a jogada do computador seleccionando aleatoriamente uma das casas livres disponíveis e colocando um 'X' na mesma.

O script inicializa o tabuleiro, define a primeira jogada do computador no centro e, em seguida, entra num loop que alterna as jogadas entre o utilizador e o computador até que uma condição de vitória ou empate seja cumprida.