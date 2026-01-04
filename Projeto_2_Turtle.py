from turtle import Turtle
tartaruga = Turtle()
tartaruga.speed(1)
while True:
#Definindo qual direção ir inicial
    direcao = str(input('Deseja movimentar para frente ou para trás(F=Frente ou T=Trás 0=Sair): ')).upper()
    if direcao not in ["F", "T", "0"]:
        print('Opção inválida!')
        continue
    if direcao == "0":
        print('Encerrando o Programa...')
        break
    
    if direcao == 'F':
        distancia = int(input(f'Qual a distancia em pixels para {direcao}: '))
        tartaruga.forward(distancia)
    elif direcao == 'T':
        distancia = int(input(f'Qual a distancia em pixels para {direcao}: '))
        tartaruga.backward(distancia)
#Definindo qual rotação fazer
    rotação = int(input('''Para qual direção quer rotacionar: 
        [ 1 ]Direita
        [ 2 ]Esquerda
        [ 3 ]Não Rotacionar
    '''))
#Rotação a Direita
    if rotação == 1:
        direita = int(input('Quantos Graus a direita deseja virar?: '))
        tartaruga.right(direita)
#Rotação a Esquerda
    elif rotação == 2:
        esquerda = int(input('Quantos graus quer virar a Esquerda?: '))
        tartaruga.left(esquerda)
#Não rotacionar
    elif rotação == 3:
        continue
