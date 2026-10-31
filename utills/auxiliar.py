import json
from cidades.lista import cidade_mg
import re
from datetime import datetime


def titulo(texto):
    print('='*40)
    print(texto.center(40))
    print('='*40)


def subtitulo(texto):
     print('='*20)
     print(texto.center(20))
     print('='*20)


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
                         if nascimento < hoje:
                              return data
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
     while True:
          nome = input('Digite seu nome completo: ')
          nome2 = nome.lower()
          if re.search(r'[a-z]+',nome2) and not(re.search(r'\d+',nome)):
               return nome
          else:
               print('Nome inválido')

def validar_instituicao():
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
     


     