import utills.auxiliar

def inscricao():
    id = utills.auxiliar.id_inscricao()
    dados = utills.auxiliar.ler_json()
    utills.auxiliar.titulo('Dados Pessoais')
    nome = utills.auxiliar.validar_nome()
    cpf = utills.auxiliar.validar_cpf()
    email = utills.auxiliar.validar_email()
    data_nasc = utills.auxiliar.validar_datanasc()
    telefone = utills.auxiliar.validar_telefone()
    utills.auxiliar.subtitulo('Dados de Endereço')
    cep = utills.auxiliar.validar_cep()
    utills.auxiliar.titulo('Informações Escolares')
    formacao = utills.auxiliar.validar_formacao()
    escola = utills.auxiliar.validar_escola_atual()
    rede = utills.auxiliar.validar_rede_de_ensino()
    utills.auxiliar.titulo('Escolha do Curso, Instituição E Turno')
    curso = utills.auxiliar.escolha_curso()
    utills.auxiliar.subtitulo('Instituição')
    local = utills.auxiliar.validar_instituicao()
    utills.auxiliar.subtitulo('Turno')
    turno = utills.auxiliar.validar_turno()
    dado = {'id': id,
            'nome':nome,
            'cpf':cpf,
            'data de nascimento':data_nasc,
            'cep':cep,
            'telefone':telefone,
            'e-mail':email,
            'formacao':formacao,
            'escola': escola,
            'rede de ensino': rede,
            'Curso':curso,
            'instituicao':local,
            'turno':turno}
    dados.append(dado)
    print('\033[31mGuarde esse id para poder consultar sua inscrição depois!')
    print(f'ID:{id}\033[m]')
    utills.auxiliar.salvar_json(dados)


def consulta_de_inscricao():
    utills.auxiliar.titulo('Consulta de Inscrição')
    dados = utills.auxiliar.ler_json()
    veri = False
    while True:
        try:
            id = int(input('Digite o id da sua inscrição: '))
            for dado in dados:
                if id == dado['id']:
                    for i,o in dado.items():
                        print(f'{i} : {o}\n')
                    veri = True
            if veri == False:
                print('Inscrição não encontrada!')
            else:
                break
        except ValueError:
            print('Digite um número inteiro!')

                        
    
    
    