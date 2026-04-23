#===================================================================================================
#                                    ESTAÇÕES METRO RECIFE - PE
#===================================================================================================

linha_camaragibe = [
    {"id": 1, "nome": "Recife", "tempo": 2},
    {"id": 2, "nome": "Joana Bezerra", "tempo": 2},
    {"id": 3, "nome": "Afogados", "tempo": 2},
    {"id": 4, "nome": "Ipiranga", "tempo": 2},
    {"id": 5, "nome": "Mangueira", "tempo": 2},
    {"id": 6, "nome": "Santa Luzia", "tempo": 2},
    {"id": 7, "nome": "Werneck", "tempo": 2},
    {"id": 8, "nome": "Barro", "tempo": 2},
    {"id": 9, "nome": "Tejipio", "tempo": 2},
    {"id": 10, "nome": "Coqueiral", "tempo": 3},
    {"id": 11, "nome": "Alto do Ceu", "tempo": 1},
    {"id": 12, "nome": "Curado", "tempo": 2},
    {"id": 13, "nome": "Rodoviaria", "tempo": 1},
    {"id": 14, "nome": "Cosme e Damiao", "tempo": 2},
    {"id": 15, "nome": "Camaragibe", "tempo": 0},
]


linha_jaboatao = [
    {"id": 1, "nome": "Recife", "tempo": 2},
    {"id": 2, "nome": "Joana Bezerra", "tempo": 2},
    {"id": 3, "nome": "Afogados", "tempo": 2},
    {"id": 4, "nome": "Ipiranga", "tempo": 2},
    {"id": 5, "nome": "Mangueira", "tempo": 2},
    {"id": 6, "nome": "Santa Luzia", "tempo": 2},
    {"id": 7, "nome": "Werneck", "tempo": 2},
    {"id": 8, "nome": "Barro", "tempo": 2},
    {"id": 9, "nome": "Tejipio", "tempo": 2},
    {"id": 10, "nome": "Coqueiral", "tempo": 1},
    {"id": 11, "nome": "Cavaleiro", "tempo": 2},
    {"id": 12, "nome": "Floriano", "tempo": 3},
    {"id": 13, "nome": "Engenho Velho", "tempo": 4},
    {"id": 14, "nome": "Jaboatao", "tempo": 0},
]

#===================================================================================================
#                                            FUNÇÕES
#===================================================================================================

def menu():
        print("=============================================================");
        print("SISTEMA DE CALCULO DE TEMPO DO METRO RECIFE-PE");
        print("=============================================================");
        print("Escolha uma linha para mostrar as estacoes:\n");
        print("1. Linha Camaragibe");
        print("2. Linha Jaboatao");
        print("0. Sair\n");
        print("=============================================================");
        opcao = int(input("Escolha uma opcao: "))

        match opcao:
            case 1:
                estacoes_linha_camaragibe()
                calculo_linha_camaragibe()
                calcular_novamente()
            case 2: 
                estacoes_linha_jaboatao()
                calculo_linha_jaboatao()
                calcular_novamente()
            case 0:
                print("Saindo do programa, até a proxima!")
                print("=============================================================");


#===================================================================================================
#                                    CALCULAR LINHA CAMARAGIBE
#===================================================================================================

def calculo_linha_camaragibe():
    print()
    inicio = int(input("Digite a primeira estação: "))
    fim = int(input("Digite a segunda estação: "))
    print()
    print("=============================================================")
    print()

    if inicio < 1 or inicio > 15 or fim < 1 or fim > 15:
        print("Número de estação inválido. Escolha novamente sua Linha!")
        menu()

    # converte para índice da lista
    inicio -= 1
    fim -= 1

    tempo_total = 0

    if inicio == fim:
        print("Você escolheu a mesma estação.")
        print("Tempo total: 0 minutos")
        return

    elif inicio < fim:
        print(
            f'Calculando o tempo de viagem entre a Estação '
            f'{linha_camaragibe[inicio]['nome']} e a Estação '
            f'{linha_camaragibe[fim]['nome']}\n'
        )

        for i in range(inicio, fim):
            tempo_total += linha_camaragibe[i]["tempo"]

    else:
        print(
            f'Calculando o tempo de viagem entre a Estação '
            f'{linha_camaragibe[inicio]["nome"]} e a Estação '
            f'{linha_camaragibe[fim]["nome"]}\n'
        )

        for i in range(fim, inicio):
            tempo_total += linha_camaragibe[i]["tempo"]

    print(f"[Estação {linha_camaragibe[inicio]["nome"]}] ------------- [{tempo_total} Minutos] ------------- [Estação {linha_camaragibe[fim]["nome"]}] ")
    print()
    print("=============================================================");


#===================================================================================================
#                                    CALCULAR LINHA JABOATÂO
#===================================================================================================

def calculo_linha_jaboatao():
    print()
    inicio = int(input("Digite a primeira estação: "))
    fim = int(input("Digite a segunda estação: "))
    print("=============================================================")
    print()

    if inicio < 1 or inicio > 14 or fim < 1 or fim > 14:
        print("Número de estação inválido. Escolha novamente a sua Linha!")
        menu()

    # converte para índice da lista
    inicio -= 1
    fim -= 1

    tempo_total = 0

    if inicio == fim:
        print("Você escolheu a mesma estação.")
        print("Tempo total: 0 minutos")
        return

    elif inicio < fim:
        print(
            f'Calculando o tempo de viagem entre a Estação '
            f'{linha_jaboatao[inicio]['nome']} e a Estação '
            f'{linha_jaboatao[fim]['nome']} \n'
        )

        for i in range(inicio, fim):
            tempo_total += linha_jaboatao[i]['tempo']
    else:
        print(
            f'Calculando o tempo de viagem entre a Estação '
            f'{linha_jaboatao[inicio]['nome']} e a Estação '
            f'{linha_jaboatao[fim]['nome']} \n'
        )

        for i in range(fim, inicio):
            tempo_total += linha_jaboatao[i]['tempo']

    print(f"[Estação {linha_jaboatao[inicio]['nome']}] ------------- [{tempo_total} Minutos] ------------- [Estação {linha_jaboatao[fim]['nome']}] ")
    print()
    print("=============================================================");

#===================================================================================================
#                                  FUNÇÃO DE RETORNO PARA O MENU
#===================================================================================================

def calcular_novamente():
    opcao = input("Deseja calcular outra Linha? [S/N] ").upper()
    
    if opcao not in ("S", "N"):
        print("Opção Invalida!")
        calcular_novamente()
    elif opcao == "S":
        menu()
    else:
        print("Saindo do programa, até a proxima!")
        print("=============================================================\n\n")


#===================================================================================================
#                                   FUNÇÃO DE EXIBIR ESTAÇÕES
#===================================================================================================

def estacoes_linha_camaragibe():
    print("=============================================================")
    print("                      LINHA CAMARAGIBE                       ")
    print("=============================================================")
    for estacao in linha_camaragibe:
        print(f"{estacao['id']} - {estacao['nome']}")
    print("=============================================================");
    print()

def estacoes_linha_jaboatao():
    print("=============================================================")
    print("                       LINHA JABOATÃO                        ")
    print("=============================================================")
    for estacao in linha_jaboatao:
        print(f"{estacao['id']} - {estacao['nome']}")
    print()
    print("=============================================================");

#===================================================================================================
#                                         MENU PRINCIPAL
#===================================================================================================
menu()