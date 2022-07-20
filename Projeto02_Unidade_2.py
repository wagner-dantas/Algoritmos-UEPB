'''
UNIVERSIDADE ESTADUAL DA PARAÍBA PÓLO PATOS
CURSO CIÊNCIA DA COMPUTAÇÃO
ANNA PRISCILLA MOREIRA DE FIGUEIREDO - 1º PERÍODO NORTUNO
WAGNER DANTAS MARTINS - 1º PERÍODO NORTUNO
'''

lista_filmes = [] # Armazena a lista de filmes
usuario1_lista_filmes_assitido = [] # armazena os filmes assistido e não assitido pelo usuario
usuario2_lista_filmes_assitido = [] # armazena os filmes assistido e não assitido pelo usuario

# Gera uma Tela do Título do Sistema
#  Recebe como parâmetro o título do sistema
def gerarTelaTituloSistema(titulo):
    for colunas in range(50):
        print('*',end="")
    print()
    espaco_inicial = int((50-len(titulo))/2)
    for inicio_lado_direito in range(espaco_inicial):
        print(' ',end="")
    print(titulo)
    for colunas in range(50):
        print('*',end="")
    print()

#  Gera a lista de filmes
#  recebe como parâmetros a quantidade de filmes a ser salva na lista
def gerarListaFilmes(quantidade_filmes):
    print(f'Por Favor Informe {quantidade_filmes} Filmes!')
    for filme in range(quantidade_filmes):
        nome_filme = ''
        print(f'Informe o Nome do {filme+1}º:')
        while len(nome_filme) == 0:
            nome_filme = input('Nome do Filme: ')
            if len(nome_filme) > 0:
                lista_filmes.append(nome_filme)
            else:
                print('_' * 40)
                print('É obrigatório informar o nome do filme!')
                print('_' * 40)

#  Gera a lista de filmes que o usuário assistiu e que ele não assistiu
#  recebe como parâmetro o usuário
def filmesAssistidosPeloUsuario(usuario):
    print("#"*107)
    print(f'olá usuário {usuario} informe quais filmes você já assistiu da lista abaixo, informando [S] para sim e [N] para não')
    print("#"*107)
    for filme in lista_filmes:
        resposta = ''
        print('_' * 50)
        print(f'Você já Assistiu o Filme {filme}?')
        print('_' * 50)
        while len(resposta) == 0:
            resposta = input('Digite [S] para sim ou [N] para não: ')
            if (resposta.upper() == 'S') or (resposta.upper() == 'N'):
                if usuario == 1:
                    if resposta.upper() == 'S':
                        usuario1_lista_filmes_assitido.append(True)
                    else:
                        usuario1_lista_filmes_assitido.append(False)
                else:
                    if resposta.upper() == 'S':
                        usuario2_lista_filmes_assitido.append(True)
                    else:
                        usuario2_lista_filmes_assitido.append(False)
            else:
                print("#" * 80)
                print('A resposta informada não é válida, por favor informe [S] para sim e [N] para não')
                print("#" * 80)
                resposta = ''

# função responsável por recomendar filmes que os usuários não assistiram
def recomendacoes():
    indice = 0
    for filmes in usuario2_lista_filmes_assitido:
        if filmes:
            if not usuario1_lista_filmes_assitido[indice]:
                print(f'Olá usuário 1, recomendamos o filme {lista_filmes[indice]}')
        indice += 1
    indice = 0
    for filmes in usuario1_lista_filmes_assitido:
        if filmes:
            if not usuario2_lista_filmes_assitido[indice]:
                print(f'Olá usuário 2, recomendamos o filme {lista_filmes[indice]}')
        indice += 1

# EXECUÇÃO DO SISTEMA
gerarTelaTituloSistema('SISTEMA DE RECOMENDAÇOES RUDIMENTAR') #  Gera tela de título do sistema
gerarListaFilmes(10) #  Gera a lista de filmes
filmesAssistidosPeloUsuario(1) #  gera a lista dos filmes assistidos pelo usuário 1
filmesAssistidosPeloUsuario(2) #  gera a lista de filmes assistidos pelo usuário 2
print()
print("#"*31)
print('='*31)
print('RECOMENDAÇÕES PARA OS USUÁRIOS')
print('='*31)
print("#"*31)
recomendacoes() #  recomenda a lista de filmes assistidos para o usuário 1 e 2