# Início do programa - solicitamos as coordenadas de X e Y e convertemos no tipo int:

x = int(input("Digite a coordenada inicial no eixo x de 0 a 10:"))
y = int(input("Digite a coordenada inicial no eixo y de 0 a 10:"))

# Importamos duas bibliotecas de Python que iremos utilizar para gerar uma posição aleatória para o Professor

from random import seed
from random import choice

seed(1)
tamanho_mapa = [i for i in range(11)]

for _ in range(1):
    professor_x = choice(tamanho_mapa)

for _ in range(1):
    professor_y = choice(tamanho_mapa)

# Agora vamos pedir ao jogador para definir o caminho desejado e realizaremos a análise de coordenadas em sequência.

destino = input(
    "Digite o caminho a percorrer, sendo N para norte, O para oeste, L para leste e S para sul. Dê um espaço entre cada letra. Exemplo - N N O L L S:").split()

print("O caminho digitado foi: ", destino)

# Vamos inserir os valores das coordenadas fornecidas em "x1 e y1" para calcular o destino final a partir da trajetória escolhida:
x1 = x
y1 = y

for i in (destino):

    if i == "N":
        y1 = y1 + 1

    elif i == "S":
        y1 = y1 - 1

    elif i == "L":
        x1 = x1 + 1

    elif i == "O":
        x1 = x1 - 1

    else:
        print("Caminho inválido.")

# Agora vamos descobrir se iremos encontrar o professor no caminho:

caminho = destino
x2 = x
y2 = y

for i in (caminho):

    if i == "N":
        y2 = y2 + 1
        if (y2 == professor_y):
            y2 = y2 - 1

    elif i == "S":
        y2 = y2 - 1
        if (y2 == professor_y):
            y2 = y2 + 1

    elif i == "L":
        x2 = x2 + 1
        if (x2 == professor_x):
            x2 = x2 - 1

    elif i == "O":
        x2 = x2 - 1
        if (x2 == professor_x):
            x2 = x2 + 1


# início da função para tentar jogar novamente

def tentar_novamente():
    destino = input(
        "Digite o caminho a percorrer, sendo N para norte, O para oeste, L para leste e S para sul. Exemplo - N N O L L S:").split()

    x1 = x
    y1 = y

    for i in (destino):

        if i == "N":
            y1 = y1 + 1

        elif i == "S":
            y1 = y1 - 1

        elif i == "L":
            x1 = x1 + 1

        elif i == "O":
            x1 = x1 - 1

        else:
            print("Caminho inválido.")

    caminho = destino
    x2 = x
    y2 = y

    for i in (caminho):

        if i == "N":
            y2 = y2 + 1
            if (y2 == professor_y):
                y2 = y2 - 1

        elif i == "S":
            y2 = y2 - 1
            if (y2 == professor_y):
                y2 = y2 + 1

        elif i == "L":
            x2 = x2 + 1
            if (x2 == professor_x):
                x2 = x2 - 1

        elif i == "O":
            x2 = x2 - 1
            if (x2 == professor_x):
                x2 = x2 + 1

    if (x1 == x2) and (y1 == y2):
        print("Você conseguiu chegar ao destino nas coordenadas: (", x1, ", ", y1, ")")

    else:
        print("Você não conseguiu chegar ao destino e parou nas coordenadas: (", x2, ", ", y2, ")")


# fim da função definida

# Final do jogo - aqui damos o resultado e a opção de jogar novamente chamando a função "tentar_novamente()":

if (x1 == x2) and (y1 == y2):
    print("Você conseguiu chegar ao destino nas coordenadas: (", x1, ", ", y1, ")")
    print("O professor estava no corredor: (", professor_x, ", ", professor_y, ")")

else:
    print("Você não conseguiu chegar ao destino e parou nas coordenadas: (", x2, ", ", y2, ")")

jogar = input("Tentar novamente? Digite S para SIM ou N para NÃO:")

while (jogar == "S") or (jogar == "SIM") or (jogar == "s") or (jogar == "sim"):
    tentar_novamente()
    jogar = input("Tentar novamente? Digite S para SIM ou N para NÃO:")

print("FIM DO JOGO")
print("Feche o navegador para sair.")

# Fim do programa.