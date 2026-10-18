from utills.auxiliar import validar_cpf,salvar_json,validar_email,ler_json,escolha_curso,id_inscricao,titulo

def inscricao():
    id = id_inscricao()
    dados = ler_json()
    titulo('Dados Pessoais')
    cpf = validar_cpf()
    email = validar_email()
    titulo('Escolha do Curso E Instituição')
    curso = escolha_curso()
    dado = {'id': id,
            'cpf':cpf,
             'e-mail':email,
             'Curso':curso}
    dados.append(dado)
    salvar_json(dados)
    
    
    