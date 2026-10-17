from utills.auxiliar import validar_cpf,salvar_json,validar_email,ler_json

def inscricao():
    dados = ler_json()
    cpf = validar_cpf()
    email = validar_email()
    dado = {'cpf':cpf,
             'e-mail':email}
    dados.append(dado)
    salvar_json(dados)
    
    
    