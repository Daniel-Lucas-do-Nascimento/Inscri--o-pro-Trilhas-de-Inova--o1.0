import json
from cidades.lista import cidade_mg,escolas_mg
import re
from datetime import datetime


def titulo(texto):
    print('='*40)
    print(texto.center(40))
    print('='*40)


def subtitulo(texto):
     print('='*30)
     print(texto.center(30))
     print('='*30)



def salvar_json(dados):
    with open('data/inscritos.json' , 'w') as arq:
        json.dump(dados,arq,indent = 4, ensure_ascii = False)


def ler_json():
    with open('data/inscritos.json','r') as arquivo:
        dados = json.load(arquivo)
    return dados


def validar_cpf():
    dados = ler_json()
    while True:
            verificador_copia = False
            cpf = input('Digite o seu número de CPF [***.***.***-**]: ')
            if len(dados) > 0:
                    for dado in dados:
                        if dado['cpf'] == cpf:
                            verificador_copia = True
            if re.search(r"\d\d\d.\d\d\d.\d\d\d-\d\d",cpf) and verificador_copia == False:
                return cpf
            elif verificador_copia == True:
                print('CPF já cadastrado!')
            else:
                print('Formato de CPF inválido!')


def validar_email():
     dados = ler_json()
     while True:
          verificador_copia = False
          email = input('Digite seu e-mail: ')
          if len(dados) > 0:
               for dado in dados:
                    if dado['e-mail'] == email:
                         verificador_copia = True
          if re.search(r"@gmail.com",email) and verificador_copia == False and (not re.search(r"\s",email)) and (not(re.search(r"[A-Z]",email))) or re.search(r"@hotmail.com",email) and verificador_copia == False and (not re.search(r"\s",email)) and (not(re.search(r"[A-Z]",email))):
               return email
          elif verificador_copia == True:
               print('E-mail já cadastrado!')
          else:
               print('Formato de e-mail inválido!')


def escolha_curso():
     titulo('Escolha do Curso, Instituição E Turno')
     cursos = ['Desenvolvimento de Software',
    'Estetíca',
    'Cabelereiro',
    'Informática',
    'Administração',
    'Logística',
    'Gastronomia', 
    'Confeitaria', 
    'Panificação', 
    'Alimentos', 
    'Modelagem do Vestuário']
     for ind,curso in enumerate(cursos):
          print(f'[{ind + 1}]:{curso}')
     while True:
        try:
            esco = int(input('Digite o número do curso escolhido: '))
            if esco > 0 and esco < len(cursos):
                break
            else:
                 print('Escolha de curso inválida!')
        except ValueError:
             print('Formato de escolha inválido! Digite um número inteiro!')
     return cursos[esco-1]


def id_inscricao():
     maior_id = 0
     dados = ler_json()
     if len(dados) > 0:
        for dado in dados:
             if dado['id'] > maior_id:
                  maior_id = dado['id']
        return maior_id + 1
     else:
          return 1


def validar_datanasc():
     hoje = datetime.today()
     while True:
               data = input('Digite sua data de Nascimento: (**/**/****): ')
               if re.search(r'\d\d/\d\d/\d\d\d\d',data):
                    try:
                         nascimento = datetime.strptime(data,'%d/%m/%Y')
                         idade = hoje.year - nascimento.year
                         if nascimento.year < hoje.year and idade >= 16:
                              return data
                         elif idade < 16:
                              print('\033[31mIdade menor que 16!!\033[m')
                              break
                         else:
                              print('Data de nascimento inválida!')
                    except ValueError:
                         print('Data inexistente!')
               else:
                    print('Formato de Data de nascimento inválido!')


def validar_telefone():
     while True:
          tele = input('Digite seu número de telefone: [(**)****-****]: ')
          tele2 = re.sub(r'[()]','',tele)
          if re.search(r'\d\d\d\d\d\d-\d\d\d\d',tele2) and len(tele2)-1 == 10:
               return tele
          else:
               print('Número de telefone inválido!')



