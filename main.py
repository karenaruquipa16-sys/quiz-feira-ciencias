# Variáveis de estado
tentativas = 3
pontos = 0

# pergunta
pergunta = 'Quantos lados tem um triângulo'
while tentativas > 0:
    pontos = 0
    resposta = int(input(pergunta))

    if resposta == 3:
        print('Resposta correta!')
        pontos = pontos + 1
        print(f'Pontuação: {pontos}.')
        break
    else:
        print( 'Resposta errada...')
        tentativas = tentativas - 1
        print(f'Você tem {tentativas} tentativas...')
