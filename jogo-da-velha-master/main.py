from jogo_da_velha import criarBoard, fazMovimento,  getInputValido, \
                            printBoard, verificaGanhador,  verificaMovimento

from minimax import movimentoIA

print("0 - Maquina x Jogador")
print("1 - Jogador 1 x Jogador 2")
jogador = int(input("Opcao :"))

jogador0 = 0 # jogador 1
jogador1 = 1
board = criarBoard()
ganhador = verificaGanhador(board)
if (jogador0 == jogador):
    while(not ganhador): #enquanto não tiver um ganhador
        printBoard(board)
        print("===================")
        if(jogador0 == jogador): # DEFINE A IA COMO JOGADOR
            #print("entrou no 0") teste
            i,j = movimentoIA(board, jogador0)
        else: # PLAYER
            i = getInputValido("Digite a linha: ")
            j = getInputValido("Digite a coluna: ")
        
        if(verificaMovimento(board, i, j)):
            fazMovimento(board, i, j, jogador0)
            jogador0 = (jogador0 + 1)%2
        else:
            print("A posicao informado ja esta ocupada")
        ganhador = verificaGanhador(board)

elif(jogador1 == jogador): # Jogador vs Jogador
    while(not ganhador): #enquanto não tiver um ganhador
        printBoard(board)
        print("===================")
        i = getInputValido("Digite a linha: ")
        j = getInputValido("Digite a coluna: ")
            
        if(verificaMovimento(board, i, j)):
            fazMovimento(board, i, j, jogador1)
            jogador1 = (jogador1 + 1)%2
        else:
            print("A posicao informado ja esta ocupada")
        ganhador = verificaGanhador(board)
else:
    print("Opcao Invalida")

 
print("===================")
printBoard(board)
print("Ganhador = ", ganhador)
print("===================")