def validar_nome():
     titulo('Dados Pessoais')
     while True:
          nome = input('Digite seu nome completo: ')
          nome2 = nome.lower()
          if re.search(r'[a-z]+',nome2) and not(re.search(r'\d+',nome)):
               return nome
          else:
               print('Nome inválido')



def validar_instituicao():
     subtitulo('Instituição')
     locais = {1: 'Senai(Betim)',
     2: 'Alpha Unipac (Sarzedo)',
     3: 'Graú Técnico (Contagem)',
     4: 'Axioma (Brumadinho)',
     5: 'Senai (Durval de Barros)',
     6: 'Yeshua (Barreiro)'}
     for i,o in locais.items():
          print(f'[{i}]: {o}')
     while True:
          try:
               local = int(input('Selecione o local: '))
               if local > 0 and local <= 6:
                    return locais[local]
               else:
                    print('Escolha de local inválida!')
          except ValueError:
               print('Digite o Número de uma das opções! ')



def validar_turno():
     subtitulo('Turno')
     turnos = {1 : 'Manhã',
               2 : 'Tarde',
               3 : 'Noite'}
     for i,o in turnos.items():
          print(f'[{i}]: {o}')
     while True:
          try:
               turno = int(input('Selecione o seu turno Favorito: '))
               if turno > 0 and turno <= 3:
                    return turnos[turno]
               else:
                    print('Escolha de turno inválida!')
          except ValueError:
               print('Digite o Número do Turno Selecionado!')




def validar_cep():
     subtitulo('Endereço')
     veri = False
     while True:
          cidade = input('Digite o nome da sua cidade: ')
          cidade2 = cidade.lower()
          for cidade3 in cidade_mg:
               if  cidade2 == cidade3: 
                    veri = True
                    return f'Cidade: {cidade} / Estado: Minas Gerais / País: Brasil'
          if veri == False:
               print('Cidade não encontrada!')



def validar_formacao():
     subtitulo('Formação')
     formacao = {1 : 'Ensino Fundamental',
                 2 : 'Ensino Médio',
                 3 : 'Ensino Superior'}
     print(formacao)
     while True:
          try:
               escolaridade = int(input('Digite o número da sua escolaridade: '))
               if escolaridade > 0 and escolaridade <= 3:
                    return formacao[escolaridade]
               else:
                    print('Opção inválida! Digite uma das opções acima!')
          except ValueError:
               print('Digite um número inteiro!')



def validar_escola_atual():
     subtitulo('Escola Atual')
     escolas = escolas_mg
     veri = False
     while True:
          escola_hj = input('Digite o nome da escola onde estuda atualmente: ')
          for escola in escolas:
               if escola_hj.lower() == escola:
                    veri = True
                    return escola_hj
          if veri == False:
               print('Escola não encontrada!')



def validar_rede_de_ensino():
     subtitulo('Rede de Ensino')
     redes = {1 : 'Pública',
              2 : 'Privada'}
     print(redes)
     while True:
          try:
               rede = int(input('Digite a opção que representa sua rede de ensino: '))
               if rede > 0 and rede <= 2:
                    return redes[rede]
               else:
                    print('Opção Inválida!')
          except ValueError:
               print('Digite um número inteiro!')



id = 0
nome = ''
cpf = ''
email = ''
data_nasc = ''
telefone = ''
cep = ''
formacao = ''
escola = ''
rede = ''
curso = ''
local = ''
turno = ''
def entrada_de_dados():
    id = id_inscricao()
    nome = validar_nome()
    cpf = validar_cpf()
    email = validar_email()
    data_nasc = validar_datanasc()
    telefone = validar_telefone()
    cep = validar_cep()
    formacao = validar_formacao()
    escola = validar_escola_atual()
    rede = validar_rede_de_ensino()
    curso = escolha_curso()
    local = validar_instituicao()
    turno = validar_turno()


def cadastro_de_dados():
    dados = ler_json()
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
    print(f'(ID:{id}\033[m)')
    salvar_json(dados)


def consultar_inscricao():
    dados = ler_json()
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



     

     