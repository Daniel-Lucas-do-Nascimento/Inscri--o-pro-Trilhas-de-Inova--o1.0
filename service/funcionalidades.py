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
            'Curso':curso,
            'instituicao':local,
            'turno':turno}
    dados.append(dado)
    utills.auxiliar.salvar_json(dados)
    
    
    