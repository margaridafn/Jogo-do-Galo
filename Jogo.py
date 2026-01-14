from random import randrange
#Serve para o computador escolher uma jogada aleatória.

def display_board(board):                                        
#Recebe o tabuleiro (board) como argumento.
	print("+-------" * 3,"+", sep="")
#Desenha a linha superior do tabuleiro.
	for row in range(3):
#Percorre as 3 linhas.
		print("|       " * 3,"|", sep="")
#Espaço vazio acima dos números/símbolos.
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ", end="")
#Mostra cada posição do tabuleiro.
#Pode ser um número, O ou X.
		print("|")
#Fecha a linha.
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")
#Espaço vazio abaixo + linha de separação.
#Esta função só desenha o tabuleiro, não altera nada.

#Jogada do jogador.
def enter_move(board):
	ok = False	
	while not ok:
#Repete até o jogador fazer uma jogada válida.
		move = input("Coloque o número da casa que quer jogar: ") 
#Pede um número entre 1 e 9.
		ok = len(move) == 1 and move >= '1' and move <= '9' 
#Verifica se:
#tem 1 carácter.
#está entre '1' e '9'.
		if not ok:
			print("Inválido – repita a sua jogada!") 
#Se for inválido, volta a pedir.
			continue
		move = int(move) - 1 
#Converte para número.
#Subtrai 1 para adaptar aos índices (0 a 8).	
		row = move // 3 	
		col = move % 3	
#Converte o número numa linha e coluna.	
		sign = board[row][col]	
		ok = sign not in ['O','X'] 
#Verifica se a casa está livre.
		if not ok:	
			print("Campo já está ocupado – repita a sua jogada!")
			continue
	board[row][col] = 'O' 	
#Coloca o O no tabuleiro.

#Descobre casas livres.
def make_list_of_free_fields(board):
	free = []	
#Lista vazia.
	for row in range(3): 
		for col in range(3): 
#Percorre todo o tabuleiro.
			if board[row][col] not in ['O','X']: 
				free.append((row,col)) 
#Se não tiver O nem X → está livre.
	return free
#Devolve uma lista com posições livres.

#Verifica se alguém ganhou.
def victory_for(board,sgn):
	if sgn == "X":	
		who = 'me'	
	elif sgn == "O": 
		who = 'you'	
#Define quem ganhou.
	else:
		who = None	
	cross1 = cross2 = True  
#Para verificar diagonais.
	for rc in range(3):
#Verifica:
#linhas.
#colunas.
#diagonais.
		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:	
			return who
#Linha completa.
		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: 
			return who
#Coluna completa.
		if board[rc][rc] != sgn: 
			cross1 = False
#Diagonal principal.
		if board[2 - rc][2 - rc] != sgn: 
			cross2 = False
#Outra diagonal.
	if cross1 or cross2:
		return who
	return None
#Ninguém ganhou.

#Jogada do computador.
def draw_move(board):
	free = make_list_of_free_fields(board)
#Casas livres. 
	cnt = len(free)
	if cnt > 0:	
		this = randrange(cnt)
#Escolhe uma posição aleatória.
		row, col = free[this]
		board[row][col] = 'X'
#Coloca o X.


board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] 
board[1][1] = 'X' 
#Computador começa no centro.
free = make_list_of_free_fields(board)
human_turn = True 
while len(free):
#Enquanto houver casas livres.
	display_board(board)
	if human_turn:
		enter_move(board)
#Jogador.
		victor = victory_for(board,'O')
	else:	
		draw_move(board)
#Computador.		victor = victory_for(board,'X')
	if victor != None:
		break
#Verifica vitória.
	human_turn = not human_turn	
#Alterna turno.	
	free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
	print("O computador ganhou!")
elif victor == 'me':
	print("Você ganhou!")
else:
	print("Empate!")